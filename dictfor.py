items = {
		"shoes":600,
		"book":400, 
		"ball":200,
		"pen":100 
}

print("Welcome to our shop. Do you wish to buy anything?")

<input type="radio" value="Yes">
<label for="yes">Yes</label><br>
<input type="radio" value="No">
<label for="no">No</label><br>

for key in items.keys():
	print(key + " = " + str(items[key]))


