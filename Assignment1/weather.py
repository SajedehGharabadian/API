import requests
import json
from PySide6.QtWidgets import QApplication,QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap


# 
# print(response.status_code)
def weather():
    city_name = window.line_Edit.text()
    response = requests.get("https://goweather.herokuapp.com/weather/"+str(city_name))
    print(response.status_code)
    window.label_day1.setText("Day 1")
    window.label_day2.setText("Day 2")
    window.label_day3.setText("Day 3")
    window.textEdit.setStyleSheet("border: 5px solid black;")
    window.textEdit_2.setStyleSheet("border: 5px solid black;")
    window.textEdit_3.setStyleSheet("border: 5px solid black;")
    if response.status_code == 200:
        weather_city = json.loads(response.text)
        print(weather_city['description'])
        
        if weather_city['description'] == 'Partly cloudy':
            window.label_des.setText(str(weather_city['description']))
            window.label_temp.setText("Temperature: "+str(weather_city['temperature']))
            window.label_wind.setText("Wind: "+str(weather_city['wind']))
            image = QPixmap("images/cloudy_day.png").scaled(150,150)
            window.label_img.setPixmap(image)
            window.label_temp_day2.setText("Temperature: "+str(weather_city['forecast'][1]['temperature']))
            window.label_wind_day2.setText("Wind: "+str(weather_city['forecast'][1]['wind']))
            window.label_temp_day3.setText("Temperature: "+str(weather_city['forecast'][2]['temperature']))
            window.label_wind_day3.setText("Wind: "+str(weather_city['forecast'][2]['wind']))


        elif weather == "Thunderstorm":
            window.label_des.setText(str(weather_city['description']))
            window.label_temp.setText(str(weather_city['temperature']))
            window.label_wind.setText(str(weather_city['wind']))
            image = QPixmap("images/cloud_day_light bolt.png").scaled(150,150)
            window.label_img.setPixmap(image)
            window.label_temp_day2.setText("Temperature: "+str(weather_city['forecast'][1]['temperature']))
            window.label_wind_day2.setText("Wind: "+str(weather_city['forecast'][1]['wind']))
            window.label_temp_day3.setText("Temperature: "+str(weather_city['forecast'][2]['temperature']))
            window.label_wind_day3.setText("Wind: "+str(weather_city['forecast'][2]['wind']))


        elif weather == "Clear":
            window.label_des.setText(str(weather_city['description']))
            window.label_temp.setText(str(weather_city['temperature']))
            window.label_wind.setText(str(weather_city['wind']))
            image = QPixmap("images/sun_sunny.png").scaled(150,150)
            window.label_img.setPixmap(image)
            window.label_temp_day2.setText("Temperature: "+str(weather_city['forecast'][1]['temperature']))
            window.label_wind_day2.setText("Wind: "+str(weather_city['forecast'][1]['wind']))
            window.label_temp_day3.setText("Temperature: "+str(weather_city['forecast'][2]['temperature']))
            window.label_wind_day3.setText("Wind: "+str(weather_city['forecast'][2]['wind']))


        elif weather == "Light rain":
            window.label_des.setText(str(weather_city['description']))
            window.label_temp.setText(str(weather_city['temperature']))
            window.label_wind.setText(str(weather_city['wind']))
            image = QPixmap("images/light_rain_.png").scaled(150,150)
            window.label_img.setPixmap(image)
            window.label_temp_day2.setText("Temperature: "+str(weather_city['forecast'][1]['temperature']))
            window.label_wind_day2.setText("Wind: "+str(weather_city['forecast'][1]['wind']))
            window.label_temp_day3.setText("Temperature: "+str(weather_city['forecast'][2]['temperature']))
            window.label_wind_day3.setText("Wind: "+str(weather_city['forecast'][2]['wind']))



my_app = QApplication([])

loader = QUiLoader()
window = loader.load('main_window.ui')
window.select_btn.clicked.connect(weather)

window.show()
my_app.exec()