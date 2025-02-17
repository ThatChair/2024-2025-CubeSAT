import time

from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS

from FinalProject.utils.Integrator3d import Integrator3d
from FinalProject.utils.Pos import Pos
from FinalProject.utils.misc import calculate_average


class Gyro:

    accel_offset = Pos(0, 0, 0)
    accel = Pos(0, 0, 0)
    vel = Pos(0, 0, 0)
    pos = Pos(0, 0, 0)

    vel_integrator = Integrator3d(pos, time.time())
    accel_integrator = Integrator3d(pos, time.time())

    def __init__(self, i2c):
        self.accel_gyro = LSM6DS(i2c)

    def calibrate(self):
        average_x, average_y, average_z = self.accel_gyro.acceleration
        for i in range(1000):
            accel_x, accel_y, accel_z = self.accel_gyro.acceleration
            average_x = calculate_average(average_x, accel_x, i)
            average_y = calculate_average(average_y, accel_y, i)
            average_z = calculate_average(average_z, accel_z, i)
        self.accel_offset = Pos(average_x, average_y, average_z)
        
    def reset(self):
        self.pos = Pos(0, 0, 0)
        self.vel = Pos(0, 0, 0)
        self.vel_integrator = Integrator3d(self.pos, time.time())
        self.accel_integrator = Integrator3d(self.pos, time.time())

    def update(self, current_time):
        accel_x, accel_y, accel_z = self.accel_gyro.acceleration
        accel_x -= self.accel_offset.x
        accel_y -= self.accel_offset.y
        accel_z -= self.accel_offset.z
        self.accel = Pos(accel_x, accel_y, accel_z)

        self.vel = self.accel_integrator.update(self.accel, current_time)
        self.pos = self.vel_integrator.update(self.vel, current_time)