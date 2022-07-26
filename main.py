import requests
import json

"""Taken from the tutorial here: https://www.dataquest.io/blog/last-fm-api-python/"""


def lastfm_get(payload):
    """
    lastfm_get() will query the LastFM API.
    :param payload: the payload to send, including the API key needed to use their service.
    :return: a JSON formatted response.
    """

    # define headers and URL
    headers = config_json['header']  # {'user-agent': 'BigGuyWhoKills'}
    api_key = api_key_json['apiKey']
    url = config_json['url']

    # Add API key and format to the payload
    payload['api_key'] = api_key
    payload['format'] = 'json'

    return requests.get(url, headers=headers, params=payload)


def json_print(obj):
    """
    json_print() will print the results in a formatted manner.
    :param obj: the raw JSON to format and print to screen.
    :return: none
    """

    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


if __name__ == '__main__':
    with open('config.json') as file:
        config_json = json.load(file)
    with open('apiKey.json') as file:
        api_key_json = json.load(file)
    # headers = {'user-agent': 'BigGuyWhoKills'}

    # payload = {'api_key': api_key, 'method': 'chart.gettopartists', 'format': 'json'}
    response = lastfm_get({'method': 'chart.gettopartists'})
    # print(response.status_code)
    # print(response.text)
    json_print(response.json())
