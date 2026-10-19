import gpiozero as gz
import time
import signal

def basic_on_off():
    print("Basic On / Off")
    green_led = gz.DigitalOutputDevice(18)
    green_led.on()
    time.sleep(3)
    green_led.off()

def fancy_leds():
    print("Fancy LEDs")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    #green_led.on()
    #time.sleep(3)
    #green_led.off()

    #yellow_led.blink(on_time=2, off_time=0.1, n=3, background=False)

    yellow_led.blink(on_time=0.5, off_time=1.5)
    signal.pause()

def led_board():
    print("LED Board")
    led_board = gz.LEDBoard(red=14, yellow=15, green=18, pwm=True)

    led_board.on()
    time.sleep(1)

    led_board.off()
    time.sleep(1)

    led_board.red.on()
    led_board.green.on()
    time.sleep(1)

    led_board.red.off()
    led_board.green.off()
    time.sleep(1)

    led_board.yellow.value = 0.5
    time.sleep(1)

    led_board.yellow.off()


def main():
    print("LEDs")
    led_board()

main()
