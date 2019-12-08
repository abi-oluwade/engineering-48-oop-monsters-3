from building_class import *


class LectureTheatres(Building):
    def __init__(self, location, hall_number):
        super().__init__(location)
        self.hall_number = hall_number

    def turn_lights_off(self):
        super().turn_lights_off()
        print('Sorry, the light will prevail')


# ex_lect = LectureTheatres('maimi', 200)
#
# ex_lect.turn_lights_off()
