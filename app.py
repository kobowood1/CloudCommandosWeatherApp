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
        # json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15) # change from Kelvin to Celsius
        min_temp = int(json_data['main']['temp_min'] - 273.15)  # change from Kelvin to Celsius
        max_temp = int(json_data['main']['temp_max'] - 273.15) # change from Kelvin to Celsius
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise']))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset']))

        # Prepare the weather information to display
        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
        
        # Update the label widgets with the weather information
        label1.config(text = final_info)
        label2.config(text = final_data)
    
        # Display an error message if an exception occurs during weather retrieval
    except Exception as e: 
        label1.config(text = "OOPS!")
        label2.config(text = "No city found")

# Create the main application window
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Cloud Commando Weather App")

# Font styles for the text
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# Create text entry field for city input
textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 30)
textField.focus()
textField.bind('<Return>', getWeather)

# Create labels for displaying weather information
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

# Start the Tkinter event loop
canvas.mainloop()
