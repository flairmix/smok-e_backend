import sys
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from starlette import status


sys.path.append("..")

router = APIRouter(
    prefix='/convert_units',
    tags=['converter_units']
)


@router.get("/", status_code=status.HTTP_200_OK)
def convert_units(
    input_units: str = Query(min_length=1, default='Gcal_h'),
    input_value: float = Query(default=1.0),
    output_units: str = Query(min_length=1, default='kW')
                  ):
    
    return convert_power(input_units, input_value, output_units)


power_units = {'Gcal_h': 1.0, 
               'kW':1163, 
               'W': 1163000}


def convert_power(input_units: str,
                input_value: float,
                output_units: str 
                ) -> dict:
    if input_units not in power_units.keys() and output_units not in power_units.keys():
        return {'output_value': 'Fail'}

    elif input_units == 'Gcal_h':
        return {'output_value': (input_value * power_units[output_units])}

    elif input_units != 'Gcal_h':
        preconvert = round(input_value / power_units[input_units], 4) 
        return {'output_value': (preconvert * power_units[output_units])}

    else:
        return {'output_value': 'Fail'}
