import tkinter as tk
import requests
from tkinter import font
from PIL import Image, ImageTk

HEIGHT = 700
WIDTH = 800

# def test_function(entry):
#     print('this is the entry: ', entry)

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_string = 'City: %s \nConditions: %s \nTemperature(C) %s' % (name, description, temp)
    except:
        final_string = 'Problem Retrieving Information'

    return final_string

def get_weather(city):
    weather_key = 'f5acd6757c7648de980e211f4181bd20'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params = parameters)#must use "params" keyword
    #print(response)
    weather = response.json()

    label['text'] = format_response(weather)




root = tk.Tk()#root window to place everything into

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)#for setting initial window size
canvas.pack()

background_image = tk.PhotoImage(file='sky.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)


#URL
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}


#organize widgets on screen
frame = tk.Frame(root, bg='#6699ff',bd=5)#bd=border
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=('Arial',18))
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text="Get Weather",font=('Arial', 18), command=lambda: get_weather(entry.get()))#place button in root window
button.place(relx=0.7,relheight=1,relwidth=0.3)#place button on the screen


lower_frame = tk.Frame(root, bg='#6699ff',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame, font=('Arial', 18), anchor='nw',justify='left',bd=4)
label.place(relwidth=1,relheight=1)

#print(tk.font.families())


#use pack to organize
'''pack has expand, fill, and side optional arguments to help in organization'''
#use grid to organize
'''grid, give a row and column to organize within a matrix/grid'''
#use place to organize
''''''



root.mainloop()# to run application (constantly)


