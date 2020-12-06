# I LIKE TRAINS
train_mass = 22680
train_acceleration = 10
train_distance = 100

def get_force(mass, acceleration):
  return mass * acceleration
get_force(train_mass, train_acceleration)
train_force = get_force(train_mass, train_acceleration)
train_force1 = "{:,}".format(train_force)
print("The GE train supplies " + str(train_force1) + " Newtons of force.")
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force
train_work = get_work(train_mass, train_acceleration, train_distance)
train_work1 = "{:,}".format(train_work)
print("The GE train does " + str(train_work1) + " Joules of work over " + str(train_distance) + " meters.")

# INRGEE
bomb_mass = 1
c = 3*10**8
def get_energy(mass, c):
  return mass * c
bomb_energy = get_energy(bomb_mass, c)
bomb_energy1 = "{:,}".format(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy1) + " Joules.")

# THE AURA THAT MY SKIN FEELS
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = round(f_to_c(100), 1)
print("It's " + str(f100_in_celsius) + " degrees in celsius.")

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) +32
  return f_temp
c0_in_fahrenheit = round(c_to_f(0), 1)
print("It's " + str(c0_in_fahrenheit) + " degrees in fahrenheit.")