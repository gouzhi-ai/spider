import json
from random import choice
from random import randint
from random import random
from time import time
from typing import Union
from urllib.parse import urlencode

from gmssl import sm3, func


class ABogus:
    __end_string = "cus"
    __str = {
        "s0": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
        "s1": "Dkdpgh4ZKsQB80/Mfvw36XI1R25+WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=",
        "s2": "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=",
        "s3": "ckdp1h4ZKsUB80/Mfvw36XIgR25+WQAlEi7NLboqYTOPuzmFjJnryx9HVGDaStCe",
        "s4": "Dkdpgh2ZmsQB80/MfvV36XI1R45-WUAlEixNLwoqYTOPuzKFjJnry79HbGcaStCe",
    }

    def __init__(self, user_agent: str = "", platform: str = None):
        self.user_agent = user_agent
        self.ua_code = self.generate_ua_code(user_agent)
        self.browser = self.generate_browser_info(platform)
        self.browser_len = len(self.browser)
        self.browser_code = self.char_code_at(self.browser)

    def generate_ua_code(self, user_agent: str) -> list:
        numbers = [0.00390625, 1, 14]
        key_string = ''.join(chr(int(num)) for num in numbers)
        return self.sm3_to_array(self.generate_result(self.rc4_encrypt(user_agent, key_string), "s3"))

    def list_1(self, a=170, b=85, c=45) -> list:
        return self.random_list(a, b, 1, 2, 5, c & a)

    def list_2(self, a=170, b=85) -> list:
        return self.random_list(a, b, 1, 0, 0, 0)

    def list_3(self, a=170, b=85) -> list:
        return self.random_list(a, b, 1, 0, 5, 0)

    def random_list(self, b=170, c=85, d=0, e=0, f=0, g=0) -> list:
        r = random() * 10000
        v = [r, int(r) & 255, int(r) >> 8]
        s = v[1] & b | d
        v.append(s)
        s = v[1] & c | e
        v.append(s)
        s = v[2] & b | f
        v.append(s)
        s = v[2] & c | g
        v.append(s)
        return v[-4:]

    def from_char_code(self, *args):
        return "".join(chr(code) for code in args)

    def generate_string_1(self):
        return self.from_char_code(*self.list_1()) + self.from_char_code(
            *self.list_2()) + self.from_char_code(*self.list_3())

    def generate_string_2(self, url_params: str, method="GET") -> str:
        a = self.generate_string_2_list(url_params, method)
        e = self.end_check_num(a)
        a.extend(self.browser_code)
        a.append(e)
        return self.rc4_encrypt(self.from_char_code(*a), "y")

    def generate_string_2_list(self, url_params: str, method="GET") -> list:
        start_time = int(time() * 1000)
        end_time = start_time + randint(4, 8)
        params_array = self.generate_params_code(url_params)
        method_array = self.generate_method_code(method)
        return self.list_4(
            (end_time >> 24) & 255,
            params_array[21],
            self.ua_code[23],
            (end_time >> 16) & 255,
            params_array[22],
            self.ua_code[24],
            (end_time >> 8) & 255,
            (end_time >> 0) & 255,
            (start_time >> 24) & 255,
            (start_time >> 16) & 255,
            (start_time >> 8) & 255,
            (start_time >> 0) & 255,
            method_array[21],
            method_array[22],
            int(end_time / 256 / 256 / 256 / 256) >> 0,
            int(start_time / 256 / 256 / 256 / 256) >> 0,
            self.browser_len,
        )

    def list_4(self,
               a: int,
               b: int,
               c: int,
               d: int,
               e: int,
               f: int,
               g: int,
               h: int,
               i: int,
               j: int,
               k: int,
               m: int,
               n: int,
               o: int,
               p: int,
               q: int,
               r: int,
               ) -> list:
        return [
            44,
            a,
            0,
            0,
            0,
            0,
            24,
            b,
            n,
            0,
            c,
            d,
            0,
            0,
            0,
            1,
            0,
            239,
            e,
            o,
            f,
            g,
            0,
            0,
            0,
            0,
            h,
            0,
            0,
            14,
            i,
            j,
            0,
            k,
            m,
            3,
            p,
            1,
            q,
            1,
            r,
            0,
            0,
            0]

    def end_check_num(self, a: list):
        r = 0
        for i in a:
            r ^= i
        return r

    def convert_to_char_code(self, a):
        d = []
        for i in a:
            d.append(ord(i))
        return d

    def split_array(self, arr, chunk_size=64):
        result = []
        for i in range(0, len(arr), chunk_size):
            result.append(arr[i:i + chunk_size])
        return result

    def char_code_at(self, s):
        return [ord(char) for char in s]

    def generate_result(self, s, e="s4"):
        r = []

        for i in range(0, len(s), 3):
            if i + 2 < len(s):
                n = (
                        (ord(s[i]) << 16)
                        | (ord(s[i + 1]) << 8)
                        | ord(s[i + 2])
                )
            elif i + 1 < len(s):
                n = (ord(s[i]) << 16) | (
                        ord(s[i + 1]) << 8
                )
            else:
                n = ord(s[i]) << 16

            for j, k in zip(range(18, -1, -6), (0xFC0000, 0x03F000, 0x0FC0, 0x3F)):
                if j == 6 and i + 1 >= len(s):
                    break
                if j == 0 and i + 2 >= len(s):
                    break
                r.append(self.__str[e][(n & k) >> j])

        r.append("=" * ((4 - len(r) % 4) % 4))
        return "".join(r)

    def generate_method_code(self, method: str = "GET") -> list[int]:
        return self.sm3_to_array(self.sm3_to_array(method + self.__end_string))

    def generate_params_code(self, params: str) -> list[int]:
        return self.sm3_to_array(self.sm3_to_array(params + self.__end_string))

    def sm3_to_array(self, data: Union[str, list]) -> list[int]:
        if isinstance(data, str):
            b = data.encode("utf-8")
        else:
            b = bytes(data)  # 将 List[int] 转换为字节数组

        # 将字节数组转换为适合 sm3.sm3_hash 函数处理的列表格式
        h = sm3.sm3_hash(func.bytes_to_list(b))

        # 将十六进制字符串结果转换为十进制整数列表
        return [int(h[i: i + 2], 16) for i in range(0, len(h), 2)]

    def generate_browser_info(self, platform: str = "Win32") -> str:
        inner_width = randint(1280, 1920)
        inner_height = randint(720, 1080)
        outer_width = randint(inner_width, 1920)
        outer_height = randint(inner_height, 1080)
        screen_x = 0
        screen_y = choice((0, 30))
        value_list = [
            inner_width,
            inner_height,
            outer_width,
            outer_height,
            screen_x,
            screen_y,
            0,
            0,
            outer_width,
            outer_height,
            outer_width,
            outer_height,
            inner_width,
            inner_height,
            24,
            24,
            platform,
        ]
        return "|".join(str(i) for i in value_list)

    def rc4_encrypt(self, plaintext, key):
        s = list(range(256))
        j = 0

        for i in range(256):
            j = (j + s[i] + ord(key[i % len(key)])) % 256
            s[i], s[j] = s[j], s[i]

        i = 0
        j = 0
        cipher = []

        for k in range(len(plaintext)):
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            t = (s[i] + s[j]) % 256
            cipher.append(chr(s[t] ^ ord(plaintext[k])))

        return ''.join(cipher)

    def generate_a_bogus(self, url_params: Union[dict, str]) -> str:
        string_1 = self.generate_string_1()
        string_2 = self.generate_string_2(urlencode(url_params))
        string = string_1 + string_2
        return self.generate_result(string, "s4")


