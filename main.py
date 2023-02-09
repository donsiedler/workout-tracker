import requests
from local_settings import APP_ID, API_KEY
from local_settings import GENDER, WEIGHT_KG, HEIGHT_CM, AGE

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

workout_input = input("Tell me what did you do today?\n")

api_params = {
    "query": workout_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


response = requests.post(API_ENDPOINT, headers=headers, json=api_params)
print(response.text)
