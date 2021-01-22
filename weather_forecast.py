import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date
from datetime import datetime
from weather_mail import send_email

api_key = "b311a159baf1b28bea868fd152afcbb5"
position = [300, 430, 560, 690, 820]

city_list = ["London",
             "Vero Beach",
             "Boston",
             "Kitzbuhel",
             "Aspen"]
uk_list = ["London", "Manchester", "Glasgow", "Birmingham", "Newcastle"]
us_list = ["New York", "Washington D.C.", "Vero Beach", "Aspen", "San Francisco"]
big_list = [city_list]

for section in big_list:
    img = Image.open("post.png")
    draw = ImageDraw.Draw(img)

    # Writing the title
    font = ImageFont.truetype("Inter.ttf", size=50)
    if section == uk_list:
        content = "Latest UK Weather Forecast"
    elif section == us_list:
        content = "Latest US Weather Forecast"
    elif section == city_list:
        content = "Latest Weather Forecast"
    colour = "rgb(255,255,255)"
    (x, y) = (55, 50)
    draw.text((x, y), content, colour, font=font)

    # Writing the date
    font = ImageFont.truetype("Inter.ttf", size=30)
    content = date.today().strftime("%A %B %dth, %Y at ") + datetime.now().strftime("%H:%M")
    colour = "rgb(255,255,255)"
    (x, y) = (55, 145)
    draw.text((x, y), content, colour, font=font)

    index = 0
    for city in section:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=b311a159baf1b28bea868fd152afcbb5&units=metric".format(
            city)
        response = requests.get(url)
        data = json.loads(response.text)

        # Writing city name
        font = ImageFont.truetype("Inter.ttf", size=50)
        colour = "rgb(0,0,0)"
        (x, y) = (135, position[index])
        draw.text((x, y), city, colour, font=font)

        # Writing High Temperature
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(round(data["main"]["temp_max"], 1))
        colour = "rgb(255,255,255)"
        (x, y) = (600, position[index])
        draw.text((x, y), content, colour, font=font)

        # Writing Low Temperature
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(round(data["main"]["temp_min"], 1))
        colour = "rgb(255,255,255)"
        (x, y) = (735, position[index])
        draw.text((x, y), content, colour, font=font)

        # Writing Conditions
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data["weather"][0]["main"])
        colour = "rgb(255,255,255)"
        (x, y) = (860, position[index])
        draw.text((x, y), content, colour, font=font)

        index += 1

    if section == uk_list:
        img.save(str("UK Weather Forecast on ") + date.today().strftime("%A %B %dth, %Y at ") + datetime.now().strftime(
            "%H:%M") + (".png"))
        img_pdf = img.convert("RGB")
        img_pdf.save(str("UK Weather Forecast on ") + date.today().strftime("%A %B %dth, %Y at ") + datetime.now().strftime(
            "%H:%M") + (".pdf"))
    elif section == us_list:
        img.save(str("US Weather Forecast on ") + date.today().strftime("%A %B %dth, %Y at ") + datetime.now().strftime(
            "%H:%M") + (".png"))
        img_pdf = img.convert("RGB")
        img_pdf.save(str("US Weather Forecast on ") + date.today().strftime("%A %B %dth, %Y at ") + datetime.now().strftime(
            "%H:%M") + (".pdf"))
    elif section == city_list:
        # img_jpg = img.convert("RGB")
        # img_jpg.save(str("Weather Forecast on ") + date.today().strftime("%A %B %dth, %Y at ") + datetime.now().strftime(
        #     "%H%M") + (".jpg"))
        # img_pdf = img.convert("RGB")
        # img_pdf.save(str("Weather Forecast on ") + date.today().strftime("%A %B %dth, %Y at ") + datetime.now().strftime(
        #     "%H%M") + (".pdf"))
        # send_email(str("Weather Forecast on ") + date.today().strftime("%A %B %dth, %Y at ") + datetime.now().strftime(
        #     "%H%M") + (".jpg"))

        img_jpg = img.convert("RGB")
        img_jpg.save("Weather Forecast.jpg")
        # send_email("Weather Forecast.jpg")

