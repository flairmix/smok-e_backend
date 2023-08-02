from .Room import Room
from .Corridor import Corridor
from ..smoke_consts import CALORIFIC_VALUE_WOOD


def corridor_calc_response(room: Room, corridor: Corridor) -> dict:
    """
    Returning results of calculations for pair: Room - Corridor.
    """
    
    result = { 
        'room_volume_m3' : room.room_volume_m3,
        'Fw' : room.Fw,
        'A0' : room.A0,
        'CALORIFIC_VALUE_WOOD' : CALORIFIC_VALUE_WOOD,
        'Fw_unit_fire_load_by_walling': room.Fw_unit_fire_load_by_walling,
        'v0_air_for_burn' : room.v0_air_for_burn,
        'room_opening_rate' : room.room_opening_rate,
        'unit_fire_load_critical' : room.unit_fire_load_critical,
        'unit_fire_load_by_floor_square' : room.unit_fire_load_by_floor_square,
        'fire_type' : ("Регулируемый вентиляцией" if room.fire_type.value == 1 else "Регулируемый нагрузкой"),
        'room_temp_inside_K' : room.room_temp_inside + 273,
        'max_temp' : room.max_temp,
        'temp_smoke_coridor' : room.temp_smoke_coridor,
        'corridor_smoke_hight_limit' : room.corridor_smoke_hight_limit,
        'corridor_temp_K' : room.corridor_temp_K,
        'corridor_smoke_temp' : room.corridor_smoke_temp,
        'corridor_door_area' : room.corridor_door_area,
        'smoke_consumption_mass' : room.smoke_consumption_mass,
        'smoke_density' : room.smoke_density,
        'smoke_consumption_vol' : room.smoke_consumption_vol
        }
    
    for key, value in result.items():
        if type(value) == float:
            result[key] = round(value, 2)
            
    return result