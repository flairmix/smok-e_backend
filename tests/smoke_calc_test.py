import unittest

from ..app.smoke_calc.smoke_corridor.Room import Room


class TestRoom(unittest.TestCase):
    def test(self):
        Room_test = Room(
                 room_systemname = "Room_System_Name_test",
                 room_name = "Room_name_test",
                 room_level = 1,
                 room_area_m2 = 50,
                 room_high_m = 3,
                 room_fire_load_density = 800,
                 room_calorific_value_fire_load = 14,
                 room_temp_inside = 24)
        
        Room_test.calc_Fw()
        
        self.assertEqual(Room_test.Fw, 169.67)
    
    
if __name__ == '__main__':
    unittest.main()

