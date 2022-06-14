# grabGitCommits
The script grabs public Github commits and saves to your Mongodb

## FAQ

There are two scripts, one is for triggering the script using HTTP endpoint, the other is to run the script through a command-line interface

## Requirements

1. MongoDB - host address & port
2. Python 3
3. Repository that you want

## How To

### A. Using the HTTP endpoint

1. Launch the terminal from the folder and enter ```python http_endpoint.py```
2. Open browser and at the tab, enter:  ```host:port/<repository_owner>/<repository_file>/<mongodb_host>/<mongodb_port>``` be sure to replace the value < > as shown in the example below:

3. Example: your server is hosted at 192.168.0.1 and the port used is 42069 where your github repository is https://github.com/flutter/flutter therefore it should be ```192.168.0.1:42069/flutter/flutter/localhost/5000```

* host = 192.168.0.1
* port = 42069
* repository_owner = flutter
* repository_file = flutter
* mongodb_host = localhost
* mongodb_port = 5000

4. Let it run
5. Your MongoDB is now updated :D

### B. Using your CLI

1. Launch the terminal from the folder and enter ```python grab_commits.py <repository_owner> <repository_name> <mongodb_host> <mongodb_port```
2. Example: your server is hosted at 192.168.0.1 and the port is 69420 where your github repository is https://github.com/microsoft/vscode therefore it should be ``` python grab_commits.py microsoft vcode localhost 5000``` as:

* repository_owner = microsoft
* repository_file = vscode
* mongodb_host = localhost
* mongodb_port = 5000

3. If you used ```python grab_commits.py``` then just do enter the input asked
4. Let it run
5. Your MongoDB is now updated :D
