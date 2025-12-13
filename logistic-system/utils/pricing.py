# Pricing

class Pricing:
	@staticmethod
	def koszt_wagi(waga):
		if waga <= 1:
			return 10
		elif waga <= 5:
			return 20
		return 40
	
	@staticmethod
	def koszt_kraju(kraj):
		if kraj.lower() == "polska":
			return 0
		elif kraj.lower() in ['niemcy', 'francja', 'hiszpania', 'portugalia', 'włochy', 'holandia', 'belgia', 'szwajcaria',
						'austria', 'czechy', 'słowacja', 'węgry', 'chorwacja', 'litwa', 'łotwa', 'estonia', 
						'finlandia', 'szwecja', 'dania', 'norwegia', 'islandia', 'lichtenstein', 'luksemburg',
						'bułgaria', 'rumunia', 'grecja', 'malta', 'słowenia', 'irlandia', 'cypr']:
			return 15
		return 40
	
	@staticmethod
	def koszt_priorytetu(priorytet):
		return 30 if priorytet else 0
	
		