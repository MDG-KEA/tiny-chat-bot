# Importere library til at forbinde til adafruit.io
import mqttBotPubSub
from machine import Pin
from time import sleep
import dht

lib = mqttBotPubSub

sensor = dht.DHT11(Pin(14))
Pin(14, Pin.OUT, value=0)

while True:
    try:
        # her måler vi på vores temp/hum sensor
#         sleep(2)
#         sensor.measure()
#         temp = sensor.temperature
#         hum = sensor.humidity

        #if temp >= 20.0:
            # panic message
            #lib.client.publish(topic=lib.mqtt_pub_feedname, msg="HOT HOT HOT")
            # tøm strengen igen
            #lib.m = ""

        # lib.m vil indholde strengen som indtastes i feltet "skriv til Jarvis"
        # Hvis strengen er identisk med "Streng til Bot" køres koden i if sætningen
        if lib.m == "streng til bot":
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="streng fra bot")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            lib.m = ""

        # "Hej Friday" og svarer "Hello Sir"
        if lib.m == "hej friday":
            # strengen botten returnere
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Hello sir.")
            # tøm strengen igen
            lib.m = ""

        # Joke 1
        if lib.m == "fortæl en joke friday":
            # strengen botten returnere
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Rank 14.")
            # tøm strengen igen
            lib.m = ""

        # Joke 2
        if lib.m == "fortæl en anden joke friday":
            # strengen botten returnere
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="You're not rank 14, you scrub.")
            # tøm strengen igen
            lib.m = ""

        # Fortæl DHT11's temperatur
        if lib.m == "friday hvad er temperaturen?":
            # botten returnere først on confirm at den tjekker
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="One moment, I will check the temperature.")
            # tøm strengen igen
            lib.m = ""
           # lav en temp måling
            sleep(2)
            sensor.measure()
            temp = sensor.temperature()

           # hvis temp er for høj send for varm besked
            if temp > 30.0:
                lib.client.publish(topic=lib.mqtt_pub_feedname, msg="HOT HOT HOT")
                lib.client.publish(topic=lib.mqtt_pub_feedname, msg="HOT HOT HOT")
                lib.client.publish(topic=lib.mqtt_pub_feedname, msg="HOT HOT HOT")
                lib.m = ""
           # hvis temp er for lav send kold besked
            elif temp < 18.0:
                lib.client.publish(topic=lib.mqtt_pub_feedname, msg="COLD COLD COLD")
                lib.client.publish(topic=lib.mqtt_pub_feedname, msg="COLD COLD COLD")
                lib.client.publish(topic=lib.mqtt_pub_feedname, msg="COLD COLD COLD")
                lib.m = ""
           # hvis temperaturen er okay, send temp målingen
            else:
                lib.client.publish(topic=lib.mqtt_pub_feedname, msg="The temperature is: %3.1f C" % temp)
                lib.m = ""

        # fortæl hvad fugtigheden er
        if lib.m == "friday hvad er fugtigheden?":
            # botten returnere først on confirm at den tjekker
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="One moment, I will check the humidity.")
            # tøm stregen igen
            lib.m = ""
            # tjekker her fugtigheden og sender besked hvad fugtigheden er
            sleep(2)
            sensor.measure()
            hum = sensor.humidity()
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="The humidity is: %3.1f" % hum)
            # tøm besked igen
            lib.m = ""

        # tænd lampen
        if lib.m == "friday taend lyset":
            # der tændes for lampen på pin 4
            Pin(4, Pin.OUT, value=1)
            # botten skriver den har tændt
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="I have turned on the light, sir.")
            # tøm besked igen
            lib.m = ""

        if lib.m == "friday sluk lyset":
            # der slukkes for lampen på pin 4
            Pin(4, Pin.OUT, value=0)
            # botten skriver den har slukket
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="I have turned off the light, sir.")
            # tøm beskeden igen
            lib.m = ""

        # Tjekker for nye beskeder
        lib.client.check_msg()
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
