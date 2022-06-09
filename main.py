import re
import time
from zipfile import ZipFile


def main():
    with ZipFile("access_log_Jul95.zip") as zip:
        zip.extractall()

    logs_file = open("access_log_Jul95", "r")
    logs_list = logs_file.read().split("\n")

    regex = re.compile('[(\d{3})(\w+)].+ - - \[(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2})'
                       ' -\d{4}\] "HEAD.+HTTP\/\d\.\d" 200 \d+')

    start = time.strptime("01/Jul/1995:10:49:28", "%d/%b/%Y:%H:%M:%S")
    finish = time.strptime("02/Jul/1995:19:35:11", "%d/%b/%Y:%H:%M:%S")

    s = 0
    for i in logs_list:
        request_matches = re.match(regex, i)
        if request_matches:
            current = time.strptime(request_matches.group(1), "%d/%b/%Y:%H:%M:%S")
            if start <= current <= finish:
                print(request_matches.group())
                s += 1

    print(s)


if __name__ == '__main__':
    main()
















# '[(\d{3})(\w+)].+ - - \[(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}) -\d{4}\] "HEAD.+HTTP\/\d\.\d" 200 \d+'
