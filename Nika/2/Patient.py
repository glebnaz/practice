class Patient:
    def __init__(self, first_name='', last_name='', father_name='',date_of_birth=''):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_father_name(father_name)
        self.set_date_of_birth(date_of_birth)

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, name):
        self.__first_name = name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, name):
        self.__last_name = name

    def get_father_name(self):
        return self.__father_name

    def set_father_name(self, name):
        self.__father_name = name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date):
        self.__date_of_birth = date


    def __str__(self):
        return self.get_first_name() + ", " + self.get_last_name() + ", " + self.get_father_name() + ", " \
            + self.get_date_of_birth() + ", " + "."
