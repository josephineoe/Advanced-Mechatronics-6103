from machine import Pin, I2C
import time

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)
print("Detected I2C devices:", [hex(addr) for addr in i2c.scan()])

# Initialize sensors
def init_sensors():
    # Accelerometer (0x19)
    i2c.writeto_mem(0x19, 0x20, bytes([0x57]))  # 100Hz, XYZ enabled
    
    # Magnetometer (0x1e)
    i2c.writeto_mem(0x1e, 0x02, bytes([0x00]))  # Continuous mode
    
    # Gyroscope (try both possible addresses)
    try:
        i2c.writeto_mem(0x6b, 0x20, bytes([0x0F]))  # 95Hz, XYZ enabled
        gyro_addr = 0x6b
    except OSError:
        i2c.writeto_mem(0x69, 0x20, bytes([0x0F]))
        gyro_addr = 0x69
    return gyro_addr

gyro_address = init_sensors()

# Sensor reading functions
def read_accel():
    data = i2c.readfrom_mem(0x19, 0x28 | 0x80, 6)
    x = (data[1] << 8) | data[0]
    y = (data[3] << 8) | data[2]
    z = (data[5] << 8) | data[4]
    return (x/16384.0, y/16384.0, z/16384.0)  # Scale to g (±2g range)

def read_mag():
    data = i2c.readfrom_mem(0x1e, 0x03 | 0x80, 6)
    x = (data[0] << 8) | data[1]
    y = (data[2] << 8) | data[3]
    z = (data[4] << 8) | data[5]
    return (x/32768.0*4.0, y/32768.0*4.0, z/32768.0*4.0)  # Scale to Gauss

def read_gyro():
    data = i2c.readfrom_mem(gyro_address, 0x28 | 0x80, 6)
    x = (data[1] << 8) | data[0]
    y = (data[3] << 8) | data[2]
    z = (data[5] << 8) | data[4]
    return (x*0.07, y*0.07, z*0.07)  # Scale to °/s (±2000dps range)

# Main loop
while True:
    print("\nAccel (g):", read_accel())
    print("Mag (G):", read_mag())
    print("Gyro (°/s):", read_gyro())
    time.sleep(1)