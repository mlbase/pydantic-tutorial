from datetime import datetime

from pydantic import ValidationError
from pydantic.dataclasses import dataclass


class Myconfig:
    max_anystr_length = 10
    validate_assignment = True
    error_msg_templates = {
        'value_error.any_str.max_length': 'max_length:{limit_value}'
    }


@dataclass(config=Myconfig)
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None


user = User(id='42', signup_ts='2032-06-12T12:00')
try:
    user.name = 'x' * 20
except ValidationError as e:
    print(e)