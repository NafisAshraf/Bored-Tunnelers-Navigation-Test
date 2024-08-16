import random
import time
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*") 

def send_data():
    while True:
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        print(f'Emitting: x={x}, y={y}, z={z}')
        socketio.emit('new_number', {'x': x, 'y': y, 'z': z})
        time.sleep(1)

def send_burst_data():
    while True:
        for _ in range(100):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            z = random.randint(0, 100)
            print(f'Emitting: x={x}, y={y}, z={z}')
            socketio.emit('new_number', {'x': x, 'y': y, 'z': z})
            time.sleep(0.01)
        time.sleep(5)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.start_background_task(send_burst_data)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)




# from flask import Flask
# from flask_socketio import SocketIO
# import random
# import time

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hhhhh'
# socketio = SocketIO(app, cors_allowed_origins="*")

# def send_data():
#     while True:
#         # Simulate a burst of data
#         # for _ in range(100):  # Adjust the range for the number of data points you want to send in the burst
#         x = random.randint(0, 100)
#         y = random.randint(0, 100)
#         z = random.randint(0, 100)
#         print(f'Emitting: x={x}, y={y}, z={z}')  # Debug log
#         socketio.emit('new_number', {'x': x, 'y': y, 'z': z})
#             # time.sleep(0.01)  # Short sleep to simulate rapid data sending
#         time.sleep(1)  # Longer sleep between bursts

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')
#     send_data()

# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')

# if __name__ == '__main__':
#     socketio.run(app, host='0.0.0.0', port=5000, debug=True)