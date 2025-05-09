import network
import time
import socket
from machine import Pin, I2C
import math
from mpu9250 import MPU9250

# Initialize sensor
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
sensor = MPU9250(i2c)

# Sensor processing
RAD_TO_DEG = 57.295779513
FILTER_ALPHA = 0.1
f_phi = f_theta = 0.0  # Roll/Pitch

def manual_json_dumps(data):
    """Manual JSON implementation that works without any modules"""
    return ('{"roll":%.2f,"pitch":%.2f,"timestamp":%d}' % 
           (data['roll'], data['pitch'], data['timestamp']))

def get_orientation():
    global f_phi, f_theta
    ax, ay, az = sensor.acceleration
    gx, gy, gz = sensor.gyro
    
    a_phi = math.atan2(ay, az)
    a_theta = math.atan2(-ax, math.sqrt(ay**2 + az**2))
    
    f_phi = FILTER_ALPHA * (f_phi + gx * 0.001) + (1 - FILTER_ALPHA) * a_phi
    f_theta = FILTER_ALPHA * (f_theta + gy * 0.001) + (1 - FILTER_ALPHA) * a_theta
    
    return {
        'roll': round(f_phi * RAD_TO_DEG, 2),
        'pitch': round(f_theta * RAD_TO_DEG, 2),
        'timestamp': time.ticks_ms()
    }

def start_server():
    ap = network.WLAN(network.AP_IF)
    ap.config(essid='PicoOrientation', password='pico1234')
    ap.active(True)
    ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(1)
    
    print('AP Mode Active')
    print('SSID: PicoOrientation')
    print('IP: 192.168.4.1')
    print('Endpoint: /orientation (GET)')
    
    while True:
        conn, addr = s.accept()
        request = conn.recv(1024).decode()
        
        if 'GET /orientation' in request:
            data = get_orientation()
            json_data = manual_json_dumps(data)
            
            conn.send('HTTP/1.1 200 OK\r\n')
            conn.send('Content-Type: application/json\r\n')
            conn.send('Access-Control-Allow-Origin: *\r\n')
            conn.send('Connection: close\r\n\r\n')
            conn.send(json_data)
        
        conn.close()

start_server()