name = input("Enter driver name: ")
dist = float(input("Enter distance (km): "))
fuel_cons = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))
litres_needed = dist * fuel_cons / 100
fuel_cost = litres_needed * fuel_price
cost_per_km = fuel_cost / dist
print("=" * 30, "\n" , " " * 6, "ROAD TRIP SUMMARY", "\n" , "=" * 30, sep = "")
print("Driver :", name)
print("Distance :", dist, "km")
print("Consumption :", fuel_cons, "L/100km")
print("Fuel price :", fuel_price, "KZT/L",)
print("-" * 30)
print("Litres needed:", litres_needed, "L")
print("Fuel cost : ", fuel_cost, "KZT")
print("Cost per km :", cost_per_km, "KZT")
print("=" * 30)