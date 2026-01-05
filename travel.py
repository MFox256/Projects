# In this project I will be making a trip planner using functions! It will be called Tripplanner v1.0

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Matt")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be travelling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

# You'll notice I change the mode of transport when I call the function. This is just to demonstrate how calling the function with a new value overrides the previous one!

destination_setup("Medway", "Norwood", estimate, "Van")
