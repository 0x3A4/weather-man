#imports
import requests as r
import json
import csv

#general variables
ziparray = ['00000']
latarray = ['0.00']
lngarray = ['0.00']

#weather api key
wkey = open('api.key', 'r').read().splitlines()[0]


#zip parser
with open('zip.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ziparray.append(row['ZIP'])
        latarray.append(row['LAT'])
        lngarray.append(row['LNG'])

userzip = input('what is your zipcode? ').strip()
for x in range(1000):
    try:
        if len(userzip) == 5:
            if int(userzip) >= 0:
                userzip = str(userzip)
                zipindex = ziparray.index(userzip)
                lat = str(round(float(latarray[zipindex]),2))
                lng = str(round(float(lngarray[zipindex]),2))
                           
            else:
                userzip = input('wrong format. please enter a 5 digit zip code ')
        else:
            userzip = input('wrong format. please enter a 5 digit zip code ')
        
   
    except TypeError:
        userzip = input('wrong format. please enter a 5 digit zip code ')
    
    except ValueError: 
        userzip = input('invalid zip code. please enter a valid 5 digit zip code ')
#print(userzip, lat, lng)


#get json
weatherreq = r.get("https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lng + "&appid=" + wkey+ "&units=imperial")
wjson = weatherreq.text
wjson = json.loads(wjson)
#print(json.dumps(wjson, indent=4))


#parse json into variables
currenttemp = wjson['main']['temp']
hightemp = wjson['main']['temp_max']
lowtemp = wjson['main']['temp_min']
conditions = wjson['weather'][0]['main']
icon = wjson['weather'][0]['icon']
wind = wjson['wind']['speed']
winddeg = wjson['wind']['deg']


#output
print('')
print('Your current tempurature is:', currenttemp)
print('The low is:', lowtemp)
print('The high is:', hightemp)
print('It is currently', conditions)
print('The current windspeed is:', wind)
print('at', winddeg, 'degrees.')

#ideas
#make catch statement to check for response code, if error occurs tell end user to try again later or wtvr
#create auto update button using loops and gui
#just the gui in general


