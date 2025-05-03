import requests

def getAPIContent(api_key, api_url):
    request_url = f'{api_url}?api_key={api_key}'

    #get returns data in a df.  Using .json converts json formatted data into a python dictionary
    api_content = requests.get(request_url).json()

    return api_content