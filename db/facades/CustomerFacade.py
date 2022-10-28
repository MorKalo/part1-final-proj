from BaseFacade import BaseFacade
from db.tables.Flight import Flight
from db.tables.Customer import Customer
from db.tables.Ticket import Ticket
from errors.FlightNotFoundException import FlightNotFoundException
from errors.NoMoreTicketsForFlightsException import NoMoreTicketsForFlightsException
from errors.TicketNotFoundException import TicketNotFoundException
from errors.UsernotauthorizedException import UsernotauthorizedException
from logger import Logger

class CustomerFacade(BaseFacade):

    def __init__(self, logintoken):
        super().__init__()
        self.logger = Logger.get_instance()
        self.logintoken =logintoken



    def update_customer(self,customer_id,update_data):#input from user only the data that we want to update.
        if customer_id!=self.logintoken.id:
            raise UsernotauthorizedException #need to check the token
        #customer_id=self.logintoken.id
        self.logger.logger.debug( f'update customer is about to happen')
        original_customer = self.repo.get_by_condition(Customer, lambda query: query.filter(Customer.id == customer_id).all())
        if not original_customer:
            print('Failed, we cant find customer with this ID number.')
            self.logger.logger.error(
                                f'--FAILED--  {customer_id} we cant find customer with this ID number')
            return
        #trying to find this customer in Customer, and to check if there isnt another customer with does deatils:
        #Phone number
        if self.repo.get_by_condition(Customer,
                                      lambda query: query.filter(Customer.phone_number == update_data.phone_number).all()):
            print('Failed, a customer with this phone number is already exists.')
            self.logger.logger.error(
                                   f'--FAILED--  {customer_id} a customer with the same Phone number {update_data.phone_number}'
                                   f'is alredy exists.')
            return
            #Credit-Card number
        if self.logger.get_by_condition(Customer,
                                      lambda query: query.filter(Customer.credit_card_no == update_data.credit_card_no).all()) and \
                self.repo.get_by_condition(Customer, lambda query: query.filter(
                    Customer.credit_card_no == update_data.credit_card_no).all()) != original_customer:
            print('Failed, a customer with this credit card number is already exists.')
            self.logger.logger.error(
                                  f'--FAILED--  {customer_id} a customer with the Credit card  number {update_data.credit_card_no}'
                                   f'is alredy exists.')
            return
        self.repo.update_by_id(Customer, customer_id, {Customer.first_name: update_data.first_name, Customer.last_name: update_data.last_name,
                                                                    Customer.address: update_data.address, Customer.phone_number: update_data.phone_number,
                                                                    Customer.credit_card_no: update_data.credit_card_no})
        self.logger.logger.info(
                           f'--Sucsses--  customer id  {customer_id}  update details:'
                            f' {update_data}')


    def add_ticket(self, ticket):#Need to input object of ticket, with flight_id & customer_id
        #just the customer with login can buy for himself and admin can add ticket
        self.logger.logger.debug( f'adding ticket by {self.logintoken.name}, id {self.logintoken.id}, role{self.logintoken.role} is about to happen')
        flight= self.repo.get_by_condition(Flight, lambda query: query.filter(Flight.id==ticket.flight_id).all())
        if not flight:
            self.logger.logger.error( f'--FAILED--  adding ticket by {self.logintoken.name}, id '
                                                  f'{self.logintoken.id}, role{self.logintoken.role}  for flight'
                                                  f' NO. {ticket.flight_id}, because we cant find this flight')
            raise FlightNotFoundException
        if flight[0].remaining_Tickets <= 0:
            self.logger.logger.info( f'--FAILED--  adding ticket by {self.logintoken.name}, id '
                                                 f'{self.logintoken.id}, role{self.logintoken.role}  for flight'
                                                 f' NO. {ticket.flight_id}, because no more tickets are available'
                                                 f' for this flight')
            raise NoMoreTicketsForFlightsException(ticket.flight_id)
        customer = self.repo.get_by_condition(Customer, lambda query: query.filter(Customer.id == ticket.customer_id).all())
        if self.logintoken.role!=3:
            if customer[0].id!= self.logintoken.id:
                raise UsernotauthorizedException
                return
        if not customer:
            print('Failed, we cant find customer with this ID number.')
            self.logger.logger.error(
                               f'--FAILED--  {ticket.customer_id} we cant find customer with this ID number.')
        if self.repo.get_by_condition(Ticket, lambda query: query.filter(Ticket.customer_id == ticket.customer_id,
                                                                         Ticket.flight_id == ticket.flight_id).all()):
            print('Failed, this customer already heve ticket for this flight.')
            self.logger.logger.error(
                                   f'--FAILED-- customer id {ticket.customer_id} already heve ticket for this flight number {ticket.flight_id}.')
            return
        else:
            flight[0].remaining_Tickets -=1
            self.repo.add(ticket)
            self.logger.logger.info( f'--SUCCESS-- {self.logintoken.name} {self.logintoken.id} adding ticket for customer id  {ticket.customer_id} to flight {ticket.flight_id} is finish Successfully')
            self.logger.logger.debug( f'there is more {flight[0].remaining_Tickets} ticket for flight {ticket.flight_id}')
            return True

    def remove_ticket(self, ticket_id): #FUNC BY ID, fun can action only by the customer id thats own and admin
        ticket_exists = self.repo.get_by_condition(Ticket, lambda query: query.filter(Ticket.id == ticket_id).all())
        if not ticket_exists:
            self.logger.logger.error(
                                   f'--FAILED--   {self.logintoken.name}, id {self.logintoken.id} trying to remove ticket id {ticket_id}'
                                   f'  but we cant find this ticket')
            raise TicketNotFoundException
        elif ticket_exists[0].customer_id != self.logintoken.id:
            if self.logintoken.role != 3:
                raise UsernotauthorizedException
        else:
            self.logger.logger.debug(
                             f'removing ticket by {self.logintoken.name} id {self.logintoken.id} is about to happen.')
            flight = self.repo.get_by_condition(Flight,
                                            lambda query: query.filter(Flight.id == ticket_exists[0].flight_id).all())
            ticketforflight=flight[0].remaining_Tickets
            self.repo.update_by_id(Flight,ticket_id,{Flight.remaining_Tickets:ticketforflight+1})
            self.repo.delete(Ticket, ticket_id)
            self.logger.logger.info( f'--SUCCESS--  remove ticket by {self.logintoken.name} '
                                            f'id {self.logintoken.id} for customer id  {Ticket.customer_id}'
                                                 f' to flight {ticket_id} is finish Successfully')
            self.logger.logger.debug( f'there is more {flight[0].remaining_Tickets} ticket for flight {ticket_id}')
            return True

    def get_my_tickets(self):#FUNC only for my id, take id from token
        self.logger.logger.info(
                       f'--SUCCESS--  get ticket by customer {self.logintoken.name}  id  {self.logintoken.id} is finish Successfully')
        return self.repo.get_by_id(Ticket,(self.logintoken.id))







