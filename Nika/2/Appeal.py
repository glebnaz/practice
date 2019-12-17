#Обращения (Врач, Пациент, Дата обращения, Диагноз, Стоимость лечения).
import datetime
class Appeal:
    def __init__(self, Doctor, Patient,Diagnosis,Data,Cost):
        self.set_Doctor(Doctor)
        self.set_Date(Data)
        self.set_Cost(Cost)
        self.set_Diagnosis(Diagnosis)
        self.set_Patient(Patient)



    def getId(self):
        return self.__Id

    def get_Doctor(self):
        return self.__Doctor

    def set_Doctor(self, doctror):
        self.__Doctor = doctror

    def get_Patient(self):
        return self.__Patient

    def set_Patient(self, Patient):
        self.__Patient = Patient

    def get_Date(self):
        return self.__Date

    def set_Date(self,value):
        self.__Date = value

    def get_Diagnosis(self):
        return self.__Diagnosis

    def set_Diagnosis(self, d):
        self.__Diagnosis = d

    def setId(self, d):
        self.__Id = d

    def get_Cost(self):
        return self.__Cost

    def set_Cost(self, cost):
        self.__Cost = cost

    def __str__(self):
        return "Doctor - " + str(self.get_Doctor()) + ",Patient -  " + str(self.get_Patient()) + ", " + self.get_Diagnosis()+ ", " + str(self.get_Cost())
