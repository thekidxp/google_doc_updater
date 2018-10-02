from googleapiclient.discovery import build


def find_file(credentials, sheets_servie):
    drive_service = build('drive', 'v3', credentials=credentials)

    results = drive_service.files().list(q="name='Signup_Sheet'",
                                         fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        return create_sheet(sheets_servie)
    elif len(items) > 1:
        return 1
    else:
        return items[0]


def update_sheet(sheets_service, spreadsheet_id, range_name, body):
    return sheets_service.spreadsheets().values().append(spreadsheet_id,
                                                         range_name,
                                                         'RAW',
                                                         body).execute()


def create_sheet(sheets_service):
    return sheets_service.spreadsheets().create(body='').execute()


def share_sheet():
    return 0
