
km_or_m = input("KM or Mile? ")
value = int(input("Value: "))

if km_or_m == "km":
	print(f"Mile: {value / 1.609344}")
	print(f"Meter: {value * 1000}")

elif km_or_m == "mile":
	print(f"Km: {value * 1.609344}")

