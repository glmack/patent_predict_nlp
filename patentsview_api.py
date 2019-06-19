import requests
import json
import time
import os

class PatentsViewApi(object):
    def __init__(self):
        super(PatentsViewApi, self).__init__()

    def get_patent(self, search_keywords, results_fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        patents = []
        params = {
            '_text_any': search_keywords,
            'fields': ",".join(results_fields)
        }
        response = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        patents.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return patents

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details