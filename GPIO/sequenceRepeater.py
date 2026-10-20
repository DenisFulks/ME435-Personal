import gpiozero as gz
import time
import signal

delay = 0.5
sequence = []
leds = gz.LEDBoard(14, 15, 18)

def repeatSequence(sequence):
    print(sequence)

    for i in range(len(sequence)):
        if sequence[i] == "red":
            redLEDOn()
            time.sleep(delay)
            LEDsOff()
            time.sleep(delay)
        elif sequence[i] == "yellow":
            yellowLEDOn()
            time.sleep(delay)
            LEDsOff()
            time.sleep(delay)
        elif sequence[i] == "green":
            greenLEDOn()
            time.sleep(delay)
            LEDsOff()
            time.sleep(delay)
    print("Sequence Done!")

    sequence.clear()

def redLEDOn(sequence = []):
    print("Red On")
    leds.value = (1, 0, 0)
    sequence.append("red")

def yellowLEDOn(sequence = []):
    print("Yellow On")
    leds.value = (0, 1, 0)
    sequence.append("yellow")

def greenLEDOn(sequence = []):
    print("Green On")
    leds.value = (0, 0, 1)
    sequence.append("green")

def LEDsOff():
    leds.off()

def main():
    repeatButton = gz.Button(25)
    
    redButton = gz.Button(22)
    yellowButton = gz.Button(23)
    greenButton = gz.Button(24)

    repeatButton.when_pressed = lambda: repeatSequence(sequence)

    redButton.when_pressed = lambda: redLEDOn(sequence)
    redButton.when_released = LEDsOff

    yellowButton.when_pressed = lambda: yellowLEDOn(sequence)
    yellowButton.when_released = LEDsOff

    greenButton.when_pressed = lambda: greenLEDOn(sequence)
    greenButton.when_released = LEDsOff

    signal.pause()

main()