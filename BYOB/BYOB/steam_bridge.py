import json
import socket
import time
import pygame

HOST = "127.0.0.1"
PORT = 5005

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    raise RuntimeError(
        "No gamepad detected. Check Steam Input and reconnect the controller."
    )

pad = pygame.joystick.Joystick(0)
pad.init()

print("Controller:", pad.get_name())
print("Axes:", pad.get_numaxes())
print("Buttons:", pad.get_numbuttons())
print("Waiting for MATLAB...")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

try:
    conn, address = server.accept()
    print("MATLAB connected:", address)

    with conn:
        while True:
            pygame.event.pump()

            axes = [
                round(pad.get_axis(i), 4)
                for i in range(pad.get_numaxes())
            ]
            buttons = [
                pad.get_button(i)
                for i in range(pad.get_numbuttons())
            ]

            packet = {
                "axes": axes,
                "buttons": buttons
            }

            conn.sendall(
                (json.dumps(packet) + "\n").encode("utf-8")
            )
            time.sleep(0.02)
            
            # print(axes)
            # print(buttons)

except (BrokenPipeError, ConnectionResetError):
    print("MATLAB disconnected.")

finally:
    server.close()
    pygame.quit()