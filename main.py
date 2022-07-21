from __future__ import print_function
import json
import os.path
from asyncio import sleep

import gspread
from dotenv import load_dotenv
import pandas as pd
from apiclient import discovery
from google.oauth2 import service_account

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/forms.responses.readonly", 'https://www.googleapis.com/auth/drive',
          'https://spreadsheets.google.com/feeds']
secret_file = os.path.join(os.getcwd(), os.getenv('SECRET_FILE'))
credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=SCOPES)
service = discovery.build('forms', 'v1', credentials=credentials)
sheets_service = discovery.build('sheets', 'v4', credentials=credentials)
gc = gspread.authorize(credentials)


def get_responses():
    form_id = os.getenv('FORM_ID')

    result = service.forms().responses().list(formId=form_id).execute()
    metadata = service.forms().get(formId=form_id).execute()

    # print(metadata)

    with open('responses.json', 'w') as file:
        json.dump(result, file)

    with open('responses.json', 'r') as file:
        return json.load(file)


def push_to_sheet(dataframe: pd.DataFrame):
    sheet_key = os.getenv('SHEET_ID')
    sheet = gc.open_by_key(sheet_key)
    worksheet = sheet.worksheet('Responses from Python')
    worksheet_dataframe = pd.DataFrame(worksheet.get_all_records())

