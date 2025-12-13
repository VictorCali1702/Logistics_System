# Logistics System
from utils.pricing import Pricing

class LogisticsSystem:
	def __init__(self):
		self.packages = []

	def add_package(self, package):
		self.packages.append(package)

	def calculate_price(self, package):
		return (
			Pricing.koszt_wagi(package.waga)
			+ Pricing.koszt_kraju(package.kraj)
			+ Pricing.koszt_priorytetu(package.priorytet)
		)
	
	def report(self):
		print(f"Liczba paczek: {len(self.packages)}")
		