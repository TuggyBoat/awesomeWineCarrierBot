from __future__ import print_function
import json
import os.path
from asyncio import sleep
from dotenv import load_dotenv

from apiclient import discovery
from google.oauth2 import service_account

load_dotenv()

def get_responses():
    SCOPES = ["https://www.googleapis.com/auth/forms.responses.readonly", 'https://www.googleapis.com/auth/drive']
    secret_file = os.path.join(os.getcwd(), os.getenv('SECRET_FILE'))
    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=SCOPES)
    service = discovery.build('forms', 'v1', credentials=credentials)

    form_id = os.getenv('FORM_ID')

    result = service.forms().responses().list(formId=form_id).execute()
    metadata = service.forms().get(formId=form_id).execute()

    print(metadata)

    with open('responses.json', 'w') as file:
        json.dump(result, file)

    with open('responses.json', 'r') as file:
        return json.load(file)


