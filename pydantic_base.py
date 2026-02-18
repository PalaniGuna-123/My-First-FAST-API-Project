from pydantic import BaseModel 

class Person(BaseModel):
    name: str
    age: int
    email: str
Valid_data = Person(name="Guna", age=30, email="john.doe@example.com")
print(Valid_data)