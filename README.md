# Create a Real-time error alert system using the Vonage Messages APIkey

## To setup this project

Project tree:

```
├── alert.py
├── LICENSE
├── README.md
├── requirements.txt
└── send_alert.sh
```

1. Clone this project and cd into project directory:
```
git clone git@github.com:Psycadelik/Real-time-error-monitor.git && cd Real-time-error-monitor
```

2. create .env file from the sample provided and replace the fields with your credentials from the Vonage developer dashboard:
```
# Vonage Credentials
VONAGE_API_KEY=XXXXXX
VONAGE_API_SECRET=XXXXXX
VONAGE_SENDER=XXXX
RECIPIENT=XXXXX

```

3. Create a Python virtual environment:  `python3 -m venv .venv && source .venv/bin/activate`

4. Install the dependecies: `pip3 install -r requirements.txt`

5. Run the command on a terminal:
```
tail -F "/path/to/log/file" | grep --line-buffered -i "error" | <project_dir>/.venv/bin/activate >pyp -b 'sys.path.append(""); from alert import send_alert' 'send_alert(line)'
```

**Note**:
supply an error log file in the command: `tail -F "/path/to/log/file"`.
For example, we have an error log file in our `/tmp` folder: `application.log`.

Run the command as follows:
```
tail -F "/tmp/application.log" | grep --line-buffered -i "error" | <project_folder>/.venv/bin/activate >pyp -b 'sys.path.append(""); from alert import send_alert' 'send_alert(line)'
```
