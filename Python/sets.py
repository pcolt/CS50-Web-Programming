# Create an enpty set
s = set()

# Add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(3)
print(s)  # {1,2,3}

s.remove(3)
print(s)  # {1,2}

print(f"The set has {len(s)} elements")
