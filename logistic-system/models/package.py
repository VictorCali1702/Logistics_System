# Package
import uuid
from datetime import datetime


class Package:
	def __init__(self, waga, kraj, priorytet=False):
		self.tracking_id = self._generate_tracking_id()
		self.waga = waga
		self.kraj = kraj
		self.priorytet = priorytet

		self.status = "przyjęta"
		self.history = [(self.status, self._timestamp())]

	def _generate_tracking_id(self):
		return f"FlyExpress-{uuid.uuid4().hex[:6].upper()}"
	
	def _timestamp(self):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	def zmien_status(self, nowy_status):
		self.status = nowy_status
		self.history.append((nowy_status, self._timestamp()))

	def info(self):
		return (
			f"Tracking: {self.tracking_id}\n"
			f"Status: {self.status}\n"
			f"Kraj: {self.kraj}\n" 
			f"Waga: {self.waga} kg\n" 
			f"Priorytet: {self.priorytet}"
		)
	
	def pokaz_historie(self):
		print("Historia statusów:")
		for status, time in self.history:
			print(f"{time} -> {status}")
			