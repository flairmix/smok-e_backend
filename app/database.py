from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./smoke_0.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


# postgresql
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@localhost/TodoApplicationDatabase"
# SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://flairmix:M120461mix@PostgresContainer:5432/flairmix"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://flairmix:M120461mix@PostgresContainer:5432/flairmix"


engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

