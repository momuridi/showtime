import showtime.timeutils.timetool as timetool
import time
from sys import stdout


def main():
    while True:
        print(timetool.environment_time_now())
        time.sleep(1)
        stdout.flush()

if __name__ == '__main__':
    main()