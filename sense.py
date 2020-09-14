#!/usr/bin/python3.7

import datetime
from sense_hat import SenseHat


CSV = True
DB = False


sense = SenseHat()
sense.clear()

temp = sense.get_temperature()

humidity = sense.get_humidity()


if CSV:
    with open('/home/pi/senseHat/andmed.csv','a') as f:
        praegu = datetime.datetime.now()
        praegu_päev = praegu.strftime("%d/%m/%Y")
        praegu_kell = praegu.strftime("%H.%M.%S")
        praegu_nädalapäev = praegu.isoweekday()
        praegu_ISO = praegu.isoformat()
        andmed = f"{praegu_ISO},{praegu_päev},{praegu_kell},{praegu_nädalapäev},{temp},{humidity} \n"
        f.write(andmed)

# Add SQL later!

# Add web server even later!
