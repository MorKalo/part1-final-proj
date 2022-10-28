from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from db.Db_config import Base
from db.tables.User import User

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name= Column(String())
    last_name= Column(String())
    address=Column(String())
    phone_number=Column(String(), unique=True)
    credit_card_no=Column(String(), unique=True)
    user_id=Column(BigInteger,  ForeignKey('users.id', ondelete='CASCADE'), unique=True)

    customer_users=relationship('User',foreign_keys=[user_id], backref=backref("customer_user", uselist=True, passive_deletes=True))


    def __repr__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} address={self.address}\
         phone_number={self.phone_number} credit_card_no={self.credit_card_no} user_id={self.user_id}>'

    def __str__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} address={self.address}\
         phone_number={self.phone_number} credit_card_no={self.credit_card_no} user_id={self.user_id}>'

