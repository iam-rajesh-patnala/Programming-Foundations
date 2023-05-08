# Car class should have the following attributes & methods
#
# Old Attributes:
#   color, max_speed, acceleration, tyre_friction, is_engine_started, current_speed
#
# Old Methods:
#   start_engine, stop_engine, accelerate
#
# New Methods
#   apply_brakes:
#       - decrease the current_speed value according to the tyre_friction value
#       - current_speed should never go below 0
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


# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    car.start_engine()
    car.accelerate()  # Calling the accelerate method when the is_engine_started is True
    print(car.current_speed)  # 10
    car.apply_brakes()  # Calling the apply_brakes method
    # current_speed of the car should decrease according to the tyre_friction value.
    print(car.current_speed)  # (10 - 3 => 7)
    car.apply_brakes()
    print(car.current_speed)  # 7 - 3 => 4
    car.apply_brakes()
    print(car.current_speed)  # 4 - 3 => 1
    car.apply_brakes()
    print(car.current_speed)  # 1 - 3 => 0 (current_speed should never go behind 0.)
