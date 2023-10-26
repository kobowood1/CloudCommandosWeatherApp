# Import necessary libraries
import tkinter as tk # Tkinter library for GUI
import requests # Requests library for making HTTP requests
import time # Time library for manipulating time data

 
# Function to retrieve weather information
def getWeather(canvas):
    try: 
        # Get the city name from the text entry field
        city = textField.get()

        # API endpoint for weather data
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9036b0259df683d94625d841023d526f"
        
        # Send HTTP GET request to the API and retrieve JSON response
        json_data = requests.get(api).json()
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
        label1.config(text = final_info)
        label2.config(text = final_data)
    except Exception as e: 
        label2.config(text = "No city found")

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Cloud Commando Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 30)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()