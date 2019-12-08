class Doctor:
    def __init__(self, first_name='', last_name='', father_name='',category='',specialty=''):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_category(category)
        self.set_speciality(specialty)
        self.set_father_name(father_name)

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

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    def get_specialty(self):
        return self.__specialty

    def set_speciality(self, specialty):
        self.__specialty = specialty

    def __str__(self):
        return self.get_first_name() + ", " + self.get_last_name() + ", " + self.get_father_name() + ", " \
            + self.get_category() + ", " + self.get_specialty() + "."
