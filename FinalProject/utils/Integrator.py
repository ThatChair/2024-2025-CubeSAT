from FinalProject.utils.Pose import Pose


class Integrator3d:
    def __init__(self, initial_pose: Pose):
        self.current_pose = initial_pose
        self.previous_pose = initial_pose

    def update(self, current_measurement: Pose) -> Pose:
        dt = current_measurement.time - self.previous_pose.time

        dist = Pose(
            0.5 * (current_measurement.x + self.previous_pose.x) * dt,
            0.5 * (current_measurement.y + self.previous_pose.y) * dt,
            0.5 * (current_measurement.z + self.previous_pose.z) * dt,
            dt
        )

        self.previous_pose = current_measurement

        self.current_pose += dist
        return self.current_pose