#!/usr/bin/python3
"""
This module contains the function that displays the
stats from the standard input
"""
import sys
import re

def initialize_log():
  """
  This function initializes a log dictionary with keys for file size
  and a dictionary of HTTP status codes. The initial values are set
  to 0, and the function 
  """
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    log = {"file_size": 0, "code_list": {str(code): 0 for code in status_codes}}
    print(f"{log = }")
    return log

def parse_line(line, regex, log):
  """
  This function takes a log line, a regular expression (regex), and the
  current log dictionary as input. It attempts to match the log line using the regular
  expression and updates the log with relevant information such as file size and HTTP status
  codes.
  """
    match = regex.fullmatch(line)

    if match:
        stat_code, file_size = match.group(1, 2)
        log["file_size"] += int(file_size)
        if stat_code.isdecimal():
            log["code_list"][stat_code] += 1
    return log

def print_codes(log):
  """
  This function takes the log dictionary as input and prints the file size and
  counts of each HTTP status code that occurred in the log. It sorts the status
  codes before printing for better readability.
  """
    print("File size: {}".format(log["file_size"]))

    sorted_code_list = sorted(log["code_list"])
    for code in sorted_code_list:
        if log["code_list"][code]:
            print(f"{code}: {log['code_list'][code]}")

def main():
  """
  The main function of the script. It initializes a regular expression
  for parsing log lines, initializes the log, and then reads log lines from
  standard input. It calls the parse_line function to update the log for
  every log line and prints log statistics every 10 lines.
  """
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    log = initialize_log()
    line_count = 0

    for line in sys.stdin:
        line = line.strip()
        line_count += 1
        log = parse_line(line, regex, log)

        if line_count % 10 == 0:
            print_codes(log)

if __name__ == "__main__":
    main()
    initialize_log()

