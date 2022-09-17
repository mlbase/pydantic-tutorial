from typing import List, Optional
from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: float| None = None


class Bar(BaseModel):
    apple ='x'
    banana = 'y'


#dependency injection by pydantic
class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]


if __name__ == '__main__':
    m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
    print(m)

    print(m.dict())