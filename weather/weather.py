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
    print(weather["weatherinfo"]["ptime"] + "发布")
    print()

    wind_url = "http://www.weather.com.cn/data/sk/" + city_id + ".html"
    wind_data = urllib.request.urlopen(wind_url).read().decode("utf8")
    wind = json.loads(wind_data)
    print("当前实况 " + wind["weatherinfo"]["time"])
    print("当前温度：" + wind["weatherinfo"]["temp"])
    print("风向：" + wind["weatherinfo"]["WD"])
    print("风力：" + wind["weatherinfo"]["WS"])
    print("相对湿度：" + wind["weatherinfo"]["SD"])
    print()

    city_weather_url = "http://m.weather.com.cn/data/" + city_id + ".html"
    city_weather_data = urllib.request.urlopen(city_weather_url).read().decode("utf8")
    city_weather = json.loads(city_weather_data)
    weatherinfo = city_weather["weatherinfo"]
    print("城市：" + weatherinfo["city"] + weatherinfo["city_en"])
    print("日期：" + weatherinfo["date_y"] + " " + weatherinfo["week"])
    print("今日天气：" + weatherinfo["weather1"])
    print("温度：" + weatherinfo["temp1"] + ", 华氏温度：" + weatherinfo["tempF1"])
    print(weatherinfo["wind1"] + " " + weatherinfo["fl1"])
    print("穿衣指数：" + weatherinfo["index"])
    print(weatherinfo["index_d"])
    print("48小时穿衣指数：" + weatherinfo["index48"])
    print(weatherinfo["index48_d"])
    print("紫外线强度：" + weatherinfo["index_uv"])
    print("48小时紫外线强度：" + weatherinfo["index48_uv"])
    print("洗车指数：" + weatherinfo["index_xc"])
    print("旅游指数：" + weatherinfo["index_tr"])
    print("舒适指数：" + weatherinfo["index_co"])
    print("晨练指数：" + weatherinfo["index_cl"])
    print("晾晒指数：" + weatherinfo["index_ls"])
    print("过敏指数：" + weatherinfo["index_ag"])
