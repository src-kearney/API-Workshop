import requests
import webbrowser

key = 'api_key'

def main():
    page()

def random():
    response = requests.get(
        'https://sandbox-api.brewerydb.com/v2/beer/random',
        params={'key': key},
    )

    json_response = response.json()
    print(json_response)

def page():

    response = requests.get(
        'https://sandbox-api.brewerydb.com/v2/breweries/',
        params={'p':'1','key': key},
    )

    json_response = response.json()
    breweries = json_response["data"]

    brewery = None

    for item in breweries:
        if(item["name"] == "Guinness"):
            brewery = item

    print(brewery)
    webbrowser.open_new(brewery["images"]["medium"])

if __name__ == '__main__':
    main()
