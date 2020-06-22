import json
import requests

def accessAPI(event):
  
    # Enter your API key here 
    api_key = "55e2d8de716e1ac27bd082681f5bcbe1"
  
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
    # Give city name 
    #zip_code = event['Details']['Parameters']['zip']
    zip_code = "97068"
  
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "zip=" + zip_code + "&appid=" + api_key
   
    print(complete_url)
   
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
  
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
  
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
  
        # store the value of "main" 
        # key in variable y 
        print(x)
        y = x["main"] 
  
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
  
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
  
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
  
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
  
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
  
        # print following values 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
                        
    else: 
        print(" City Not Found ") 
        
    return str(weather_description)

def lambda_handler(event, context):
    
    weather = accessAPI(event)
    
    return {
        'statusCode': 200,
        'description': weather
    }
