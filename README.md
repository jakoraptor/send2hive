# send2hive
This script is used to upload observables to a given hive case from a remote host. 

Replace \*\*\*HIVEURL AND PORT\*\*\* (in the script) with the url of the hive e.g. http://localhost:9000

## Usage
For the script to work it requires an environment variable called "hiveAPIkey" to be created for the user making the call. <BR>To do this, log in to the hive and reveal your API key. Then run:<BR>
 <code>export hiveAPIkey=***VALID API KEY***</code><BR>
To send a file to the hive the usage is as follows:<BR>
 <code>python3 sendfile.py "filename" "case id"</code>
