# OOPs program


class Robot:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

    def charge(self):
        remain_battery = 10
        self.battery_level += remain_battery
        print(f"{self.name} is now at {self.battery_level}% battery some changes")


my_robot = Robot("Sparky", 50)
my_robot.charge()
