import tkinter as tk
from configparser import ConfigParser
from re import S
from tkinter import Label, messagebox, W, E, N
import json
import datetime


from PIL import ImageTk, Image


import requests


def weather_search(city, countrycode):
    result = requests.get(url_API.format(city, countrycode, api_ke))

    if result:
        json_file = result.json()  ## API url uses Json to store the content, this json() function will get result from the json content

        city = json_file['name']  ## use to get the city name
        country = json_file['sys']['country']  ## use to get the country name from the json content in the uRL
        weather_l = json_file['weather'][0][
            'main']  ## use to get the weather from the json content like its cloudy, foggy
        kelvin_temp = json_file['main']['temp']

        c_temp = kelvin_temp - 273.15
        f_temp = (kelvin_temp - 273.15) * 9 / 5 + 32
        Humidity =  json_file['main']['humidity']
        feels_like_K = json_file['main']['feels_like']
        feelslike_c = feels_like_K - 273.15
        wind_speed = json_file['wind']['speed']

        output = [city, country, c_temp, f_temp,weather_l, Humidity, feelslike_c, wind_speed]  ## varrieble to store the resutls of the above

        return output


def print_weather():
    ci = Search_city.get()  ## varriable to store the city that user inputs
    ci2= Search_countrycode.get()

    x = weather_search(ci, ci2) ## sends the city name to  the weather search function to get all the data

    if x:

        location_label['text'] = 'Location: {}, {}'.format(x[0], x[1]) ## it use location as an array where text is the index and then x is also used as an array whihc stores the all the data from the search function

        temperaature_Label['text'] = 'Temperature: {:.2f} c, {:.2f} F'.format(x[2], x[3])
        weather_lable['text'] = 'Weather:{}'.format(x[4])
        Humidity_label['text'] = 'Humidity: {}'.format(x[5])

        feelslike_label['text'] = 'Feels like: {:.2f} c'.format(x[6])
        windspeed_label['text'] = 'Wind speed: {}'.format(x[7])

    else :

        messagebox.showeeror('Error', 'Its not a valid city name, Please enter the city name again')


window = tk.Tk()
window.geometry('850x900')
window.config(bg='dark grey')



Search_city = tk.StringVar()
Search_countrycode = tk.StringVar()

test = tk.Label(window, text="Enter the city name: ", bg= 'dark grey', fg="black", font=("Arial", 20, "bold"), width=20)

test.grid(row=1, column=0, ipady=15)


c = tk.Entry(window, textvariable=Search_city, fg="blue", font=("Arial", 20, "bold"), width=20)
c.grid(row=1, column=1)

test2= tk.Label(window, text="Enter the country code: ", bg= 'dark grey', fg="black", font=("Arial", 20, "bold"), width=20)
test2.grid(row=2, column=0, ipady=15)

c1 = tk.Entry(window, textvariable=Search_countrycode, fg="blue", font=("Arial", 20, "bold"), width=20)
c1.grid(row=2, column=1)




##city_entry = tk.Entry(window, textvariable=Search_city, width=45)


Search_button = tk.Button(window, text='Search Weather !', bg='grey', fg='blue', font=("Arial", 20, "bold"), command=print_weather)
Search_button.place(x=200, y= 170)

dt = datetime.datetime.now()
date = Label(window, text=dt.strftime('Date and Time : %A, %m/%d/%Y, %H:%M:%S'), bg='dark grey', font=("bold", 15))
date.place(x=200, y=240)
#month = Label(window, text=dt.strftime('%m/%d/%Y, %H:%M:%S'), bg='dark grey', font=("bold", 15))
#month.place(x=300, y=140)

if int((dt.strftime('%I'))) >= 8 & int((dt.strftime('%I'))) <= 5:
    print(dt.strftime('%I'))
    img = ImageTk.PhotoImage(Image.open('moon.png'))
    panel = Label(window, image=img)
    panel.place(x=200, y=300)
else:
    img = ImageTk.PhotoImage(Image.open('sun.png'))
    panel = Label(window, image=img)
    panel.place(x=200, y=300)

location_label = tk.Label(window, text="Location: ", fg="black", font=("Arial", 20), bg="white")
location_label.place(x=200, y=510)


temperaature_Label = tk.Label(window, text="Temperature: ", fg="black", font=("Arial", 20), bg="white")
temperaature_Label.place(x=200, y=550)


weather_lable = tk.Label(window, text="Weather", fg="black", font=("Arial", 20), bg="white")
weather_lable.place(x=200, y=590)

Humidity_label = tk.Label(window, text="Humidity: ", fg="black", font=("Arial", 20), bg="white")
Humidity_label.place(x=200 , y=630)

feelslike_label = tk.Label(window, text="Feels like: ", fg="black", font=("Arial", 20), bg="white")
feelslike_label.place(x=200 , y=670)

windspeed_label = tk.Label(window, text="Wind Speed: ", fg="black", font=("Arial", 20), bg="white")
windspeed_label.place(x=200 , y=710)






url_API = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'

config_file = "key"
config = ConfigParser()
config.read(config_file)
api_ke = config['api_key']['key']

window.title("Weather App")

window.mainloop()
