#For this project I had to build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

#Sal’s Shippers has several different options for a customer to ship their package:

#Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
#Flat rate: $20
#2 lb or less 	$1.50 per pound
#Over 2 lb but less than or equal to 6 lb 	$3.00 per pound
#Over 6 lb but less than or equal to 10 lb 	$4.00 per pound
#Over 10 lb 	$4.75 per pound

#Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
#Flat rate : $125

#Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
#2 lb or less $4.50 per pound
#Over 2 lb but less than or equal to 6 lb $9.00 per pound
#Over 6 lb but less than or equal to 10 lb $12.00 per pound
#Over 10 lb $14.25 per pound

#Begin

weight = 4.8 
ground_cost = ""
drone_cost = ""
#Ground shipping
if weight <= 2:
  ground_cost = (1.5 * weight) + 20
elif weight <= 6:
  ground_cost = (3 * weight) + 20
elif weight <= 10:
  ground_cost = (4 * weight) + 20 
else:
  ground_cost = (4.75 * weight) + 20
ground_premium = ground_cost + 125  

#Drone shipping
if weight <= 2: 
  drone_cost = (4.50 * weight)
elif weight <= 6: 
  drone_cost = (9 * weight)
elif weight <= 10:
  drone_cost = (12 * weight)
else:
  drone_cost = (14.25 * weight) 
#Select shipping method using variables: ground_cost OR drone_cost 
#For premium ground shipping use the variable: ground_premium  
print(f"${ground_cost}")
