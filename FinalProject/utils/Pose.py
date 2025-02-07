class Pose:
    def __init__(self, x, y, z, time):
        self.x = x
        self.y = y
        self.z = z
        self.time = time

    def __add__(self, other):
        return Pose(self.x + other.x, self.y + other.y, self.z + other.z, self.time + other.time)

    def __sub__(self, other):
        return Pose(self.x - other.x, self.y - other.y, self.z - other.z, self.time - other.time)