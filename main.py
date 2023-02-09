from datetime import datetime
import requests
from local_settings import APP_ID, API_KEY, AUTH_TOKEN
from local_settings import GENDER, WEIGHT_KG, HEIGHT_CM, AGE, USERNAME

PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"
NUTRITIONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

NUTRITIONIX_API_HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

SHEETY_API_HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
}

workout_input = input("Tell me what did you do today?\n")

api_params = {
    "query": workout_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(NUTRITIONIX_API_ENDPOINT, headers=NUTRITIONIX_API_HEADERS, json=api_params)
response.raise_for_status()
workout_data = response.json()["exercises"]

now = datetime.now()

for exercise in workout_data:
    row_to_save = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    r = requests.post(SHEETY_API_ENDPOINT, headers=SHEETY_API_HEADERS, json=row_to_save)
    r.raise_for_status()
    print(r.json())
