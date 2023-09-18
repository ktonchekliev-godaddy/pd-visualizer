#!/opt/homebrew/bin/python3
import pdpyras
import os
import sys
import json

configLocation = "########"

def displayIncidents():
    if not os.path.exists(configLocation):
        sys.exit("Couldn't file config file in: {location}".format(location=configLocation))

    with open(configLocation) as file:
        configData = json.loads(file.read())

    pdSession = pdpyras.APISession(configData['apiToken'])
    incidentResponse = pdSession.jget("/incidents?user_ids[]={userId}".format(userId=configData['userId']))
    incidentCount = len(incidentResponse['incidents'])
    print("Incidents: {incidentCount}".format(incidentCount=incidentCount))
    if incidentCount > 0:
        print("---")
        for incident in incidentResponse['incidents']:
            incidentTile = incident['title']
            incidentColor = "black" if incident['status'] == 'acknowledged' else "yellow"
            incidentUrl = incident['html_url']
            print("{title} | color={color} | href={url} | length=60".format(title=incidentTile.replace('|', ''), color=incidentColor, url=incidentUrl))


if __name__ == "__main__":
    displayIncidents()
