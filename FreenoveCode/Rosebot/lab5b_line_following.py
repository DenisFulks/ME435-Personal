from rosebot import Rosebot
import time

def main():
    print("Lab 5b Line Following")
    robot = Rosebot()

    try:
        while True:
            print(robot.ultrasonic.get_cm())
            print(robot.line_sensors.get_line_word())

            time.sleep(1)

    except KeyboardInterrupt:
        # Handle Ctrl-C to exit the program
        robot.drive_system.stop()
        print("Goodbye!")

main()