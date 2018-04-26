import requests
import json
import time
import codecs
import sys
meetup_api_key = ''



def main():

	#Get cities to be pulled from Meetup
	locations = getCitiesFromCSV()
	print(locations)

	for city in locations:
		per_page = 10
		current_results = per_page
		offset = 0
		while (current_results == per_page):
			params = {"sign":"true","country":"US", "city":city[0], "state":city[1], "radius": 10, "key":meetup_api_key, "page":per_page, "offset":offset }
			response = call(params)
			time.sleep(1)
			offset += 1
			for group in response['results']:
				category = ""
				if "category" in group:
					category = group['category']['name']
				print(group['name'])


def call(params):
	req = requests.get("http://api.meetup.com/2/groups", params = params)
	data = req.json()
	return data




"""
Reads locations.csv to get all cities in list form with state. 
"""
def getCitiesFromCSV():
	locations = []
	for line in open('locations.csv', "r", encoding='utf-8-sig'):
		place = line.split(",")
		locations.append([place[0].strip(), place[1].strip()])

	return locations


if __name__=="__main__":
   main()