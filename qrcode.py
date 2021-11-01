import cv2
from code import Code
from camera import Camera

def validate_code(code, found_codes):
	if code not in found_codes:
		found_codes.add(code)
		print(code)

def start_scanning():
	Camera.start_camera()
	# barcodes found thus far
	found_codes = set()
	while True:
		code = Camera.scan_code()
		if code is not None:
			validate_code(code.decoded_content, found_codes)
		# if the `q` key was pressed, break from the loop
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break
	Camera.stop_camera()

if __name__ == "__main__": 
    start_scanning()