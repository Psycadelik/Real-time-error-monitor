#!/bin/bash

tail -F "/path/to/log/file" | grep --line-buffered -i "error" | pyp -b 'sys.path.append(""); from alert import send_alert' 'send_alert(line)'
