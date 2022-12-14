from pydantic import BaseModel, Field
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


class MyModel(BaseModel):
    metadata: dict[str, str] = Field(alias='metadata_')

    class Config:
        orm_mode = True


BaseModel = declarative_base()


class SQLModel(BaseModel):
    __tablename__ = 'my_table'
    id = sa.Column('id', sa.Integer, primary_key=True)
    # 'metadata' is reversed by SQLAlchemy, hence the '-'
    metadata_ = sa.Column('metadata', sa.JSON)


sql_model = SQLModel(metadata_={'key': 'val'}, id=1)

pydantic_model = MyModel.from_orm(sql_model)


print(pydantic_model)

print(pydantic_model.dict(by_alias=True))