#!/usr/bin/env python3
#
# 查询一个城市的天气状况。
# Inquiry the weather of city.
import urllib.request
import json
import city
import sys

if __name__ == "__main__":
    city_name = input("你想查询哪个城市的天气？\n")
    try:
        city_id = city.city[city_name];
    except KeyError:
        print("输入的城市不存在")
        sys.exit()
    weather_url = "http://www.weather.com.cn/data/cityinfo/" + city_id + ".html"
    weather_data = urllib.request.urlopen(weather_url).read().decode("utf8")
    weather = json.loads(weather_data)
    print(weather["weatherinfo"]["weather"])
    print(weather["weatherinfo"]["temp2"] + " ~ " +  weather["weatherinfo"]["temp1"])
