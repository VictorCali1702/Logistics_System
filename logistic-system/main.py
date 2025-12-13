# Main Program
from models.package import Package
from models.logistics_system import LogisticsSystem
from models.locker import Locker

system = LogisticsSystem()

p1 = Package(2.5, "Niemcy", True)
system.add_package(p1)

print("Cena:", system.calculate_price(p1), "zł")

locker = Locker("INP-01", "B")
locker.place_package(p1)

print(p1.info())
system.report()
