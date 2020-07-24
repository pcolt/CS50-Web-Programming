def announce(f):
	def wrapper():
		print("About to run the function...")
		f()
		print("Done with the funcntion.")
	return wrapper

@announce
def hello():
	print("Hello, world")

def hello2():
	print("Hi there!")

print("1")
hello()

print("2")
announce(hello2())