if __name__ == "__main__":
    import requests


    url = "https://www.douyin.com/aweme/v1/web/comment/list/"

    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        'Cookie': "ttwid=1%7CBtgMVexTRal-XY5PajkmZ4qq1VSN_xmmNhacROwxnNs%7C1733217333%7C0cbb98fd5c5e07f176c80b967ec84c2a923144473eeeac8a302149bd6e561176; UIFID_TEMP=a6000b6bd0597977c28c1dbb751d8a8c80ef4c078dbea6da280536e6f6924b828cc5212fb0fc8cadaaad1f38010ec3f8fe599a2ffd5e732d191e637b64bd2d0360670224bb5c6b16c678708817c07dc7; s_v_web_id=verify_m488upm7_p8Oa9sXZ_TlPy_4389_A1hN_Uq3paUPxcZvW; dy_swidth=1920; dy_sheight=1080; hevc_supported=true; xgplayer_user_id=743528818429; fpk1=U2FsdGVkX1+uEio1TSQp5Um78KlRFmNiwL3ec0bwZ0m7eClQpFMzPKbeTvoJDIjeQzzHVsfzV7EsMjojJR42jQ==; fpk2=c28c178f7fc01e92a5161b6c80153add; passport_csrf_token=b4e73ce3deb545a51ffd9e9c0a919e5e; passport_csrf_token_default=b4e73ce3deb545a51ffd9e9c0a919e5e; odin_tt=4c2a490c8472e057951f781aa15849c3063ce16b20657d02e0cf74c7884dd4ed56f4e1f11f4db2e43fd0ae3c24c2f92a170851f1e7b61603aa0e78feea56d887f76e695b97fbc8c4f3d5fc74c0a3644f; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; bd_ticket_guard_client_web_domain=2; is_dash_user=1; UIFID=a6000b6bd0597977c28c1dbb751d8a8c80ef4c078dbea6da280536e6f6924b828cc5212fb0fc8cadaaad1f38010ec3f8b04dd17b9fff3931487fd386d7a5c1acc81c1754bc4ccfa93ab88ae072e97c1381e906c08c9f9f859bbc94e9c3038c3272b4b531c2c761d4711ef6b0bcb026ceebb81abc35a24e31e500180e43d109b782a3b2e40a716bee23d5e32a6612757d9f3805b0cdc63b015f19a9c9a976bc64; WallpaperGuide=%7B%22showTime%22%3A1733217639264%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A10%2C%22cursor2%22%3A2%7D; douyin.com; xg_device_score=7.463851802933686; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A200%7D%22; strategyABtestKey=%221733305816.681%22; home_can_add_dy_2_desktop=%221%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; csrf_session_id=122d715e1dcf541c05ae7d190dec72f7; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUGYwLzZleFFZMHo1SENnRnNZczl4akl4b3I3VHFkRHA2UW9sMWtzVGM1dVZvRlBXNlFzN1NrU1hENTQzM3FjS216cmoxd0hCN2hDT1dQdllUajdaWkE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; biz_trace_id=ea4a32d7; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e5827292771273f2736343435373d303536363632342778; bit_env=z0IE4X6z2picEWUGvieZCJ4ZPWBW-Fin_RXhg3solk1Bti0f14lo5aH4-iwtTh8MssJhGb_yrUTPYsazhdORE55_1wkxkr62tYWZcJKgyfqwkaP5dlQ8-6vIdKiHqtlh6-McPFlHAjW7oQWLSoSvZYoFm4-YHq-C_JG4BgjNfa-5c3e5K5hwWbRSp-QaMwwL-ibeYZ1tASxdl4CbbtUiUGSUUfgiRz6OFTeFgWN7IC4PuL3w0W_puiEdfKCdxzkq_VDOnZo6NQvvK8_IvRln7uGSqJ-4DiqpgHd-SwWK78BVH0v6xv5KxyZy6j0KrgfpA5ghxh-GDAuKNDzfUkEjwCP6piXmGOTC8gXS64jP32PSb3i1_3i5CGoW7x8qmPxpblwBUIXfrL0k7KYUA87N1_iJk73SR6fRqh614Xk5safxCLvdBxt5oNABugkiehLmjoJ-5nU0OUFo5-igGqrlla467CYSqUICPUzwKTHb5D7RzK81Yv0Beld5SP8CtZJl-60IksjP3-lVwZgcYMLKHNX40QHXY_OI8SQri8u_zaU%3D; gulu_source_res=eyJwX2luIjoiMTJlYzU4ZjUyYmU1YzJjYWQ5NTJlMDMwMjQxYzhkNzE3NTFhZDM1ZWZiYTVlNjU3MzVhMmU2OGEyMGU2YTc0OSJ9; passport_auth_mix_state=9xi7l82gps7ep5dbthqro63nckzug7lw; download_guide=%223%2F20241204%2F0%22"
    }

    params = {
        "aweme_id": "7394759586336623899",
        "cursor": "40",
        "count": "20",
    }


    bogus = ABogus(headers['user-agent'])

    a_bogus = bogus.generate_a_bogus(params)
    print(a_bogus)

    params['a_bogus'] = a_bogus
    response = requests.get(url, params=params, headers=headers)

    print(response.status_code)
    print(response.text)
    #
    # url = "https://www.douyin.com/aweme/v1/web/comment/list/"
    #
    # headers = {
    #     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    #     'Cookie': "ttwid=1%7CBtgMVexTRal-XY5PajkmZ4qq1VSN_xmmNhacROwxnNs%7C1733217333%7C0cbb98fd5c5e07f176c80b967ec84c2a923144473eeeac8a302149bd6e561176; UIFID_TEMP=a6000b6bd0597977c28c1dbb751d8a8c80ef4c078dbea6da280536e6f6924b828cc5212fb0fc8cadaaad1f38010ec3f8fe599a2ffd5e732d191e637b64bd2d0360670224bb5c6b16c678708817c07dc7; s_v_web_id=verify_m488upm7_p8Oa9sXZ_TlPy_4389_A1hN_Uq3paUPxcZvW; dy_swidth=1920; dy_sheight=1080; hevc_supported=true; xgplayer_user_id=743528818429; fpk1=U2FsdGVkX1+uEio1TSQp5Um78KlRFmNiwL3ec0bwZ0m7eClQpFMzPKbeTvoJDIjeQzzHVsfzV7EsMjojJR42jQ==; fpk2=c28c178f7fc01e92a5161b6c80153add; passport_csrf_token=b4e73ce3deb545a51ffd9e9c0a919e5e; passport_csrf_token_default=b4e73ce3deb545a51ffd9e9c0a919e5e; odin_tt=4c2a490c8472e057951f781aa15849c3063ce16b20657d02e0cf74c7884dd4ed56f4e1f11f4db2e43fd0ae3c24c2f92a170851f1e7b61603aa0e78feea56d887f76e695b97fbc8c4f3d5fc74c0a3644f; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; bd_ticket_guard_client_web_domain=2; is_dash_user=1; UIFID=a6000b6bd0597977c28c1dbb751d8a8c80ef4c078dbea6da280536e6f6924b828cc5212fb0fc8cadaaad1f38010ec3f8b04dd17b9fff3931487fd386d7a5c1acc81c1754bc4ccfa93ab88ae072e97c1381e906c08c9f9f859bbc94e9c3038c3272b4b531c2c761d4711ef6b0bcb026ceebb81abc35a24e31e500180e43d109b782a3b2e40a716bee23d5e32a6612757d9f3805b0cdc63b015f19a9c9a976bc64; WallpaperGuide=%7B%22showTime%22%3A1733217639264%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A10%2C%22cursor2%22%3A2%7D; douyin.com; xg_device_score=7.463851802933686; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A200%7D%22; strategyABtestKey=%221733305816.681%22; home_can_add_dy_2_desktop=%221%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; csrf_session_id=122d715e1dcf541c05ae7d190dec72f7; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUGYwLzZleFFZMHo1SENnRnNZczl4akl4b3I3VHFkRHA2UW9sMWtzVGM1dVZvRlBXNlFzN1NrU1hENTQzM3FjS216cmoxd0hCN2hDT1dQdllUajdaWkE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; biz_trace_id=ea4a32d7; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e5827292771273f2736343435373d303536363632342778; bit_env=z0IE4X6z2picEWUGvieZCJ4ZPWBW-Fin_RXhg3solk1Bti0f14lo5aH4-iwtTh8MssJhGb_yrUTPYsazhdORE55_1wkxkr62tYWZcJKgyfqwkaP5dlQ8-6vIdKiHqtlh6-McPFlHAjW7oQWLSoSvZYoFm4-YHq-C_JG4BgjNfa-5c3e5K5hwWbRSp-QaMwwL-ibeYZ1tASxdl4CbbtUiUGSUUfgiRz6OFTeFgWN7IC4PuL3w0W_puiEdfKCdxzkq_VDOnZo6NQvvK8_IvRln7uGSqJ-4DiqpgHd-SwWK78BVH0v6xv5KxyZy6j0KrgfpA5ghxh-GDAuKNDzfUkEjwCP6piXmGOTC8gXS64jP32PSb3i1_3i5CGoW7x8qmPxpblwBUIXfrL0k7KYUA87N1_iJk73SR6fRqh614Xk5safxCLvdBxt5oNABugkiehLmjoJ-5nU0OUFo5-igGqrlla467CYSqUICPUzwKTHb5D7RzK81Yv0Beld5SP8CtZJl-60IksjP3-lVwZgcYMLKHNX40QHXY_OI8SQri8u_zaU%3D; gulu_source_res=eyJwX2luIjoiMTJlYzU4ZjUyYmU1YzJjYWQ5NTJlMDMwMjQxYzhkNzE3NTFhZDM1ZWZiYTVlNjU3MzVhMmU2OGEyMGU2YTc0OSJ9; passport_auth_mix_state=9xi7l82gps7ep5dbthqro63nckzug7lw; download_guide=%223%2F20241204%2F0%22"
    # }
    #
    # params = {
    #     "aweme_id": "7394759586336623899",
    #     "cursor": "40",
    #     "count": "20",
    # }
    #
    #
    # bogus = ABogus(headers['user-agent'])
    #
    # a_bogus = bogus.generate_a_bogus(params)
    # print(a_bogus)
    #
    # params['a_bogus'] = a_bogus
    # response = requests.get(url, params=params, headers=headers)
    #
    # print(response.status_code)
    # print(response.text)


    user_agent_11 = "Mozilla/5.0"
    print(bogus.generate_ua_code(user_agent_11))