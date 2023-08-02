

class Corridor:

    def __init__(self,
                 corridor_system_name,
                 corridor_level,
                 corridor_hight,
                 corridor_door_hight,
                 corridor_door_width,
                 corridor_area,
                 corridor_lenght,
                 corridor_coef_building_type,
                 corridor_temp
                 ):
                     
        self.corridor_system_name = corridor_system_name
        self.corridor_level = corridor_level
        self.corridor_hight = corridor_hight
        self.corridor_door_hight = corridor_door_hight
        self.corridor_door_width = corridor_door_width
        self.corridor_opening1_area = self.corridor_door_hight * self.corridor_door_width
        self.corridor_area = corridor_area
        self.corridor_lenght = corridor_lenght
        self.corridor_coef_building_type = corridor_coef_building_type
        self.corridor_temp = corridor_temp
        self.corridor_temp_K = corridor_temp + 273

    def __str__(self):
        return f"class corridor: corridor_system_name-{self.corridor_system_name}, level:  {self.level}"
