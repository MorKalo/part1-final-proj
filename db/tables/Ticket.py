from datetime import datetime
from sqlalchemy import Table, Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from db.Db_config import Base
from sqlalchemy.orm import relationship, backref

association_table= Table('flight_customer', Base.metadata,
                         Column('flght_id', ForeignKey ('flights.id', ondelete='CASCADE'), primary_key=True),
                         Column('customer_id', ForeignKey ('customers.id', ondelete='CASCADE'), primary_key=True),
                         )

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    flight_id= Column(BigInteger(), ForeignKey('flights.id', ondelete='CASCADE'), nullable=False)
    customer_id=Column(BigInteger(), ForeignKey('customers.id', ondelete='CASCADE'), nullable=False)

    #__table_args__ = (UniqueConstraint('flght_id', 'customer_id', name='una_1')) #one customer cun buy only one ticket per flight

    flight=relationship('Flight', backref=backref('tickets_of_flight', uselist=False, passive_deletes=True))
    customer=relationship('Customer', backref=backref('tickets_of_customer', uselist=False, passive_deletes=True))

    def __repr__(self):
        return f'\n<id={self.id} flight_id={self.flight_id} customer_id{self.customer_id} >'

    def __str__(self):
        return f'\n<id={self.id} flight_id={self.flight_id} customer_id{self.customer_id} >'


