from FinalProject.utils.Pos import Pos


class Integrator3d:

    def __init__(self, initial_pose: Pos, initial_time: float):
        self.current_pose = initial_pose
        self.previous_pose = initial_pose
        self.previous_time = initial_time
        self.time = initial_time

    def update(self, current_measurement: Pos, current_time: float) -> Pos:
        self.time = current_time
        dt = self.time - self.previous_time

        dist = Pos(
            0.5 * (current_measurement.x + self.previous_pose.x) * dt,
            0.5 * (current_measurement.y + self.previous_pose.y) * dt,
            0.5 * (current_measurement.z + self.previous_pose.z) * dt,
        )

        self.previous_pose = current_measurement
        self.previous_time = self.time

        self.current_pose += dist
        return self.current_pose