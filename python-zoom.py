## As a good portion of this code is directly from Geeks 4 Geeks,
## I will signify what portions of code are MINE (written, not dictated)
## This signifier will be with the line MW

import jwt
import requests
import json
from time import time

## MW START
import os
from dotenv import load_dotenv
## MW END


## MW START

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

# file = open('.env', 'r', encoding='utf-8')

# line = file.readline()
# line2 = file.readline()

# API_KEY = line
# API_SEC = line2

## MW END


# create a function to generate a token
# using the pyjwt library

# MW START (I rewrote the generateToken function using a different JWT library)

def generateToken():
	encoded = jwt.encode({'iss': API_KEY, 'exp': time() + 5000}, API_SECRET, algorithm="HS256")
	return encoded

	# jwtInstance = jwt.JWT()

	# # Create a payload of the token containing
	# # API Key & expiration time
	# jwtMessage = {'iss': API_KEY, 'exp': time() + 5000},
	# # create a token using the api secret, the api key, and a hashing algo

	# # Secret used to generate token signature
	# # Specify the hashing alg
	# token = jwtInstance.encode(jwtMessage, API_SECRET, alg='HS256')
	# return token.decode('utf-8')

# MW END

# create json data for post requests
meetingdetails = {
    "topic": "Dennyzens Hangout",
    "type": 2,
    "start_time": "2019-06-14T10: 21: 57",
    "duration": "120",
    "timezone": "America/Los_Angeles",
    "agenda": "Study and hunt for jobs together",
    "recurrence": {
        "type": 8,
        "end_times": 10,
        "repeat_interval": 10,
        "type": 1,
    },
    "settings": {
        "host_video": "false",
        "participant_video": "false",
        "join_before_host": "true",
        "mute_upon_entry": "false",
        "watermark": "true",
        "audio": "voip",
        "auto_recording": "none"
    }
}

# send a request with headers including
# a token and meeting details

generateToken()

def createMeeting():
	headers = {'authorization': 'Bearer ' + generateToken(),
			'content-type': 'application/json'}

	response = requests.post(
		f'https://api.zoom.us/v2/users/me/meetings',
		headers=headers, data=json.dumps(meetingdetails))

	solution = json.loads(response.text)
	join_URL = solution["join_url"]

	URL = print(f'{join_URL}')

	return URL


# run the create meeting function
createMeeting()
