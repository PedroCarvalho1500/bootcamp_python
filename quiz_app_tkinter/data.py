import requests
import html

parameters = {
    "amount": 20,
    "type": "boolean"
}

html_decod = {

}

response = requests.get("https://opentdb.com/api.php",params= parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]


