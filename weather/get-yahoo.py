###
# Weather Alarm Clock
#
# Requires: urllip, json, datetime, subprocess
#
# Mac Requirements: system 
# 
# Speech Recognition requires: SpeechRecognition, portaudio (for Mac)
#
###

import urllib, json, datetime, subprocess
import speech_recognition as sr
from os import system

## Defaults
sayCmd = "say -v Oliver "
timeOfDay = ('Morning', 'Morning', 'Morning', 'Morning', 'Morning', 'Morning', 'Morning', 'Morning', 'Morning', 'Morning', 'Morning', 'Afternoon', 'Afternoon', 'Afternoon', 'Afternoon', 'Afternoon', 'Afternoon', 'Evening', 'Evening', 'Evening', 'Evening', 'Evening', 'Evening', 'Morning')
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
months = ('January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
name = 'Christopher'

## Speech function
def speek( cmd, say ):
	system( cmd + say )
	return

## Play/loop alarm sound
audio_file = "alarm_beep.wav"
#for _ in range(2):
#	subprocess.call(["afplay", audio_file])
	
## Setup time of day
today = datetime.datetime.today()
currAbsTime = today.hour
currWeekday = today.weekday()
currMonth = today.month
currDay = today.day
currYear = today.year

speek(sayCmd, "Good " + timeOfDay[abs(currAbsTime)] + " " + name + ". Today is " + weekdays[int(currWeekday)] + ", " + months[int(currMonth - 1)] + " " + str(currDay) + ", " + str(currYear))

## Setup Yahoo! Weather API query, and request JSON feed
burlingtonQuery = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="burlington, nc")'
yahooWeatherEndpoint = 'https://query.yahooapis.com/v1/public/yql?q=' + burlingtonQuery + '&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
yahooWeatherResponse = urllib.urlopen(yahooWeatherEndpoint)
yahooWeatherData = json.loads(yahooWeatherResponse.read())
#print yahooWeatherData

## Do forecast stuff
forecast = yahooWeatherData['query']['results']['channel']['item']['forecast']
forecastToday = forecast[0]
forecastText = forecastToday['text']
forecastTodayHigh = forecastToday['high']
forecastTodayLow = forecastToday['low']
forecastTodaySpeek = "The forecast is " + forecastText + " with a high of " + forecastTodayHigh + ", and a low of " + forecastTodayLow + " degrees fahrenheit"

speek(sayCmd, forecastTodaySpeek)


## Forecast, 5 day loop
#print forecast
#for x in forecast:	
#	day = x['day']
#	date = x['date']
#	high = x['high']
#	low = x['low']
#	speek = "The forecast for" + day + ", " + date + " is a high of " + high + " degrees, and a low of " + low + " degrees fahrenheit"
#	system('say -v Oliver ' + speek)