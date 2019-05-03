class Persona:

	def __init__(self,nombre,edad):
		self.nombre=nombre
		self.edad=edad

	def __eq__(self,objeto2):
		if self.edad==objeto2.edad:
			return True
		return False

	def __ne__(self,objeto2):
		if self.edad!=objeto2.edad:
			return True
		return False

	def __gt__(self,objeto2):
		if self.edad>objeto2.edad:
			return True
		return False

	def __ge__(self,objeto2):
		if self.edad>=objeto2.edad:
			return True
		return False

	def __lt__(self,objeto2):
		if self.edad<objeto2.edad:
			return True
		return False

#main block

persona1=Persona("Juan",22)
persona2=Persona("Ana",20)

if persona1==persona2:
	print("Las dos persona tiene la misma edad")
else: 
	print ("No tienen la misma edad")