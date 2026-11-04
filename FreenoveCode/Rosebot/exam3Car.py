from rosebot import Rosebot
import mqtt_helper as mh
import gpiozero as gz
import time
import signal

class App:
    
    def __init__(self):
        self.robot = Rosebot()

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/fulksdm/#",
                                publish_topic_name="me435/fulksdm/to_computer",
                                use_off_campus_broker=False)
        self.mqtt_client.callback = self.mqtt_callback

    def mqtt_callback(self, message_type, message_payload):
        print("Recieved type: ", message_type)
        print("Recieved payload: ", message_payload)

        if message_type == "left":
            if message_payload[0] == 1:
                self.robot.drive_system.set_speeds(message_payload[2], message_payload[2], 0, 0)
            else:
                self.robot.drive_system.set_speeds(-message_payload[2], -message_payload[2], 0, 0)
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()

        if message_type == "right":
            if message_payload[0] == 1:
                self.robot.drive_system.set_speeds(0, 0, message_payload[2], message_payload[2])
            else:
                self.robot.drive_system.set_speeds(0, 0, -message_payload[2], -message_payload[2])
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()

        if message_type == "both":
            if message_payload[0] == 1:
                self.robot.drive_system.set_speeds(message_payload[2], message_payload[2], message_payload[3], message_payload[3])
            else:
                self.robot.drive_system.set_speeds(-message_payload[2], -message_payload[2], -message_payload[3], -message_payload[3])
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()
  

def main():
    print("Rosebot MQTT")
    app = App()

    try:
        while True:
            app.mqtt_client.send_message("ultra", round(app.robot.ultrasonic.get_cm()))
            time.sleep(2)
    except KeyboardInterrupt:
        print("Goodbye")
        app.robot.drive_system.stop()
        app.mqtt_client.close()

main()