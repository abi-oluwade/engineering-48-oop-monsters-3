# 'Monsters' is the parent class for 2 different subclasses, it contains the name and skill_list attribute.
class Monsters:
    def __init__(self, name, skill_list):
        self.name = name
        self.skill_list = skill_list

    # The method here adds a new skill  to the monster by appending it to the end of the skills list, this works because
    # we created the data type 'list' in the object 'monsters1'. And returns an updated 'skill_list' attribute to the
    # object 'monsters1'
    def new_skill(self, new_skill):
        self.skill_list.append(new_skill)
        return self.skill_list


# Here when creating object monster1, to turn it into a list used [] brackets, what would be a cleaner way to do this?

monster1 = Monsters('Dexter', ['Hairy, Snarmy, Cold'])
monster2 = Monsters('Terrie', ['Boxxy, Puppy, Kibble'])
monster3 = Monsters('Bison', ['Micro, Tweezers, Water'])


# print(monster1.skill_list)
# monster1.new_skill('Full')
# print(monster1.skill_list)
# print(monster1.new_skill('Quick'))

