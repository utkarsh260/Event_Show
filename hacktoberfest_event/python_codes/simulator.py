import random 
import numpy as np
import simpy

NUM_EMPLOYEES = 2
AVERAGE_SUPPORT_TIME = 5
CUSTOMER_INTERVAL = 1

SIM_TIME= 120

customer_handled = 0

class CallCentre:
    
    def __init__(self, env, num_employess, support_time):
        self.env = env
        self.staff = simpy.Resource(env, num_employess)
        self.support_time = support_time

    def support(self, customer):
        random_time = max(1, np.random.normal(self.support_time, 4)) 
        #use max to avoid negative values and 4 is standard deviation
        yield self.env.timeout(random_time)
        print(f"support finished for {customer} at {self.env.now:.2f}")

def customer(env, name, call_centre):
    global customer_handled
    print(f"customer {name} entres waiting queue at {env.now:.2f}")
    with call_centre.staff.request() as request:
        yield request
        print(f"customer {name} entres call at {env.now:.2f}")
        yield env.process(call_centre.support(name))
        print(f"Customer {name} left call at {env.now:.2f}")

        customer_handled +=1

def setup(env, num_employees, support_time, customer_interval):
    call_centre = CallCentre(env, num_employees, support_time)

    for i in range(1, 6):
        env.process(customer(env, i, call_centre))
    
    while True:
        yield env.timeout(random.randint(customer_interval -1, customer_interval +1))
        i+=1
        env.process(customer(env, i, call_centre))

print("starting Calling CallCentre Simulation...")
env= simpy.Environment()
env.process(setup(env, NUM_EMPLOYEES, AVERAGE_SUPPORT_TIME, CUSTOMER_INTERVAL))
env.run(until= SIM_TIME)

print("Customers handled:", str(customer_handled))