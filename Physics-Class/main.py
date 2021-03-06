# Project : Calculation of some fundamnetal physical properties
# Date    : 23/05/2020

# Fahrenheit conversion to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# Celsius conversion to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

# Force Calculation
def get_force(mass, acceleration):
    return (mass * acceleration)

# Energy Calculation
def get_energy(mass, c = 3*10**8):
    return (mass * (c * c))

# Work Calculation
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return (force * distance)


f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)


train_mass = 22680
train_acceleration = 10
train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force\n")

train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters\n")


bomb_mass = 1
bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules\n")
