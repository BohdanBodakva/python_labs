import re
import time
from zipfile import ZipFile


def main():
    with ZipFile("access_log_Jul95.zip") as zip:
        zip.extractall()

    logs_file = open("access_log_Jul95", "r").read().split("\n")

    regex = re.compile('[(\d{3})(\w+)].+ - - \[(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2})'
                       ' -\d{4}\] "HEAD.+HTTP\/\d\.\d" 200 \d+')

    start_time = time.strptime("01/Jul/1995:10:49:28", "%d/%b/%Y:%H:%M:%S")
    finish_time = time.strptime("02/Jul/1995:19:35:11", "%d/%b/%Y:%H:%M:%S")

    number_of_logs = 0

    for i in logs_file:
        request_matches = re.match(regex, i)
        if request_matches:
            current_time = time.strptime(request_matches.group(1), "%d/%b/%Y:%H:%M:%S")
            if start_time <= current_time <= finish_time:
                print(request_matches.group())
                number_of_logs += 1

    print("Number = " + str(number_of_logs))


if __name__ == '__main__':
    main()

