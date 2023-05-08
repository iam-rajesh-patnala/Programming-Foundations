# Car class should have the following attributes & methods
#
# Old Attributes:
#   color, max_speed, acceleration, tyre_friction, is_engine_started, current_speed
#
# Old Methods:
#   start_engine, stop_engine, accelerate, apply_brakes
#
# New Methods:
#   sound_horn:
#       - Print "Beep Beep" if car engine is on
#       - Print "Car has not started yet" if car engine is off
#
# When a new car is created, the engine should be off by default and current_speed should be 0


# Implement the Car class appropriately
class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction, is_engine_started=False, current_speed=0):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = is_engine_started
        self.current_speed = current_speed

    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False

    def accelerate(self):
        if self.is_engine_started:
            if self.current_speed < self.max_speed:
                self.current_speed += self.acceleration
        else:
            print("Car has not started yet")

    def apply_brakes(self):
        if self.current_speed >= self.tyre_friction:
            self.current_speed -= self.tyre_friction
        else:
            self.current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car has not started yet")


# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    car.sound_horn()  # Calling the accelerate method when the is_engine_started is False
    car.start_engine()  # Starting the engine
    car.sound_horn()  # Calling the accelerate method when the is_engine_started is True
