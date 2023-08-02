from .Room import Room
from .Corridor import Corridor
from .corridor_calc_one import corridor_calc_one
import numpy as np
import pandas as pd


def corridor_df_one(room: Room, corridor: Corridor):

    parameter = corridor_calc_one(room, corridor)

    for i in range(0, len(parameter)):
        if type(parameter[i]) in (float, np.float64):
            parameter[i] = round(parameter[i], 2)
            
    name_parameter_rus = [
        'Коридор', 
        'Наименование обслуживаемого помещения',
        'Площадь пола помещения', 
        'Высота помещения', 
        'Объём помещения',
        'Суммарная площадь внутренней поверхности ограждающих строительных конструкций',
        'Проем №1 ширина', 
        'Проем №1 высота',
        'Суммарная площадь проемов помещения',
        'Низшая теплота сгорания древесины',
        'Плотность пожарной нагрузки помещения',
        'Удельная приведенная пожарная нагрузка, отнесенная к площади тепловоспринимающей поверхности ограждающих строительных конструкций помещения',
        'Средняя теплота сгорания пожарной нагрузки',
        'Удельное количество воздуха, необходимое для полного сгорания пожарной нагрузки',
        'Проемность помещения',
        'Удельное критическое количество пожарной нагрузки',
        'Удельная приведенная пожарная нагрузка, отнесенная к площади пола помещения',
        'Вид объемного пожара',
        'Начальная температура воздуха в помещении',
        'Начальная температура воздуха в помещении',
        'Максимальная среднеобъемная температура в помещении',
        'Искомое значение температуры газов, поступающих из горящего помещения в коридор',
        'Высота коридора', 'Площадь коридора', 'Длина коридора',
        'Предельная толщина дымового слоя',
        'Температура воздуха в коридоре', 'Температура воздуха в коридоре',
        'Средняя температура дымового слоя',
        'Поправочный коэффициент на тип здания',
        'Высота двери при выходе из коридора по путям эвакуации',
        'Ширина двери при выходе из коридора по путям эвакуации',
        'Площадь двери при выходе из коридора по путям эвакуации',
        'Массовый расход удаляемых непосредственно из коридоров продуктов горения',
        'Плотность дымовых газов',
        'Объемный расход удаляемых непосредственно из коридоров продуктов горения'
    ]

    name_parameter = [
        'corridor',
        'room_name',
        'room_area_m2',
        'room_high_m',
        'room_volume_m3',
        'Fw',
        'corridor_door_width',
        'corridor_door_hight',
        'A0',
        'CALORIFIC_VALUE_WOOD',
        'room_fire_load_density',
        'Fw_unit_fire_load_by_walling',
        'room_calorific_value_fire_load',
        'v0_air_for_burn',
        'room_opening_rate',
        'unit_fire_load_critical',
        'unit_fire_load_by_floor_square',
        'fire_type',
        'room_temp_inside',
        'room_temp_inside_K',
        'max_temp',
        'temp_smoke_coridor',
        'corridor_hight',
        'corridor_area',
        'corridor_lenght',
        'corridor_smoke_hight_limit',
        'corridor_temp_C',
        'corridor_temp_K',
        'corridor_smoke_temp',
        'coef_building_type',
        'corridor_door_hight',
        'corridor_door_width',
        'corridor_door_area',
        'smoke_consumption_mass',
        'smoke_density',
        'smoke_consumption_vol'
    ]
    

    units = [
        '-',
        '-',
        'м2',
        'м',
        'м3',
        'м2',
        'м',
        'м',
        'м2',
        'МДж/кг',
        'МДж/м2',
        'кг/м2',
        'МДж/кг',
        'м3/кг',
        'м 1/2',
        'кг/м2',
        'кг/м2',
        '-',
        'C',
        'K',
        'K',
        'K',
        'м',
        'м2',
        'м',
        'м',
        'C',
        'K',
        'K',
        '-',
        'м',
        'м',
        'м2',
        'кг/с',
        'кг/м3',
        'м3/ч',
    ]

    sign = [
        '-', '-', 'Fƒ', 'hƒ', 'V', 'Fw', '-', '-', 'A0', 'Qнд', 'qп', 'qk',
        'Qнср', 'V0', 'П', 'qkкр', 'q0', '-', 'tr', 'Tr', 'T0max', 'T0',
        'H', 'Ac', 'lc', 'hsm', 'trk', 'Trk', 'Tsm', 'ksm', 'Hd', 'bd',
        'Ad', 'Gsm', 'ρsm', 'Lsm'
    ]
    
    
    data = pd.DataFrame(name_parameter, columns=['name_parameter'])
    data['sign'] = sign
    data['units'] = units
    data['parameter'] = parameter

    return data
