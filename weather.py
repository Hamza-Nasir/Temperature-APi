import json
import requests

# def give_weather(city,country,url):
#     weather=requests.get(url)
#     weather.status_code

print("Enter you City Name: ")
city = input()

# print("Enter the country in which City is located: ")
# country = input()

key = "dcaf0d7f17e32a1e0167316d3b5cdbda"

url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

x = requests.get(url)

if (x == 200):
    y = x.json()

    z = y["main"]

    current_weather = z["temp"]

    t = current_weather - 273

    print(f"Current temperature in Centigrade: {t}")

else:
    print("Invalid entry!")

