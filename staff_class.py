from monsters_class import *


class Staff:
    def __init__(self, name, staff_id):
        super.__init__(name)
        self.staff_id = staff_id
        self.staff_name = []

    def staff(self, full_name):
        self.staff_name.append(full_name)