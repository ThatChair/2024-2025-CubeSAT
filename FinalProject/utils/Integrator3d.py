from FinalProject.utils.Pos import Pos


class Integrator3d:
    def __init__(self, initial_pose: Pos):
        self.current_pose = initial_pose
        self.previous_pose = initial_pose

    def update(self, current_measurement: Pos) -> Pos:
        dt = current_measurement.time - self.previous_pose.time

        dist = Pos(
            0.5 * (current_measurement.x + self.previous_pose.x) * dt,
            0.5 * (current_measurement.y + self.previous_pose.y) * dt,
            0.5 * (current_measurement.z + self.previous_pose.z) * dt,
            dt
        )

        self.previous_pose = current_measurement

        self.current_pose += dist
        return self.current_pose