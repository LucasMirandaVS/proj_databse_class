from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


hero_1 = Hero(name="Capitão Patria", secret_name="Homelander",age=44)
hero_2 = Hero(name="A-Train", secret_name="Um Trem",age=28)
hero_3 = Hero(name="Rusty-Man", secret_name="Ferrugem", age=22)


engine = create_engine("sqlite:///banco_de_dados.db", echo = True)


SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()