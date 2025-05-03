import requests

def getAPIContent(api_key, api_url):
    request_url = f'{api_url}?api_key={api_key}'

    api_content = requests.get(request_url).json()

    return api_content