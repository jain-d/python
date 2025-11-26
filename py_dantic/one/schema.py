from pydantic import BaseModel


class Engine(BaseModel):
    type: str | None
    cap: int | None

class Vehicle(BaseModel):
    company: str | None
    spec: Engine | None

class Person(BaseModel):
    id: int
    name: str
    age: int
    location: str | None
    vehicles: list[Vehicle]

class FinalStructure(BaseModel):
    People: list[Person]
