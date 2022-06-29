vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford fiesta Ghia 1.4',
    }

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombarider Learjet 75"
vehicles["toy"] = "glider"
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
result = vehicles.pop("f1", "Yeah, bpy!!!")
print(result)
print()
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)

for key, values in vehicles.items():
    print(key, values, sep=", ")
    
    

    
