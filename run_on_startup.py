import datetime
import sys
from display_colours import display_dawn_sigmoid
from time import sleep


def run_on_startup(dawn_min):
    while True:
        just_now = datetime.datetime.now()

        if just_now.hour == 7 and just_now.minute == 30:
            display_dawn_sigmoid(dawn_min)

        sleep(5)  # Carry on round and check again later


if __name__ == "__main__":
    dawn_duration_min = float(sys.argv[1])

    run_on_startup()