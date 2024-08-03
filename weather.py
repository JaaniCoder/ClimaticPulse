import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = '052705f1cdd45406b4b930d95da02ada'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    try:
        response = requests.get(BASE_URL, params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        })
        data = response.json()
        if data['cod'] == 200:
            weather_info = {
                'City': data['name'],
                'Temperature': f"{data['main']['temp']}°C",
                'Weather': data['weather'][0]['description'].capitalize(),
                'Humidity': f"{data['main']['humidity']}%",
                'Wind Speed': f"{data['wind']['speed']} m/s"
            }
            return weather_info
        else:
            return None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None
    
def display_weather():
    city = city_entry.get()
    if city:
        weather_info = fetch_weather(city)
        if weather_info:
            result = "\n".join([f"{key}: {value}" for key, value in weather_info.items()])
            label.config(text=result)
        else:
            label.config(text="City not found or API error.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")


app = tk.Tk()
app.title("ClimaticPulse")

app.geometry('400x400')
app.resizable(False, False)
app.configure(bg='#f0f8ff')

frame = tk.Frame(app, bg='#87ceeb', padx=20, pady=20)
frame.pack(padx=10, pady=10,expand=True)

title = tk.Label(frame, text="ClimaticPulse", font=('Helvetica', 18, 'bold'), bg='#87ceeb', fg='#fff')
title.pack(pady=(0, 20))

city_entry = tk.Entry(frame, font=('Helvetica, 14'), width=20)
city_entry.pack(pady=(0, 10))

button = tk.Button(frame, text='Get Weather Details', command=display_weather, font=('Helvetica', 14, 'bold'), bg='#4682b4', fg='#fff', relief='raised')
button.pack(pady=(0, 20))

label = tk.Label(app, text="", font=('Helevetica', 12), justify='left')
label.pack(pady=10)

app.mainloop()