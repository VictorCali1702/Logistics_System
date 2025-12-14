# Package
import uuid
from datetime import datetime


class Package:
	def __init__(self, waga, kraj, owner, priorytet=False):
		self.tracking_id = f"FLY-{uuid.uuid4().hex[:6].upper()}"
		self.waga = waga
		self.kraj = kraj
		self.owner = owner
		self.priorytet = priorytet

		self.status = "przyjęta"
		self.history = [(self.status, self._time())]
	
	def _time(self):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	def zmien_status(self, nowy_status):
		self.status = nowy_status
		self.history.append((nowy_status, self._time()))

	def to_dict(self):
		return {
			"tracking_id": self.tracking_id,
			"waga": self.waga,
			"kraj": self.kraj,
			"owner": self.owner,
			"priorytet": self.priorytet,
			"status": self.status,
			"history": self.history
		}
	'''		
	def pokaz_historie(self):
		print("Historia statusów:")
		for status, time in self.history:
			print(f"{time} -> {status}")
	'''
	@staticmethod
	def from_dict(data):
		p = Package(
			data["waga"],
			data["kraj"],
			data["owner"],
			data["priorytet"]
		)
		p.tracking_id = data["tracking_id"]
		p.status = data["status"]
		p.history = data["history"]
		return p