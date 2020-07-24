class Point():
	def __init__(self, input1, input2):
		self.x = input1
		self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)

class Flight():
	def __init__(self, capacity):
		self.capacity = capacity
		self.passengers = []
	def add_passenger(self, name):
		if not self.open_seats():
			return False
		self.passengers.append(name)
		return True
	def open_seats(self):
		return self.capacity - len(self.passengers)

flight = Flight(3)
flight.add_passenger("Pablo")
flight.add_passenger("Rosi")
print(flight.passengers)
flight.add_passenger("Bruno")
flight.add_passenger("Iacopo")
print(flight.passengers)

flight2 = Flight(3)
people = ["Carmen", "Carlos", "Carla", "Sofia"]
for person in people:
	success = flight2.add_passenger(person)
	if success:
		print(f"Added {person} to flight successfully.")
	else:
		print(f"No available seats for {person}")
