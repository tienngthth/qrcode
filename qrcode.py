import cv2
from code import Code
from camera import Camera
import socketio #python-socketio by @miguelgrinberg
import base64
from client import SocketClient
import time

def validate_code(code, found_codes):
	if code not in found_codes:
		found_codes.add(code)
		SocketClient.emit_string("result", code)
		time.sleep(0.5)
		SocketClient.disconnect() 
		return False

def start_scanning():
	SocketClient.connect()
	Camera.start_camera()
	found_codes = set()
	while True:
		code = Camera.scan_code()
		if code is not None:
			validate_code(code.decoded_content, found_codes)
			break
		# if the `q` key was pressed, break from the loop
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break
	Camera.stop_camera()

if __name__ == "__main__": 
    start_scanning()