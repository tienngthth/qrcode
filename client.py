import cv2
import socketio #python-socketio by @miguelgrinberg
import base64

class SocketClient():
    sio = socketio.Client()

    @staticmethod
    def connect():
        SocketClient.sio.connect('http://localhost:3000')

    @staticmethod   
    def emit_image(frame):
        res, frame = cv2.imencode('.jpg', frame)                        # from image to binary buffer
        encoded_data = base64.b64encode(frame).decode()                 # convert to base64 format
        image_src = 'data:image/png;base64,' 
        SocketClient.emit_string('image', image_src + encoded_data)                  # send to server

    @staticmethod   
    def emit_string(channel, data):
        SocketClient.sio.emit(channel, data)    # send to server

    @staticmethod
    def disconnect():
        SocketClient.sio.disconnect()

  