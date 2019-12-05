from Doctor import Doctor
from Patient import Patient
from Appeal import Appeal

doctor = Doctor("Gleb","Nazemnov","Andreevich","TOP","Urologiy")
patient = Patient("Egor","Maxsimov","Urkovich","20-11-1998")
appeal = Appeal(doctor,patient,"bolen",25.5)


print(doctor)
print(patient)
print(appeal.get_Doctor().get_first_name())
