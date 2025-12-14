# Main Program
from models.package import Package
from models.logistics_system import LogisticsSystem
from models.locker import Locker
import time
from storage.json_storage import load_json, save_json
from models.user import User
from reports.admin_reports import raport_statusow
import os 
from reports.charts import wykres_statusow

STATUS_FLOW = [
	"przyjęta",
	"w transporcie",
	"w sortowni",
	"w doręczeniu",
	"doręczona"
]

BASE_DIR = os.path.dirname(__file__)
USERS_PATH = os.path.join(BASE_DIR, "data", "users.json")
PACKAGES_PATH = os.path.join(BASE_DIR, "data", "packages.json")

users_data = load_json(USERS_PATH)
system = LogisticsSystem()

packages_data = load_json(PACKAGES_PATH)

for p_data in packages_data:
	system.add_package(Package.from_dict(p_data))

def login():
	username = input("Login: ").strip()
	password = input("Hasło: ").strip()

	for u in users_data:
		if u["username"] == username and u["password"] == password:
			return User(username, u["role"])
		
	return None

def zapisz_paczki():
	save_json(
		PACKAGES_PATH,
		[p.to_dict() for p in system.packages]
	)

def auto_update_statuses():
	for p in system.packages:
		if p.status != "doręczona":
			current_index = STATUS_FLOW.index(p.status)
			next_status = STATUS_FLOW[current_index + 1]
			p.zmien_status(next_status)
		
		zapisz_paczki()

def run_status_scheduler():
	while True:
		time.sleep(60) # 60 sekund
		auto_update_statuses()

def admin_menu(system):
	while True:
		print("\n🔐 PANEL ADMINA - FLY Express📦🚚")
		print("1. Raport statusów paczek")
		print("2. Symuluj zmianę statusów")
		print("3. Wykres statusów paczek")
		print("4. Wyloguj")

		wybor = input("Wybierz opcję: ")
		
		if wybor == "1":
			raport_statusow(system.packages)
		elif wybor == "2":
			auto_update_statuses()
			print("⏱️ Statusy paczek zaktualizowane")
		elif wybor == "3":
			wykres_statusow(system.packages)
		elif wybor == "4":
			print("🔓 Wylogowno.")
			return
		else:
			print("❌ Nieprawidłowy wybór")

def nadaj_paczke(user):
	waga = float(input("Podaj wagę paczki: "))
	kraj = input("Podaj kraj: ")
	priorytet = input("Priorytet (tak/nie): ").lower() == "tak"

	paczka = Package(waga, kraj, user.username, priorytet)
	system.add_package(paczka)
	zapisz_paczki()

	print("\n✅️ Paczka nadana!")
	print("Tracking ID:", paczka.tracking_id)

def sledz_paczke():
	tid = input("Podaj tracking ID: ")
	p = system.find_package(tid)

	if p:
		print(p.status)
		for s, t in p.history:
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
			print("🔓 Wylogowno.")
			print("Dziękujemy za skorzystanie z usług FLY Express📦🚚🌞")
			return
		else:
			print("❌ Nieprawidłowy wybór")

def main():
	while True:
		print("\n🔑 LOGOWANIE - FLY Express")
		user = login()
		
		if not user:
			print("❌ Błędny login lub hasło")
			continue
	
		print(f"✅️ Zalogowano jako {user.username} ({user.role})")

		if user.role == "admin":
			admin_menu(system)
		else:
			user_menu(user)

while True:
	main()
