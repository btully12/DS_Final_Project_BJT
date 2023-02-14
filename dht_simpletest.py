import board
import adafruit_dht
import time
from datetime import datetime
import pytz
import os
import time
import datetime
import glob
from time import strftime
import MySQLdb
import sys
import requests
import board
import adafruit_dht
import time
from datetime import datetime
import pytz

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)



# Routine to insert temperature records into the pidata.temps table:
def insert_record( device, datetime, temp, hum ):
        sql = "INSERT INTO rpisenso (device, datetime,temp,hum) VALUES (%s, %s,%s,%s)"
        val = (machine_1,time_in_lou,temperature_f, humidity,)
        
        try:
            conn = MySQLdb.connect(user="brett",password="bretttully",host="127.0.0.1",database="sensor")
            cursor = conn.cursor()
            cursor.execute(sql, val)
            conn.commit()
        
        except Exception as error:
            print(error)
        finally:
            cursor.close()
            conn.close()


# Main loop
try:
        while True: 
                temperature_c = dhtDevice.temperature
                temperature_f = round(temperature_c * (9 / 5) + 32,2)
                humidity = dhtDevice.humidity
                machine_1 = "P004"
                lou_time = pytz.timezone("America/New_York")
                ft = "%Y-%m-%d %H:%M:%S"
                time_in_lou = datetime.now(lou_time).strftime(ft)
                insert_record(machine_1,str(time_in_lou),format(temperature_f,'.2f'),format(humidity,'.2f'))
                time.sleep(.10)

except (IOError,TypeError) as e:
    print("Exiting...")

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print("Stopping...")
