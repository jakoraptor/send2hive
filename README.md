# send2hive
This script is used to upload observables to a given hive case from a remote host. 

Replace \*\*\*HIVEURL AND PORT\*\*\* (in the script) with the url of the hive e.g. http://localhost:9000

## Usage
For the script to work it requires a local environment variable called "hiveAPIkey" to be created for the user making the call. <BR>First, log in to the hive and reveal/copy your API key<BR>Then on the server sending the file, create the environment variable i.e.<BR>
 <code>export hiveAPIkey=***VALID API KEY***</code><BR>
To send a file to the hive the usage is as follows:<BR>
 <code>python3 sendfile.py "filename" "case id"</code>
