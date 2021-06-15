import requests
import json

class Api:
    def __init__(self):
        pass
    def get_report(self,user):
        url = "https://covid-19-data.p.rapidapi.com/country"

        querystring = {"name": user}

        headers = {
            'x-rapidapi-key': "638206764amsh615fd80b9791697p13f966jsn289a12c5eb5c",
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return json.loads(response.text)

# def xyz():
#     A = Api()
#     A.get_report("india")
