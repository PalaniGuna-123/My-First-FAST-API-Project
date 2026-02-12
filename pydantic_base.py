from pydantic import BaseModel ,EmailStr

class Person(BaseModel):
    name: str
    age: int
    email: EmailStr
Valid_data = Person(name="Guna", age=30, email="john.doe@example.com")
print(Valid_data)