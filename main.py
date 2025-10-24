from machine import Pin, I2C
import time
import struct
import math
import sys

MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

# Initialize I2C
i2c = I2C(1, scl=Pin(27), sda=Pin(26), freq=400000)

# Wake up MPU6050
i2c.writeto_mem(MPU6050_ADDR, PWR_MGMT_1, b'\x00')
time.sleep(0.1)

def read_raw_data(addr):
    high, low = i2c.readfrom_mem(MPU6050_ADDR, addr, 2)
    value = (high << 8) | low
    if value > 32768:
        value -= 65536
    return value

while True:
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_XOUT_H + 2)
    acc_z = read_raw_data(ACCEL_XOUT_H + 4)

    gyro_x = read_raw_data(0x43)
    gyro_y = read_raw_data(0x45)
    gyro_z = read_raw_data(0x47)

    Ax = acc_x / 16384.0
    Ay = acc_y / 16384.0
    Az = acc_z / 16384.0

    Gx = gyro_x / 131.0
    Gy = gyro_y / 131.0
    Gz = gyro_z / 131.0
    if Ay > 1 :
        Ay =1
    elif Ay < -1 :
        Ay = -1
    else:
        Ay = Ay
    angle = math.acos(Ay)
    angle_deg = (angle * 180)/math.pi
    roll = roll  = math.atan2(Ay, Az) * 180 / math.pi
    
    print(roll)

