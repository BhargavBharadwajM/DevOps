# DevOps Internship Assignment
#Objective:
Create a script that automates the analysis and monitoring of log files
#

This document explains how to use the provided Python script (`python-script.py`) for monitoring and analyzing log files.

Prerequisites:

* Python 3 (tested with Python 3.x)
* `logging` module (usually included in standard Python installations)

Script Usage:

1. Save the script: Download or copy the `python-script.py` script to your desired location.
2. Modify the log file path:Open the script with a text editor and replace `"/home/ubuntu/python-script.py"` with the actual path to your log file.
3. Run the script:Open a terminal, navigate to the directory where you saved the script, and run the following command:

```bash
python3 log-monitor.py
```

Explanation of the Script:

* The script continuously monitors the specified log file using `tail -F`.
* It parses new log lines and keeps track of occurrences for keywords like "error," "warning," and "critical" (these keywords can be modified within the script).
* The script periodically generates summary reports (currently after processing each line) showing the number of times each keyword has been encountered.
* To stop monitoring, press `Ctrl+C` in the terminal window where the script is running.

Sample Output:

The script will display log lines in real-time along with informative messages:

```
INFO:__main__:Summary Report:
INFO:__main__:Error: 1
INFO:__main__:Summary Report:
INFO:__main__:Error: 1
INFO:__main__:Warning: 1
INFO:__main__:Summary Report:
INFO:__main__:Error: 1
INFO:__main__:Warning: 1
INFO:__main__:Critical: 1
```

Customization:

* You can modify the list of keywords within the `process_log_line` function to track entries relevant to your needs.
* The script currently generates summary reports after processing each line. You can adjust the `generate_summary_report` function call to control the report frequency (e.g., call it every minute or after a specific number of lines).

Testing:

1. Ensure you have Python 3 and the `logging` module installed.
2. Create a sample log file with various entries, including keywords like "error," "warning," and "critical."
3. Run the script with the path to your test log file.
4. Observe the output to verify that the script monitors the log file, processes lines, and generates summary reports.

This script provides a basic framework for log monitoring and analysis. You can extend it further by adding functionalities like:

* Configurable keyword or pattern matching.
* Threshold-based actions for specific keywords (e.g., sending notifications for critical errors).
* More detailed summaries (e.g., timestamps, excerpts of log lines).

By understanding the script's functionality and customization options, you can tailor it to meet your specific log analysis requirements.
