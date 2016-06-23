from django.test import TestCase
from flask import json
# Create your tests here.
from urllib2 import urlopen
from bs4 import BeautifulSoup

url = "http://caprodseacs03.cloudapp.net/scorecards/full/1814/39581?format=json"
response = urlopen(url)
data = json.loads(response.read())
scoreCard = data['fullScorecard']
for innings in scoreCard['innings']:
    # self.batsmen.append(innings['batsmen'])
    # self.bowlers.append(innings['bowlers'])
    # self.other_info.append({
    #     'wicket' : innings['wicket'],
    #     'run': innings['run'],
    #     'over': innings['over'],
    #     'extra': innings['extra'],
    #     'bye': innings['bye'],
    #     'legBye': innings['legBye'],
    #     'wide': innings['wide'],
    #     'noBall': innings['noBall'],
    # })
    inning =dict(zip(innings, innings))

print inning
