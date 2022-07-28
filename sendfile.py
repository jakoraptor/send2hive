import sys
import json
import os
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable

hiveurl='***HIVEURL AND PORT***' # <<< CHANGE THIS
apikey=os.environ.get('hiveAPIkey')

api = TheHiveApi(hiveurl, apikey)


if len(sys.argv) < 3:
    print('Usage: python3 sendfile.py "filename" "case id"\nBefore running, add valid api key to environment variable "hiveAPIkey" using "export hiveAPIkey=***KEY***"')
    sys.exit(1)

try:
    # Init the CaseObservable object
    file_observable = CaseObservable(dataType='file',
        data=sys.argv[1],
        tlp=2,
        ioc=False,
        sighted=True,
        tags=['thehive4py'],
        message='test'
    )

    # Call the API
    response = api.create_case_observable(sys.argv[2], file_observable)

    # Display the results
    if response.status_code == 201:
        # Get response data
        observableJson = response.json()

        # Display response data
        print(json.dumps(observableJson, indent=4, sort_keys=True))
    elif response.status_code == 401:
        print('Usage: python3 sendfile.py "filename" "case id"')
        print('Authentication Failure: Check hiveAPIkey environment variable has valid key')
    else:
        print('Usage: python3 sendfile.py "filename" "case id"')
        print(f'Failure: {response.status_code}/{response.text}')

    sys.exit(0)
except OSError as e:
    print(f'Usage: python3 sendfile.py "filename" "case id"\n{e}')
