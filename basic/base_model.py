from pydantic import BaseModel, json, ValidationError


class User(BaseModel):
    id: int
    name = 'Jane Doe'


if __name__ == '__main__':
    user = User(id='123')
    # user_x = User(id='123.45')

    '''validation test'''

    assert user.id == 123
    # assert user_x.id == 123
    assert isinstance(user.id, int)
    assert user.name == 'Jane Doe'
    # assert user.name == 'Jane'
    user.id = 321
    assert user.id == 321
    # assert user.id == 123

    '''model`s property'''

    print(user.dict())
    print(user.json())

    '''model parsing'''
    # parsing obj
    new_user = User.parse_obj({ 'id': 1234, 'name': 'fuck'})
    print(new_user)

    #parsing raw
    new_user2 = User.parse_raw('{"id": 123, "name": "james"}')
    print(new_user2)

    '''type validation exception handling'''
    try:
        User.parse_obj(['not', 'a', 'dict'])
    except ValidationError as e:
        print(e)


