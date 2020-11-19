from tkinter import *
import requests



def locations6():

    url = 'https://api.openweathermap.org/data/2.5/weather'
    weatherKey = '7640ca83570b1ab09a436d45fa91e40b'
    params = {"appid": weatherKey, "q": "cape town", "units": "Metric"}# have to enter the city from here next to q  still trying to figure this part out
    response = requests.get(url, params=params)
    weather = response.json()
    print(weather)
    max =weather['main']['temp_max']
    min = weather['main']['temp_min']
    humid = weather['main']['humidity']
    winds= weather['wind']['speed']



    tempent.insert(0,max)
    tempminEnt.insert(0,min)
    humidEnt.insert(0,humid)
    windEnt.insert(0,winds)






window = Tk()
window.title("Weather app")
window.config(background="light blue")
window.geometry("500x400")

# labels for the program






temp_max= Label(window, text="Maximum Temp: ").place(x=35, y=25)
tempent =Entry(window,text="")
tempent.place(x=250, y=25)

temp_min = Label(window, text="Minimum Temp:").place(x=35, y=80)
tempminEnt = Entry(window)
tempminEnt.place(x=250, y=80)


humidit = Label(window, text="Humidity:").place(x=35, y=135)
humidEnt = Entry(window)
humidEnt.place(x=250, y=135)


wind = Label(window, text="Wind Speed:").place(x=35, y=200)
windEnt = Entry(window)
windEnt.place(x=250, y=200)


Location = Label(window, text="Enter Location:").place(x=35, y=250)
LocationEnt = Entry(window).place(x=250, y=250)
LocButtn= Button(window, text="click",command=locations6).place(x=160, y=250)



















window.mainloop()
