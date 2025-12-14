# MENU ADMINA (Raporty)

def raport_statusow(packages):
	stats = {}

	for p in packages:
		stats[p.status] = stats.get(p.status, 0) + 1

	print("📊 STATUSY PACZEK")
	for k, v in stats.items():
		print(k, ":", v)

def admin_menu(system):
	from reports.admin_reports import raport_statusow
	raport_statusow(system.packages)
