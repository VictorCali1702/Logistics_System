# Paczkomaty InPost

class Locker:
	def __init__(self, locker_id, size):
		self.locker_id = locker_id
		self.size = size # A / B / C
		self.occupied = False

	def can_fit(self, package):
		limits = {"A": 1, "B": 5, "C": 25}
		return package.waga <= limits[self.size] and not self.occupied
	
	def place_package(self, package):
		if self.can_fit(package):
			self.occupied = True
			package.zmien_status("w paczkomacie")
			return True
		return False