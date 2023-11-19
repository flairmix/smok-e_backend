from .database import Base
from sqlalchemy import Column, Integer, Float,String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

    todos = relationship("Todos", back_populates="owner")
    # smoke_corridor_calc = relationship("Smoke_corridor", back_populates="owner")


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="todos")


# class Smoke_corridor(Base):
#     __tablename__ = 'Smoke_corridors_calculations'

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)
#     create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

#     room_systemname = Column(String)
#     room_name = Column(String)
#     room_level = Column(String)
#     room_area_m2 = Column(Float)
#     room_high_m = Column(Float)
#     room_fire_load_density = Column(Float)
#     room_calorific_value_fire_load  = Column(Float)
#     room_temp_inside  = Column(Float)
#     corridor_system_name = Column(String)
#     corridor_level = Column(Float)
#     corridor_hight = Column(Float)
#     corridor_door_hight = Column(Float)
#     corridor_door_width = Column(Float)
#     corridor_area = Column(Float)
#     corridor_lenght = Column(Float)
#     coef_building_type = Column(Float)
#     corridor_temp = Column(Float)

#     owner_id = Column(Integer, ForeignKey("users.id"))
#     owner = relationship("Users", back_populates="smoke_corridors_calc")
    


