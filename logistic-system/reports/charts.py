# Matplotlib - Logistics Analyse
import matplotlib.pyplot as plt

def wykres_statusow(packages):
	stats = {}

	for p in packages:
		stats[p.status] = stats.get(p.status, 0) + 1
		
	if not stats:
		print("Brak danych do wykresu")
		return
		
	statuses = list(stats.keys())
	counts = list(stats.values())

	plt.figure()
	plt.bar(statuses, counts)
	plt.title("Liczba paczek wg. statusu")
	plt.xlabel("Status paczki")
	plt.ylabel("Liczba paczek")
	plt.tight_layout()
	plt.show()
	