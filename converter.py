print("Mile to Km Converterr")
km_or_m = input("KM, Mile or Meter? ")
value = int(input("Value: "))

if km_or_m == "km":
	print(f"Mile: {value / 1.609344}")
	print(f"Meter: {value * 1000}")

elif km_or_m == "mile":
	print(f"Km: {value * 1.609344}")

elif km_or_m == "meter"
	print(f"Km: {value / 1000}")
print("Bye")
