import flask
import serial
import threading
import time

def sendCommand(command):
    arduino.reset_input_buffer()
    message_bytes = (command + "\n").encode()
    arduino.write(message_bytes)

    response_bytes = arduino.readline()
    response = response_bytes.decode().strip()
    return response

app = flask.Flask(__name__, static_url_path='', static_folder='public')

serial_lock = threading.Lock()

@app.get('/')
def handle_naked_domain():
    return flask.redirect('/index.html')

@app.get('/api/led/<state>')
def handle_onoff_commands(state):
    response = sendCommand("LED " + state.upper())
    return response

@app.get('/api/flash/<count>/<period>')
def handle_flash_commands(count, period):
    response = sendCommand("FLASH " + count + " " + period)
    return response

print("Connecting...")
arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=20)
time.sleep(2.0)
arduino.reset_input_buffer()
print("Connected!")

app.run(host='0.0.0.0', port=8080, debug=True)
