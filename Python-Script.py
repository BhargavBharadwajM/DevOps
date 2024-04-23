import logging
import time
import subprocess
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def monitor_log_file(log_file_path):
    try:
        # Continuously monitor the log file
        process = subprocess.Popen(['tail', '-F', log_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        keyword_counts = defaultdict(int)  # Store counts of keywords
        while True:
            # Read new log lines in real-time
            line = process.stdout.readline()
            if line:
                # Process the new log line
                process_log_line(line.decode().strip(), keyword_counts)
                # Generate summary report (e.g., top errors)
                generate_summary_report(keyword_counts)
    except KeyboardInterrupt:
        logger.info("Monitoring stopped.")

def process_log_line(log_line, keyword_counts):
    # Analyze the log line and update keyword counts
    logger.debug("Processing log line: %s", log_line)
    keywords = ["error", "warning", "critical"]  # Example keywords to search for
    for keyword in keywords:
        if keyword in log_line.lower():
            keyword_counts[keyword] += 1

def generate_summary_report(keyword_counts):
    # Generate summary report (e.g., top errors)
    logger.info("Summary Report:")
    for keyword, count in keyword_counts.items():
        logger.info("%s: %d", keyword.capitalize(), count)

if __name__ == "__main__":
    log_file_path = "/home/ubuntu/testlog.txt"
    monitor_log_file(log_file_path)
