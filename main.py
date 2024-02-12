import os

import requests

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")


def get_token():
    url = "https://api.vonage.com/token"
    payload = 'grant_type=password&username={}&password={}&client_id={}&client_secret={}'.format(USERNAME, PASSWORD,
                                                                                                 CLIENT_ID, SECRET)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def get_company_call_recordings(token, account_id="self"):
    url = "https://api.vonage.com/t/vbc.prod/call_recording/v1/api/accounts/{}/company_call_recordings".format(
        account_id)

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer {}'.format(token),
    }

    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    return response.json()


if __name__ == "__main__":
    # Get Token
    token_response = get_token()
    access_token = token_response["access_token"]

    # Get company call recordings
    company_call_recordings = get_company_call_recordings(token=access_token)

    print(company_call_recordings)
