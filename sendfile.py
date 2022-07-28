#!/usr/bin/python3

import sys
import json
import keyring
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable

if len(sys.argv) != 4:
    print('Usage: python3 sendfile.py "filename" "user" "case id"\nBefore running, add valid user api key to keyring "hiveapi" eg. "keyring set hiveapi <username>"')
    sys.exit(1)

hiveurl="https://localhost:8000" # <<< CHANGE THIS
apikey=keyring.get_password("hiveapi",sys.argv[2])
api = TheHiveApi(hiveurl, apikey) # <<< ADD cert=False HERE IF SSL NOT USED

try:
    # Init the CaseObservable object
    file_observable = CaseObservable(dataType='file',
        data=sys.argv[1],
        tlp=2,
        ioc=False,
        sighted=True,
        tags=['thehive4py'],
        message='Observable sent using thehive4py'
    )

    # Call the API
    response = api.create_case_observable(sys.argv[3], file_observable)

    # Display the results
    if response.status_code == 201:
        # Get response data
        observableJson = response.json()

        # Display response data
        print(json.dumps(observableJson, indent=4, sort_keys=True))
    elif response.status_code == 401:
        print('Usage: python3 sendfile.py "filename" "user" "case id"')
        print('Authentication Failure: Check user API key in keyring - Example: "keyring set hiveapi <username>"')
    else:
        print('Usage: python3 sendfile.py "filename" "user" "case id"')
        print(f'Failure: {response.status_code}/{response.text}')

    sys.exit(0)
except OSError as e:
    print(f'Usage: python3 sendfile.py "filename" "user" "case id"\n{e}')
