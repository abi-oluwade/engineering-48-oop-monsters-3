# 'Monsters' is the parent class for 2 different subclasses, it contains the name and skill_list attribute.
# If a attribute/argument/parameter is = to a list, doe we not have to state it in the __init__?
class Monsters:
    def __init__(self, name):
        self.name = name
        self.skill_list = []

    # The method here adds a new skill  to the monster by appending it to the end of the skills list, this works because
    # we created the data type 'list' in the object 'monsters1'. And returns an updated 'skill_list' attribute to the
    # object 'monsters1'
    def new_skill(self, new_skill):
        self.skill_list.append(new_skill)
        return self.skill_list


# Here when creating object monster1, to turn it into a list used [] brackets, what would be a cleaner way to do this?

monster1 = Monsters('Dexter')
monster2 = Monsters('Terrie')
monster3 = Monsters('Bison')

# # This shows how the new_skill method can add skills to the skill_list of the monsters.
# print(monster1.skill_list)
# print(monster1.new_skill('Mouse, House, Cars'))
# print(monster1.skill_list)


# print(monster1.skill_list)
# print(monster1.new_skill('Quick'))

