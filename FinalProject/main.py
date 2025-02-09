import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS
from adafruit_lis3mdl import LIS3MDL

from FinalProject.utils.Integrator3d import Integrator3d
from FinalProject.utils.Pos import Pos

#imu and camera initialization
i2c = board.I2C()
accel_gyro = LSM6DS(i2c)
mag = LIS3MDL(i2c)

pos = Pos(0.0, 0.0, 0.0, time.time())
vel_integrator = Integrator3d(pos)
accel_integrator = Integrator3d(pos)

def update_pose():
    accelx, accely, accelz = accel_gyro.acceleration
    accel = Pos(accelx, accely, accelz, time.time())

    vel = accel_integrator.update(accel)
    return vel_integrator.update(vel)

def main():
    while True:
        pos = update_pose()
        print(pos)


if __name__ == '__main__':
    main()
