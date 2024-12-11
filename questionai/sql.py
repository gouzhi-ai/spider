import psycopg
from psycopg.rows import dict_row
from tabulate import tabulate


def get_database_connection():
    """创建数据库连接"""
    conn_params = {
        "host": "172.16.223.100",
        "port": 35432,
        "dbname": "postgres",
        "user": "postgres",
        "password": "postgres",
        "sslmode": "disable",
        "connect_timeout": 10,
        "client_encoding": "utf8"
    }

    try:
        conn = psycopg.connect(**conn_params, row_factory=dict_row)
        return conn
    except psycopg.Error as e:
        print(f"数据库连接错误: {e}")
        raise


def create_spider_table():
    """创建spider_question_db表及其字段"""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS spider_question_db (
        question_id VARCHAR(300) PRIMARY KEY,
        question_text TEXT NOT NULL,
        answer_text TEXT,
        explanation_text TEXT,
        image_url VARCHAR(500),
        metadata JSON,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- 添加字段注释
    COMMENT ON COLUMN spider_question_db.question_id IS '问题ID';
    COMMENT ON COLUMN spider_question_db.question_text IS '问题文本';
    COMMENT ON COLUMN spider_question_db.answer_text IS '答案文本';
    COMMENT ON COLUMN spider_question_db.explanation_text IS '解释文本';
    COMMENT ON COLUMN spider_question_db.image_url IS '图片URL';
    COMMENT ON COLUMN spider_question_db.metadata IS '元数据(JSON格式)';
    COMMENT ON COLUMN spider_question_db.created_at IS '创建时间';
    COMMENT ON COLUMN spider_question_db.updated_at IS '更新时间';

    -- 创建更新时间触发器
    CREATE OR REPLACE FUNCTION update_updated_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = CURRENT_TIMESTAMP;
        RETURN NEW;
    END;
    $$ language 'plpgsql';

    -- 删除已存在的触发器（如果有）
    DROP TRIGGER IF EXISTS update_spider_question_updated_at ON spider_question_db;

    -- 创建新的触发器
    CREATE TRIGGER update_spider_question_updated_at
        BEFORE UPDATE ON spider_question_db
        FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
    """

    try:
        with get_database_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(create_table_query)
                conn.commit()
                print("表创建成功！")
    except psycopg.Error as e:
        print(f"创建表失败: {e}")
        raise


def alter_question_id_length():
    """修改 question_id 字段长度为300"""
    alter_query = """
    ALTER TABLE spider_question_db 
    ALTER COLUMN question_id TYPE VARCHAR(300);
    """

    try:
        with get_database_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(alter_query)
                conn.commit()
                print("question_id 字段长度修改成功！")
    except psycopg.Error as e:
        print(f"修改字段长度失败: {e}")
        raise


def get_spider_table_schema():
    """获取spider_question_db表的详细结构"""
    query = """
    SELECT 
        c.column_name as "列名",
        c.data_type as "数据类型",
        CASE 
            WHEN c.character_maximum_length IS NOT NULL 
            THEN c.character_maximum_length::text 
            WHEN c.numeric_precision IS NOT NULL 
            THEN c.numeric_precision::text || ',' || c.numeric_scale::text
            ELSE ''
        END as "长度/精度",
        c.is_nullable as "允许空值",
        c.column_default as "默认值",
        pg_catalog.col_description(
            format('%s.%s', c.table_schema, c.table_name)::regclass::oid,
            c.ordinal_position
        ) as "字段说明",
        CASE 
            WHEN pk.constraint_type = 'PRIMARY KEY' THEN '是'
            ELSE '否'
        END as "主键"
    FROM information_schema.columns c
    LEFT JOIN (
        SELECT ku.table_schema,
               ku.table_name,
               ku.column_name,
               tc.constraint_type
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage ku
            ON tc.constraint_name = ku.constraint_name
        WHERE tc.constraint_type = 'PRIMARY KEY'
    ) pk 
    ON c.table_schema = pk.table_schema 
    AND c.table_name = pk.table_name 
    AND c.column_name = pk.column_name
    WHERE c.table_schema = 'public' 
    AND c.table_name = 'spider_question_db'
    ORDER BY c.ordinal_position;
    """

    try:
        with get_database_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()

                if not results:
                    print("表 spider_question_db 不存在或没有字段")
                    return

                print("\n表 spider_question_db 的结构：")
                print(tabulate(results, headers="keys", tablefmt="pretty"))

                # 获取表的其他信息
                table_info_query = """
                SELECT 
                    pg_size_pretty(pg_total_relation_size('spider_question_db')) as "表大小",
                    pg_size_pretty(pg_indexes_size('spider_question_db')) as "索引大小",
                    (SELECT count(*) FROM spider_question_db) as "总行数"
                """
                cur.execute(table_info_query)
                table_info = cur.fetchone()

                print("\n表的其他信息：")
                print(f"表大小: {table_info['表大小']}")
                print(f"索引大小: {table_info['索引大小']}")
                print(f"总行数: {table_info['总行数']}")

    except psycopg.Error as e:
        print(f"查询执行错误: {e}")
        raise


if __name__ == "__main__":
    try:
        # 如果表不存在，创建表
        create_spider_table()
        # 如果表已存在，修改字段长度
        alter_question_id_length()
        # 查看表结构
        get_spider_table_schema()
    except Exception as e:
        print(f"执行出错: {e}")