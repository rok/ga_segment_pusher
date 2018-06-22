import time
import logging
import hashlib
# Required to silence caching problems error for certain api clients
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.http import MediaFileUpload
from apiclient.discovery import build

def get_service(key_file_location, api_name='analytics', api_version='v3',
    scopes = ['https://www.googleapis.com/auth/analytics.edit',
              'https://www.googleapis.com/auth/analytics']):
    """Get a service that communicates to a Google API.

    Args:
    key_file_location: The path to a valid service account JSON key file.
    api_name: The name of the api to connect to.
    api_version: The api version to connect to.
    scope: A list auth scopes to authorize for the application.

    Returns:
    A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service

def upload_csv(csv_filename, analytics, account_id, web_property_id,
    custom_data_source_id):
    """Uploads provided csv to specified Google Analytics account,
    to under specified web property and assigns it custom data
    source id.
    
    Args:
    csv_filename: Path to CSV file containing data to insert into
        the dataset.
    account_id: Id of the Google Analytics account.
    web_property_id: Id of Google Analytics web property.
    custom_data_source_id: Custom data source Id assigned to the
        targeted dataset.
    analytics: Instance of apiclient service object. 

    Returns:
    Upload status.
    """

    try:
        # Create a media object to be uploaded
        media = MediaFileUpload(csv_filename,
                              mimetype='application/octet-stream',
                              resumable=False)
        upload = analytics.management().uploads().uploadData(
            accountId=account_id,
            webPropertyId=web_property_id,
            customDataSourceId=custom_data_source_id,
            media_body=media).execute()
        
        return upload

    except TypeError as error:
        # Handle errors in constructing a query.
        print('There was an error in constructing your query : %s' % error)