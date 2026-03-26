name = input("Enter driver name: ")
destination = input("Enter destination: ")
dist = float(input("Enter distance (km): "))
fuel_cons = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))
litres_needed = dist * fuel_cons / 100
fuel_cost = litres_needed * fuel_price
cost_per_km = fuel_cost / dist
print("\n", 30*"=", sep="")
print("Driver :", name)
print("Destination :", destination.upper())
print("Distance :", dist, "km")
print("Fuel cost : ", fuel_cost, "KZT")
print("Category : ", end="")
if dist < 100:
    print("Short trip")
elif dist < 500:
    print("Medium trip")
else:
    print("Long trip")
print("=" * 30, "\n", "Cost breakdown:", sep="")
for i in range(100, int(dist), 100):
    print(i, "km →", cost_per_km * i, "KZT")
print(30*"=")
print("Destination uppercase :", destination.upper())
print("Destination lowercase :", destination.lower())
print("Length :", len(destination))
print("Letter 'a' count :", destination.lower().count('a'))
print(30*"=")