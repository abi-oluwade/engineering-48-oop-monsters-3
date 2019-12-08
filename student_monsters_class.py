# 'Student Monster'class is responsible for storing the uni_id and grade data of monsters. However since it will
# share many of the same of the 'Monster' class, rather than retyping all of the self.functions such as 'self.name'
# again in the init block of code, we can rather inherit all of these attributes and methods in order to use them in
# this child class.
from monsters_class import *


# For this to be possible though, we must use the super(). function which essentially allows this process to happen
# by calling the __init__ method of the Parent/superclass(in this case the 'Monsters' class so we don't have to repeat
# code
class StudentMonster(Monsters):
    def __init__(self, name, skill_list, uni_id, grade):
        super().__init__(name, skill_list)
        self.uni_id = uni_id
        self.__grade = grade

    # This method here allows the uni admin to see the grade of the student monster, it is also a set grade using .__
    # and as we can see, there is no self.name attribute in the StudentMonsters class but it can call that attribute
    # from the 'Monsters' class thanks to the super() function.

    def see_grade(self):
        return self.name + ' has grade: ' + self.__grade


# Here is something I wanted to ask, how would I go about calling the monster1 from 'Monsters', but allow it to let me
# input a uni_id and grade WITHOUT having to put in monster1 name and skill_list again?
# monster1 = StudentMonster() or Monsters() ?

monster1 = StudentMonster('Dexter', ['Hairy, Snarmy, Cold'], 1, 'A')
monster2 = StudentMonster('Terrie', ['Boxxy, Puppy, Kibble'], 2, 'B')
monster3 = StudentMonster('Bison', ['Micro, Tweezers, Water'], 3, 'C')
monster4 = StudentMonster('Loopy', ['Small, Smooth, Cute'], 4, 'D')

student_monster_list=[]
student_monster_list.append(monster1.see_grade())
student_monster_list.append(monster2.see_grade())
student_monster_list.append(monster3.see_grade())

for grade in student_monster_list:
    print(grade)


# probably meant to use a separate run file and import the attributes etc form a bunch of different classes/files

# print(monster1.name)
# print(monster1.skill_list)
# monster1.new_skill('Hot')
# print(monster1.skill_list)
# print(monster4.see_grade())
# print(monster1.__grade) Why does this not work, do you have to use get()?
