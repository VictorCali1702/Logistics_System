# Main Program
from models.package import Package
from models.logistics_system import LogisticsSystem
from models.locker import Locker
import time
from storage.json_storage import load_json, save_json
from models.user import User
from reports.admin_reports import raport_statusow

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

def admin_menu(system):
	raport_statusow(system.packages)


def nadaj_paczke(user):
	waga = float(input("Podaj wagę paczki: "))
	kraj = input("Podaj kraj: ")
	priorytet = input("Priorytet (tak/nie): ").lower() == "tak"

	paczka = Package(waga, kraj, user.username, priorytet)
	system.add_package(paczka)

	print("\n✅️ Paczka nadana!")
	print("Tracking ID:", paczka.tracing_id)

def sledz_paczke():
	tid = input("Podaj tracing ID: ")
	p = system.find_package(tid)

	if p:
		print(p.status)
		for s, t in p.history():
			print(t, "->", s)
	
	else:
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
		
def user_menu(user):
	while True:
		print("\n📦 SYSTEM LOGISTYCZNY FLY Express")
		print("1. Nadaj paczkę")
		print("2. Śledź paczkę")
		print("3. Wyjście")

		wybor = input("Wybierz opcję: ")

		if wybor == "1":
			nadaj_paczke(user)
		elif wybor == "2":
			sledz_paczke()
		elif wybor == "3":
			print("Dziękujemy za skorzystanie z usług FLY Express.")
			break
		else:
			print("❌ Nieprawidłowy wybór")

admin_menu(system)
user_menu()
