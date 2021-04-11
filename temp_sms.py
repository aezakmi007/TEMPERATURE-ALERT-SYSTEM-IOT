import confy, json, time
from boltiot import Sms, Bolt
import json, time

minimum_limit = 400
maximum_limit = 600


mybolt =  Bolt(confy.API_KEY, confy.DEVICE_ID)
sms = Sms(confy.SID, confy.AUTH_TOKEN, confy.TO_NUMBER, confy.FROM_NUMBER)



while True:
           print("Reading sensor value")
           response = mybolt.analogRead('A0')
           data = json.loads(response)
           print("sensor value is : " + str(data['value']))
           try:
               sensor_value = int(data['value'])
               if sensor_value > maximum_limit or sensor_value < minimum_limit:
                   print("making request to Twilio to send a SMS")
                   response = sms.send_sms("The current temperature sensor value is" + str(sensor_value))
                   print("Response received from Twilio is: " +str(response))
                   print("status of SMS at Twilio is : " + str(response.status))
           except Exception as e:
                print("Error occured: Below are the details")
                print (e)

           time.sleep(10)
