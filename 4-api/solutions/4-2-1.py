import requests

'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/entityrecognition' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 3e87733d504b1731c65e565e' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=The%20Dallas%20Cowboys%20are%20a%20far%20better%20team%20than%20the%20New%20York%20Giants%20this%20year.%20The%20Giants%20have%20not%20won%20a%20conference%20game%20yet.'
'''

apikey = '3e87733d504b1731c65e565e'
url = 'https://cent.ischool-iot.net/api/azure/entityrecognition'

def extract_entities(text: str) -> dict:
    '''
    Extract entities from the text using Azure entity recognition API.
    '''
    headers = {
        'accept': 'application/json',
        'X-API-KEY': apikey,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    data = {
        'text': text
    }
    
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()

text = "The Dallas Cowboys are a far better team than the New York Giants this year. The Giants have not won a conference game yet."
results = extract_entities(text)
entities = results['results']['documents'][0]['entities']
for entity in entities:
    print(f"{entity['text']}: {entity['category']}")