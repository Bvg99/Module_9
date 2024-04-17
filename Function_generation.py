speed = 100
change = 5
distance = 1000

#Фабрика функций:

def rocket_velocity(fuel):
    if fuel == "+":
        def acceleration(speed, change):
            return speed + change
        return acceleration
    elif fuel == "-":
        def slowdown(speed, change):
            return speed - change
        return slowdown

speed_up_or_down = rocket_velocity("+")
current_speed = (speed_up_or_down(speed, change))
print('current_speed: ', current_speed)


#Пример лямбда функции с аналогом через def

time = lambda distance, current_speed: distance / current_speed
print('time: ', time(distance, current_speed))

def time_def(distance, current_speed):
    return distance / current_speed
print('time_def: ', time_def(distance, current_speed))


#Пример создания вызываемого объекта

class RentPrice:
   def __init__(self, time):
       self.time = time
   def __call__(self, cost_of_rent):
       return self.time * cost_of_rent

rent_time = RentPrice(9.52)
print('rent price: ', rent_time(2))