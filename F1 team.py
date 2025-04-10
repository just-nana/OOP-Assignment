class F1TEAM:
    def __init__(self,name,principal,drivers,engine_supplier):
        self.name = name
        self._principal = principal
        self._drivers = drivers
        self._engine_supplier = engine_supplier
        self._points = 0

    def add_points(self, points):
        if points > 0:
            self._points += points
            print(f"{self.name} gains {points} points. Total: {self._points}")
        else:
            print("Points must be positive")

    def change_driver(self, out_driver, in_driver):
        if out_driver in self.drivers:
            index = self._drivers.index(out_driver)
            self.drivers[index] = in_driver
            print(f"{self.name} replaced {out_driver} with {in_driver}")
        else:
            print(f"{out_driver} is not a driver for {self.name}")

    def team_info(self):
        return f"""
        Team: {self.name}
        Principal: {self._principal}
        Drivers: {','.join(self.drivers)}
        Engine: {self.engine_supplier}
        Points: {self._points}
        """

    def get_points(self):
        return self._points

    def set_principal(self, new_principal):
        self._principal = new_principal

class TopTeam(F1TEAM):
    def __init__(self, name, principal, drivers, engine_supplier, budget):
        super().__init__(name, principal, drivers, engine_supplier)
        self.budget = budget  # In millions

    def upgrade_facilities(self):
        if self.budget > 50:
            self.budget -= 50
            print(f"{self.name} has upgraded facilities! Budget remaining: ${self.budget}M")
        else:
            print(f"{self.name} does not have enough budget to upgrade.")
    
    # Polymorphism: override team_info
    def team_info(self):
        base_info = super().team_info()
        return base_info + f"\n        Budget: ${self.budget}M"
    
class MidfieldTeam(F1TEAM):
    def __init__(self, name, principal, drivers, engine_supplier, sponsor):
        super().__init__(name, principal, drivers, engine_supplier)
        self.sponsor = sponsor

    def attract_sponsor(self, new_sponsor):
        print(f"{self.name} has attracted a new sponsor: {new_sponsor}!")
        self.sponsor = new_sponsor
    
    def team_info(self):
        base_info = super().team_info()
        return base_info + f"\n        Sponsor: {self.sponsor}"

# Assignment 2
# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing across the water 🚢")

# Subclass: Train
class Train(Vehicle):
    def move(self):
        print("Rumbling along the tracks 🚆")

# Function that accepts any vehicle and moves it
def travel(vehicle: Vehicle):
    vehicle.move()

# Example usage
if __name__ == "__main__":
    my_vehicles = [Car(), Plane(), Boat(), Train()]

    for v in my_vehicles:
        travel(v)
