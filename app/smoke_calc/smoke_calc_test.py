import unittest

from .smoke_corridor.Room import Room
from .smoke_corridor.Corridor import Corridor
from .smoke_corridor.corridor_calc_one import corridor_calc_one


class TestRoom(unittest.TestCase):
    def test_Room(self):
        Room_test = Room(
                 room_systemname = "Room_System_Name_test",
                 room_name = "Room_name_test",
                 room_level = 1,
                 room_area_m2 = 100,
                 room_high_m = 3,
                 room_fire_load_density = 800,
                 room_calorific_value_fire_load = 14,
                 room_temp_inside = 18)
          
        Corridor_test =  Corridor(
                 corridor_system_name = "Room_System_Name_test",
                 corridor_level = 1,
                 corridor_hight = 3,
                 corridor_door_hight = 2.,
                 corridor_door_width = 1.,
                 corridor_area = 30,
                 corridor_lenght = 15,
                 corridor_coef_building_type = 1.2,
                 corridor_temp = 18
                 )
        
        corridor_calc_one(Room_test, Corridor_test)
        
        
        Room_test.calc_Fw()
        Room_test.calc_v0_air_for_burn()
        Room_test.calc_Fw_unit_fire_load_by_walling()
        
        self.assertEqual(Room_test.room_volume_m3, 300)
        self.assertEqual(Room_test.Fw, 269.4)
        self.assertEqual(Room_test.v0_air_for_burn, 3.68)
        self.assertEqual(Room_test.Fw_unit_fire_load_by_walling, 21.68)
        
    
    
if __name__ == '__main__':
    unittest.main()



# {
#   "room_volume_m3": 300,
#   "Fw": 269.4,
#   "A0": 2,
#   "CALORIFIC_VALUE_WOOD": 13.8,
#   "Fw_unit_fire_load_by_walling": 21.68,
#   "v0_air_for_burn": 3.68,
#   "room_opening_rate": 0.07,
#   "unit_fire_load_critical": 1.43,
#   "unit_fire_load_by_floor_square": 57.97,
#   "fire_type": "Регулируемый вентиляцией",
#   "room_temp_inside_K": 291,
#   "max_temp": 1363.07,
#   "temp_smoke_coridor": 1090.45,
#   "corridor_smoke_hight_limit": 1.65,
#   "corridor_temp_K": 291,
#   "corridor_smoke_temp": 568.87,
#   "corridor_door_area": 2,
#   "smoke_consumption_mass": 3.39,
#   "smoke_density": 0.62,
#   "smoke_consumption_vol": 19690.95
# }