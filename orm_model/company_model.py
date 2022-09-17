from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(LONGTEXT(unicode="utf-8"))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: list[constr(max_length=255)]

    class Config:
        orm_mode = True


if __name__ == '__main__':
    co_orm = CompanyOrm(
        id=123,
        public_key='foobar',
        name='Testing',
        domains=['example.com', 'foobar.com']
    )
    print(co_orm)
    co_model = CompanyModel.from_orm(co_orm)
    print(co_model)

