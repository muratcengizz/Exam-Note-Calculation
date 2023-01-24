class midTermFinal():
	def __init__(self):
		self.midtermNote = float(input("Please enter your midterm note: "))
		self.finalNote = float(input("Please enter your final note: "))

	def calculation(self):
		self.result = (self.midtermNote * 0.40) + (self.finalNote * 0.60)




	def control(self):
		self.calculation()

		if 87 <= self.result <= 100:
			print("Your Chracter Note: AA" + f"\nYour Average Grade: {self.result}")
		elif 81 <= self.result <= 86:
			print("Your Chracter Note: BA" + f"\nYour Average Grade: {self.result}")
		elif 74 <= self.result <= 80:
			print("Your Chracter Note: BB" + f"\nYour Average Grade: {self.result}")
		elif 67 <= self.result <= 73:
			print("Your Chracter Note: CB" + f"\nYour Average Grade: {self.result}")
		elif 60 <= self.result <= 66:
			print("Your Chracter Note: CC" + f"\nYour Average Grade: {self.result}")
		elif 53 <= self.result <= 59:
			print("Your Chracter Note: DC" + f"\nYour Average Grade: {self.result}")
		elif 46 <= self.result <= 52:
			print("Your Chracter Note: DD" + f"\nYour Average Grade: {self.result}")
		elif 39 <= self.result <= 45:
			print("Your Chracter Note: FD" + f"\nYour Average Grade: {self.result}")
		elif 0 <= self.result <= 38:
			print("Your Chracter Note: FF" + f"\nYour Average Grade: {self.result}")
		else:
			print("Please try again!")

my_instance = midTermFinal()
my_instance.control()