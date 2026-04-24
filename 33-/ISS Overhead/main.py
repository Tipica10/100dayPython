import requests
from datetime import datetime
import smtplib
import time

my_email = "theephigab@gmail.com"
password= "odtedgojkoclyfwy"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
close = (abs(iss_latitude - MY_LAT) <= 5 or abs(iss_longitude - MY_LONG) <= 5)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_hour = datetime.now().hour

is_dark = sunset < time_hour or sunrise > time_hour

while is_dark and close:
    time.sleep(60)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="theephiga04@outlook.com",
                            msg=f"Subject:ISS Overhead\n\nLook up!")




