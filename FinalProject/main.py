import time
import board
from adafruit_lis3mdl import LIS3MDL
from FinalProject.utils.Gyro import Gyro
from FinalProject.utils.Integrator3d import Integrator3d
from FinalProject.utils.Pos import Pos
from FinalProject.utils.misc import *

#imu and camera initialization
i2c = board.I2C()
mag = LIS3MDL(i2c)
gyro = Gyro(i2c)

#bluetooth receiving initialization
start_receiving("/home/pi/Documents/Backbranch/2024-2025-CubeSAT/FinalProject/uplinked_files")

def main():
    gyro.calibrate()
    gyro.reset()
    while True:
        gyro.update(time.time())
        print(gyro.pos)


if __name__ == '__main__':
    main()
