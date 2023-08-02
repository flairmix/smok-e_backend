import sys
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from starlette import status
from .auth import get_current_user
from ..smoke_calc.smoke_corridor.corridor_df_one import corridor_df_one
from ..smoke_calc.smoke_corridor.corridor_calc_one import corridor_calc_one
from ..smoke_calc.smoke_corridor.corridor_calc_one_response import corridor_calc_response
from ..smoke_calc.smoke_corridor.Room import Room
from ..smoke_calc.smoke_corridor.Corridor import Corridor

sys.path.append("..")

router = APIRouter(
    prefix='/smoke',
    tags=['smoke']
)


@router.get("/corridor/", status_code=status.HTTP_200_OK)
def smoke_corridor(
        room_systemname: str = Query(min_lenght=3, default='room_systemname_default'),
        room_name: str = Query(min_length=3, default='room_name_default'),
        room_level: int = Query(gt=-10, default=1),
        room_area_m2: float = Query(gt=0, default=100.0),
        room_high_m: float = Query(gt=0, default=3.0),
        room_fire_load_density: float = Query(gt=0, default=800.0),
        room_calorific_value_fire_load: float = Query(gt=0, default=14.0),
        room_temp_inside: int = Query(gt=0, default=18),
        corridor_system_name: str = Query(min_lenght=3, default='corridor_system_name_default'),
        corridor_level: int = Query(gt=-10, default=1),
        corridor_hight: float = Query(gt=0, default=3.0),
        corridor_door_hight: float = Query(gt=0, default=2.0),
        corridor_door_width: float = Query(gt=0, default=1.0),
        corridor_area: float = Query(gt=0, default=30.0),
        corridor_lenght: float = Query(gt=0, default=15.0),
        coef_building_type: float = Query(gt=0, default=1.2),
        corridor_temp: int = Query(gt=0, default=18)
        ):
    room = Room(room_systemname, room_name, room_level, room_area_m2, room_high_m, room_fire_load_density,
                room_calorific_value_fire_load, room_temp_inside)

    corridor = Corridor(corridor_system_name, corridor_level, corridor_hight,
                        corridor_door_hight, corridor_door_width, corridor_area,
                        corridor_lenght, coef_building_type, corridor_temp)

    smoke_result_0 = corridor_calc_one(room, corridor)
    
    smoke_result_df = corridor_df_one(room, corridor)
    smoke_result_dict = smoke_result_df.to_dict(orient='dict')

    result_output = corridor_calc_response(room, corridor)

    return result_output
