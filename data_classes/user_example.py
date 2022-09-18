import dataclasses

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    friends: list[int] = dataclasses.field(default_factory=lambda: [0])
    age: int | None = dataclasses.field(
        default=None,
        metadata=dict(title='The age of the user', description='do not lie!')
    )
    height: int | None = Field(None, title='The height in cm', ge=50, le=300)


user = User(id='42')
print(user.__pydantic_model__.schema())