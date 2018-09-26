from __future__ import print_function
from google.oauth2 import service_account
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def main(values):
    service_account_file = ''
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
    sheets_service = build('sheets', 'v4', credentials=credentials)

    file = find_file(credentials)
    if file == 1:
        return

    spreadsheet_id = file['id']
    range_name = 'Sheet1'
    body = {
        'values': values
    }

    result = sheets_service.spreadsheets().values().append(spreadsheet_id,
                                                           range_name,
                                                           'RAW',
                                                           body).execute()
    print('{0} cells appended.'.format(result
                                       .get('updates')
                                       .get('updatedCells')))


def find_file(credentials):
    drive_service = build('drive', 'v3', credentials=credentials)

    results = drive_service.files().list(q='Signup_Sheet',
                                         fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        return create_sheet()
    elif len(items) > 1:
        return 1
    else:
        return items[0]


def create_sheet():
    return 0


def share_sheet():
    return 0


if __name__ == '__main__':
    main([''])
