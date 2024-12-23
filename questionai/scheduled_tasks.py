from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone
from questionai.question_ai_apis2 import scheduler_task_pre
import time
# 定义要执行的函数
def a():
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print("Formatted current time:", formatted_time)
    scheduler_task_pre()
    # print(1)
# 创建调度器
scheduler = BlockingScheduler()

# 添加任务
# 使用 CronTrigger 设置北京时间（Asia/Shanghai）每天上午10点执行
scheduler.add_job(
    func=a,
    trigger=CronTrigger(
        hour=9,
        minute=10,
        timezone=timezone('Asia/Shanghai')
    ),
    args=[]  # 这里传入函数 a 的参数
)

if __name__ == '__main__':
    try:
        print('定时任务已启动...')
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
