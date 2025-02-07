from FinalProject.utils.Pose import Pose


class Integrator3d():
    def __init__(self, initial_pose: Pose):
        self.previous_pose = initial_pose

    def update(self, current_pose: Pose) -> Pose:
        dt = current_pose.time - self.previous_pose.time

        dist = Pose(
            0.5 * (current_pose.x + self.previous_pose.x) * dt,
            0.5 * (current_pose.y + self.previous_pose.y) * dt,
            0.5 * (current_pose.z + self.previous_pose.z) * dt,
            current_pose.time
        )

        self.previous_pose = current_pose

        return dist