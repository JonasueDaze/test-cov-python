from models.person import Person
import repositories.person as repository


def create(person: Person):
    return repository.create(person)


def get(id: int):
    return repository.get(id)


def get_all():
    return repository.get_all()


def update(person: Person):
    repository.update(person)


def delete(id: int):
    repository.delete(id)
