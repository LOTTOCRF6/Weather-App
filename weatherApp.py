from tkinter import *
from tkinter import messagebox
import requests


root = Tk()
root.title("Weather Service")
root.geometry("600x500")
root.config(bg="spring green")

# Labels and Entry
city_lab = Label(root, text="City/Town:", bg="spring green", font=("Italic 15 bold"))
city_lab.place(x=5, y=6)
city_entry = Entry(root)
city_entry.place(x=140, y=7, width=220,)
temp_lab = Label(root, text="Temperature:", bg="spring green", font=("Italic 15 bold"))
temp_lab.place(x=5, y=50)
temp_entry = Entry(root)
temp_entry.place(x=180, y=50, width=220)
pre_lab = Label(root, text="Atmospheric pressure:", bg="spring green", font=("Italic 15 bold"))
pre_lab.place(x=5, y=90)
pre_entry = Entry(root)
pre_entry.place(x=280, y=90, width=220)
humid_lab = Label(root, text="Humidity:", bg="spring green", font=("Italic 15 bold"))
humid_lab.place(x=5, y=130)
humid_entry = Entry(root)
humid_entry.place(x=130, y=130, width=220)
descript_lab = Label(root, text="Description:", bg="spring green", font=("Italic 15 bold"))
descript_lab.place(x=5, y=170)
descript_entry = Entry(root)
descript_entry.place(x=160, y=170)


# functions

# check weather function
def check_weather():

    # API KEY
    weather_key = 'b2a0e923e0b5f768b7c6561f0f7398d2'

    # url
    url = 'https://api.openweathermap.org/data/2.5/weather'

    # City name from city text box
    city_name = city_entry.get()
    params1 = {'appid': weather_key, 'q': 'Cape Town', 'units': 'Metric'}
    response = requests.get(url, params=params1)
    weather = response.json()

    if weather['cod'] != '404':
        y = weather['main']
        current_temp = y['temp']
        current_presre = y['pressure']
        current_humid = y['humidity']
        z = weather['weather']
        weather_descript = z[0]['description']
        temp_entry.insert(15, str(current_temp) + "" + 'Degrees')
        pre_entry.insert(10, str(current_presre) + "" + 'hPa')
        humid_entry.insert(15, str(current_humid) + "" + '%')
        descript_entry.insert(10, str(weather_descript))
    else:
        messagebox.showerror('Error', 'City not found \n'
                             'Please enter a valid City')
        city_entry.delete(0, END)


# clear function
def clear():
    city_entry.delete(0, END)
    temp_entry.delete(0, END)
    pre_entry.delete(0, END)
    humid_entry.delete(0, END)
    descript_entry.delete(0, END)


# exit function
def exit_program():
    return root.destroy()


# Buttons
check_btn = Button(root, text="Check Weather", font=('Aria', 12), command=check_weather, bg="spring green")
check_btn.place(x=370, y=6)
clear_btn = Button(root, text="Clear", command=clear, bg="spring green")
clear_btn.place(x=5, y=240)
exit_btn = Button(root, text="Exit", command=exit_program, bg="spring green")
exit_btn.place(x=100, y=240)



root.mainloop()