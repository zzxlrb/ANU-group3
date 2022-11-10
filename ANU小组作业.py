# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:47:05 2022

@author: 23225
"""
import tkinter as tk
import requests
from datetime import datetime

class Page_1: 
    def __init__(self, window):
        self.window = window
        self.window.title("p1")
        self.window.geometry("200x200")
        self.window.config(bg="gray")
        first_label = tk.Label(root, text='USER NAME:', fg='black',bg='gray',font=('Times',8))
        first_label.pack(pady=1)
        test_field = tk.Text(root, width=24, height=1)
        test_field.pack(pady=2)
        first_label = tk.Label(root, text='PASSWORD:', fg='Black',bg='gray',font=('Times',9))
        first_label.pack(pady=4)
        test_field = tk.Text(root, width=24, height=1)
        test_field.pack(pady=2)
        button = tk.Button(self.window, text="跳转", command=self.change)
        button.pack(side = tk.BOTTOM)
 
    def change(self):
       Page_2(root)
class Page_2:  
    def __init__(self, window):
        def time_format_for_location(utc_with_tz):
            local_time = datetime.utcfromtimestamp(utc_with_tz)
            return local_time.time()

        def getWeather():
            import tkinter as tk
            import requests
            from datetime import datetime
            api = 'a19f0ddc1574fd7839c2ef5b50924d4e'
            
            location = city_value.get()
            
            part = None
            weather_url = f'http://api.openweathermap.org/data/2.5/weather?q=location&appid=b0ee83e54a7746062916a80a9e32193a&units=metric'
            response = requests.get(weather_url)
            
            weather_info = response.json()
            
            temp = int(weather_info['main']['temp'])                                    
            feels_like_temp = int(weather_info['main']['feels_like'])
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            wind_speed = weather_info['wind']['speed'] * 3.6
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']
             
            sunrise_time = time_format_for_location(sunrise + timezone)
            sunset_time = time_format_for_location(sunset + timezone)
        
            weather = f"\nWeather of: {location}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
            if feels_like_temp>=14 :
                moderation="today is warm";
            else:
                moderation="today is cold"
            if cloudy>30:
                    forecast="Today the UV light is not strong, you can travel at will";
            else:
                    forecast="Sunscreen is recommended"
            if humidity>=80 and feels_like_temp>=14:
                    sport="It's a good day for outdoor sports!";
            else:
                    sport="enjoy the warmth of your family at home!"
            
            test_field.insert(tk.INSERT,weather )
            test_2.insert(tk.INSERT,moderation)
            test_3.insert(tk.INSERT,forecast)
            test_4.insert(tk.INSERT,sport)
            
        def clear():
            test_field.delete('1.0',tk.END)
            test_2.insert('1.0',tk.END)
            test_3.insert('1.0',tk.END)
            test_4.insert('1.0',tk.END)
        second = tk.Tk()
        second.title('Weather App')
        second.geometry('400x400')


        first_label = tk.Label(second, text='Location', fg='Green',bg='Red',font=('Times',16))
        first_label.pack(pady=20)

        city_value = tk.StringVar()
        location_to_search = tk.Entry(second, textvariable=city_value, width=24,font=('Times',16))
        location_to_search.pack()


        search_button = tk.Button(second, command = getWeather, text='Search', font=('Times', 16))
        search_button.pack(pady=10)

        clear_button = tk.Button(second, command = clear, text='Clear', font=('Times', 16))
        clear_button.pack(pady=10, side = tk.RIGHT)

        second_label = tk.Label(second, text='Weather Information', fg='Green',bg='Red',font=('Times',16))
        second_label.pack(pady=10)

        test_field = tk.Text(second, width=46, height=10)
        test_field.pack()
        
        test_2 = tk.Text(second, width=15, height=1)
        test_2.pack()
        
        test_3 = tk.Text(second, width=30, height=1)
        test_3.pack()
       
        test_4 = tk.Text(second, width=50, height=1)
        test_4.pack()

        second.mainloop()



root = tk.Tk()
p1 = Page_1(root) 
root.mainloop()
