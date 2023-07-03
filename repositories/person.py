from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from models.person import Person

engine = create_engine(
    "postgresql+psycopg://postgres:postgres@localhost/postgres")
sessmaker = sessionmaker(engine)


# Auxiliary classes


class Base(DeclarativeBase):
    pass


class PersonEntity(Person, Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    age: Mapped[int] = mapped_column()


def __to_model(entity: PersonEntity):
    return Person(entity.id, entity.name, entity.age)


def __from_model(model: Person):
    return PersonEntity(model.id, model.name, model.age)


# Repository methods


def create(model: Person):
    with sessmaker.begin() as session:
        entity = __from_model(model)
        session.add(entity)
        session.flush()
        return entity.id


def get(id: int):
    with sessmaker.begin() as session:
        entity = session.get(PersonEntity, id)
        if entity is None:
            return None
        return __to_model(entity)


def get_all():
    with sessmaker.begin() as session:
        models: list[Person] = []
        entities = session.query(PersonEntity).all()
        for entity in entities:
            models.append(__to_model(entity))
        return models


def update(model: Person):
    with sessmaker.begin() as session:
        session.query(PersonEntity).filter(PersonEntity.id == model.id).update(
            {PersonEntity.age: model.age, PersonEntity.name: model.name})


def delete(id: int):
    with sessmaker.begin() as session:
        session.query(PersonEntity).filter(PersonEntity.id == id).delete()
