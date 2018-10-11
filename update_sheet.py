from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']
private_key = ''
email = ''
uri = 'https://oauth2.googleapis.com/token'
sheet_id = '1Ejmo4SPTuAtOvy96RYWhKpFVUPaaWJ5NHRms-VaYm_g'


def update_handler(event, context):
    service_info = {
        "private_key": private_key,
        "client_email": email,
        "token_uri": uri,
    }
    credentials = service_account.Credentials.from_service_account_info(service_info, scopes=SCOPES)
    sheets_service = build('sheets', 'v4', credentials=credentials, cache_discovery=False)

    spreadsheet_id = sheet_id
    range_name = 'Sheet1'
    body = {
        'values': [[event['key1'], event['key2'], event['key3'], event['key4']]]
    }

    return sheets_service.spreadsheets().values().append(spreadsheetId=spreadsheet_id,
                                                           range=range_name,
                                                           valueInputOption='RAW',
                                                           body=body).execute()


if __name__ == '__main__':
    update_handler('', '')