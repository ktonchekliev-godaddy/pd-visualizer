import pdpyras
import rumps
import json
import os
import sys

class incidentVisualizer(rumps.App):
    configLocation = "########"
    pollingTime = 3

    def __init__(self):
        if not os.path.exists(self.configLocation):
            sys.exit("Couldn't file config file in: {location}".format(location=self.configLocation))

        with open(self.configLocation) as file:
            self.configData = json.loads(file.read())

        super().__init__("Incidents: 0")
        self.session = pdpyras.APISession(self.configData['apiToken'])

    @rumps.timer(pollingTime)
    def updateIncidents(self, _):
        incidentResponse = self.session.jget("/incidents?user_ids[]={userId}".format(userId=self.configData['userId']))
        self.title = "Incidents: {incidentCount}".format(incidentCount=len(incidentResponse['incidents']))


if __name__ == "__main__":
    incidentVisualizer().run()
