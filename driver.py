class Driver:
    def __init__(self, name):
        self.name = name
        self.active_rides = []

    def __repr__(self):
        return f"Driver(name={self.name})"
