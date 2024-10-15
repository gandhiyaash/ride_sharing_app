class Rider:
    def __init__(self, name):
        self.name = name
        self.ride_count = 0
        self.is_preferred = False
        self.active_ride = []

    def update_ride_count(self):
        self.ride_count += 1
        if self.ride_count > 10:
            self.is_preferred= True
    
    def __repr__(self):
        return f"Rider(name={self.name}, rides={self.ride_count}, preferred={self.is_preferred})"