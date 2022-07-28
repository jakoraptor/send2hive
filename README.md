# send2hive
This script is used to upload observables to a given hive case from a remote host. 

Replace \*\*\*HIVEURL AND PORT\*\*\* (in the script) with the url of the hive e.g. http://localhost:8000

## Usage
For the script to work it requires a keyring entry called "hiveapi" with the user's api key.
<BR>First, log in to the hive and reveal/copy your API key<BR>Then on the server sending the file, add valid user api key to keyring "hiveapi" i.e.<BR>
 <code>keyring set hiveapi <username></code><BR>
To send a file to the hive the usage is as follows:<BR>
 <code>python3 sendfile.py "filename" "user" "case id"</code>
