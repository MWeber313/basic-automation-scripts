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

print(API_KEY)
print(API_SECRET)

## MW END


# create a function to generate a token
# using the pyjwt library


def generateToken():
	token = jwt.encode(

		# Create a payload of the token containing
		# API Key & expiration time
		{'iss': API_KEY, 'exp': time() + 5000},

		# Secret used to generate token signature
		API_SECRET,

		# Specify the hashing alg
		algorithm='HS256'
	)
	return token.decode('utf-8')


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
        "auto_recording": "cloud"
    }
}

# send a request with headers including
# a token and meeting details

def createMeeting():
	headers = {'authorization': 'Bearer ' + generateToken(),
			'content-type': 'application/json'}
	r = requests.post(
		f'https://api.zoom.us/v2/users/me/meetings',
		headers=headers, data=json.dumps(meetingdetails))

	print("\n creating zoom meeting ... \n")
	# print(r.text)
	# converting the output into json and extracting the details
	y = json.loads(r.text)
	join_URL = y["join_url"]
	meetingPassword = y["password"]

	print(
		f'\n here is your zoom meeting link {join_URL} and your \
		password: "{meetingPassword}"\n')


# run the create meeting function
createMeeting()
