# Package

class Package:
	def __init__(self, waga, kraj, priorytet=False):
		self.waga = waga
		self.kraj = kraj
		self.priorytet = priorytet
		self.status = "przyjęta"

	def zmien_status(self, nowy_status):
		self.status = nowy_status

	def info(self):
		return f"{self.status} | {self.kraj} | {self.waga} kg | priorytet: {self.priorytet}"
