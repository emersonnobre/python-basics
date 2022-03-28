# Classes são tipos personalizados de dados
class Student:
    # construtor do python
    def __init__(self, name, birthday, is_problematic):
        self.name =  name
        self.birthday = birthday
        self.is_problematic = is_problematic

    def showinfo(self):
        print("name: {name}\nbirthday: {birthday}\nis_problematic? {is_problematic}".format(name = self.name, birthday = self.birthday, is_problematic = self.is_problematic))