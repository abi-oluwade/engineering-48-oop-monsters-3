# 'The Spooky Workshop' class  was responsible for the acceptance criteria of allowing the uni admin to list the
# available scary subjects as well as add students to the list who can take the subject

# Firstly we created the class that would contain the group of variables and methods, and the objects which act as a
# member or instance of the class. All values except scary_subject_list will have defaults of no value required,
# which allows us to manipulate the parameters/arguments of each object we create, meaning some don't need a
# 'student_monster_list' for example.

# from student_monsters_class import *

class SpookyWorkshops:
    def __init__(self, scary_subject_list, staff=0, student_monster_list=0, location=0):
        self.scary_subject_list = scary_subject_list
        self.staff = staff
        self.student_monster_list = student_monster_list
        self.location = location
# This method allows the uni admin to list the students available for the appropriate scary subjects. You can use it
# in different ways, by filling the student_monster_list parameter and telling them whatis available. Or leaving
# it blank and allowing for it to be used for a general announcement instead.

    def list_scary_subjects(self):
        return ' These are the workshops available: ' + str(self.scary_subject_list)

# This method allows the uni admin to add a student to a list of student_monsters, by first appending them to the end
# of the student_monster_list and then returning that NEW value to the method, which allows the object to call it
# and be printed.

    def add_student(self, name):
        (self.student_monster_list.append(name))
        return str(self.student_monster_list) + ' These are the workshops available: ' + str(
            self.scary_subject_list)



workshop1 = SpookyWorkshops(['Spooktober, Bad Now, Scary Snow'], 'Mr Spook', ['Dexter, Terrie, Bison'], 'Florida')
workshop2 = SpookyWorkshops(['Scary Summer, House of evil, Haunted Water'])
workshop3 = SpookyWorkshops(['Bad'])
workshop4 = SpookyWorkshops(['Med'])
workshop5 = SpookyWorkshops(['Good'])

# monster1 = StudentMonster('Dexter',['Hairy, Snarmy, Cold'], 1, 'A')
# monster2 = StudentMonster('Terrie', ['Boxxy, Puppy, Kibble'], 2, 'B')

list_of_running_workshops = []
list_of_running_workshops.append(workshop1.list_scary_subjects())
list_of_running_workshops.append(workshop2.list_scary_subjects())
list_of_running_workshops.append(workshop3.list_scary_subjects())
list_of_running_workshops.append(workshop4.list_scary_subjects())
list_of_running_workshops.append(workshop5.list_scary_subjects())


# print(workshop1.scary_subject_list)
# print(workshop1.list_scary_subjects())
# print(workshop2.list_scary_subjects())
# print(workshop1.add_student('Hooper'))
# print(workshop2.list_scary_subjects())

# for workshops in list_of_running_workshops:
#     print(workshops)

