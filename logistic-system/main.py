# Main Program
from models.package import Package
from models.logistics_system import LogisticsSystem
from models.locker import Locker
import time
from storage.json_storage import load_json, save_json
from models.user import User

USERS_PATH = "data/users.json"
PACKAGES_PATH = "data/packages.json"

users_data = load_json(USERS_PATH)
system = LogisticsSystem()

def login():
	username = input("Login: ")
	password = input("Hasło: ")

	for u in users_data:
		if u["username"] == username and u["password"] == password:
			return User(username, u["role"])
		
	return None

def nadaj_paczke():
	waga = float(input("Podaj wagę paczki: "))
	kraj = input("Podaj kraj: ")
	priorytet = input("Priorytet (tak/nie): ").lower() == "tak"

	paczka = Package(waga, kraj, priorytet)
	system.add_package(paczka)

	print("\n✅️ Paczka nadana!")
	print(paczka.info())

def sledz_paczke():
	tid = input("Podaj tracing ID: ")

	for p in system.packages:
		if p.tracking_id == tid:
			print(p.info())
			p.pokaz_historie()
			return
	
	print("❌ Nie znaleziono paczki")

def symuluj_statusy():
	for p in system.packages:
		if p.status == "przyjęta":
			p.zmien_status("w transporcie")
		elif p.status == "w transporcie":
			p.zmien_status("w sortowni")
		elif p.status == "w sortowni":
			p.zmien_status("w doręczeniu")
		elif p.status == "w doręczeniu":
			p.zmien_status("doręczona")
		
def menu():
	while True:
		print("\n📦 SYSTEM LOGISTYCZNY FLY Express")
		print("1. Nadaj paczkę")
		print("2. Śledź paczkę")
		print("3. Symuluj zmianę statusów")
		print("4. Wyjście")

		wybor = input("Wybierz opcję: ")

		if wybor == "1":
			nadaj_paczke()
		elif wybor == "2":
			sledz_paczke()
		elif wybor == "3":
			symuluj_statusy()
			print("🔄 Statusy zaktualizowane")
		elif wybor == "4":
			print("Dziękujemy za skorzystanie z usług FLY Express.")
			break
		else:
			print("❌ Nieprawidłowy wybór")

menu()
