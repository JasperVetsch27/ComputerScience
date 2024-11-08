# Dictionary is a tppe of collection like lsit
# A list is a collection of items in a squence 
# A dictionary is different
# Dictionaries store data in key-value pairs 
# Yuo can retreive data quickly by using a unique key
# Instead of retreving it by index (position)

# Example
# Lists use brakcets, dictionaries use braces 
Jasper = {
    "name": "Jasper",
    "age": 15, 
    "city": "Albertville",
    "pets": 2,
    "sibling": 1
}
# Each key must be unique

# Rereiving value from a dictionary

# .get allows you to retreive a value without erroring
# When th ekey doesn't exist
# The second parameter is what is given if the value is not found
print(Jasper["age"])
print(Jasper.get("sibling"))
print(Jasper.get("weight", "Not Found"))

# You can add value to a dicionary 

Jasper["country"] = "USA"

#You can modify values

Jasper["age"] = 16

print(Jasper)

# Remove entries

Jasper.pop("pets")

print(Jasper)

# Iterate through a dictionary using a for loop

for key, value in Jasper.items():
    print(key + " " + str(value))

# Dicionary functions
print(Jasper.keys()) # Returns all keys
print(Jasper.value()) # Returns all value
print(Jasper.items()) # Returns all pairs 
print(Jasper.clear()) # Clear all items 
