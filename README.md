# send2hive
This script is used to upload observables to a given hive case from a remote host. 

## Usage
For the script to work it requires an environment variable called "hiveAPIkey" to be created for the user making the call. To do this, log in to the hive and reveal your API key. Then run:
 export hiveAPIkey=***VALID API KEY***
To send a file to the hive the usage is as follows:
 python3 sendfile.py "filename" "case id"
