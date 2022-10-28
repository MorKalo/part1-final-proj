from BaseFacade import BaseFacade
from db.tables.Administrator import Administrator
from db.tables.Customer import Customer
from db.tables.AirlineCompany import AirlineCompany
from errors.CreateUserAndObjectFailedException import CreateUserAndObjectFailedException
from db.tables.Country import Country
from errors.UsernotauthorizedException import UsernotauthorizedException
from errors.NameNeedToBeDifrentException import NameNeedToBeDifrentException
from test.DataExistException import DataExistException
from logger import Logger


class AdministratorFacade(BaseFacade):

    def __init__(self, logintoken):
        super().__init__()
        self.logger = Logger.get_instance()
        self.logintoken =logintoken


    def get_all_customers(self):
        self.logger.logger.debug( f'get all customer"s is about to happen')
        return self.repo.get_all(Customer)


    def create_airline(self, user, airline):#user and airline are object
        if not self.logintoken.role == 3:
            self.logger.logger.error(
                                   f'--FAILED--  this user "{self.logintoken.name, self.logintoken.id}"cant create airline.')
            raise UsernotauthorizedException
        else:
            if super().create_new_user(user):
                #self.add_airline(user, airline)
                self.logger.logger.debug( f'add new airline is about to happen')
                if self.repo.get_by_condition(AirlineCompany, lambda query: query.filter(
                        AirlineCompany.name == airline.name).all()):
                    self.logger.logger.error(
                                           f'--FAILED--  {airline.name} we already have Airline company with this name')
                    print('Failed.  we already have Airline company with this name.')
                    raise NameNeedToBeDifrentException
                if not self.repo.get_by_condition(Country,
                                                  lambda query: query.filter(Country.id == airline.country_id).all()):
                    print(f' Failed.  the country {airline.country_id} does not exist.')
                    return
                airline.user_id = user.id
                self.repo.add(airline)
                self.logger.logger.info( f' User created: {user}, Airline created: {airline}')
                return True
            else:
                self.logger.logger.error(
                                       f'--FAILED--   we cant create this user "{user}" and airline company "{airline}" .')
                raise CreateUserAndObjectFailedException


    def create_customer(self, user, customer):#user and customer are object
        if not self.logintoken.role == 3:
            raise UsernotauthorizedException
        else:
            if super().create_new_user(user):
                self.logger.logger.debug( f'adding customer is about to happen')
                # trying to find this customer in Customer, and to check if there isnt another customer with does deatils:
                # Phone number
                if self.repo.get_by_condition(Customer,
                                              lambda query: query.filter(
                                                  Customer.phone_number == customer.phone_number).all()):
                    print('Failed, a customer with this phone number is already exists.')
                    self.logger.logger.error(
                                           f'--FAILED--  {customer.id} a customer with the same Phone number {customer.phone_number}'
                                           f'is alredy exists.')
                    raise DataExistException
                    #return False
                # Credit-Card number
                if self.repo.get_by_condition(Customer, lambda query: query.filter(
                        Customer.credit_card_no == customer.credit_card_no).all()):
                    print('Failed, a customer with this credit card number is already exists.')
                    self.logger.logger.error(
                                           f'--FAILED--  {customer.id} a customer with the Credit card  number {customer.credit_card_no}'
                                           f'is alredy exists.')
                    raise DataExistException
                customer.user_id = user.id
                self.repo.add(customer)
                self.logger.logger.info(
                                       f'--Sucsses--  User created: {user}, Administrator created: {customer}')
                return True
            else:
                print(f'--Failed-- we cant create this user and Administrator')
                self.logger.logger.error(
                                       f'--FAILED--   we cant create this user "{user}" and Administrator{customer} .')
                raise CreateUserAndObjectFailedException


    def create_admin(self, user, administrator):#user and admin are object
        if not self.logintoken.role == 3:
            raise UsernotauthorizedException
        else:
            if super().create_new_user(user):
                self.logger.logger.debug( f'add new admin is about to happen')
                administrator.user_id = user.id
                self.repo.add(administrator)
                self.logger.logger.info(
                               f'--Sucsses--  User created: {user}, Administrator created: {administrator}')
                return True
            else:
                print (f'--Failed-- we cant create this user and Administrator')
                self.logger.logger.error(
                                       f'--FAILED--   we cant create this user "{user}" and Administrator{administrator} .')
                raise CreateUserAndObjectFailedException


    def remove_airline(self, airline_id):
        self.logger.logger.debug( f'remove airline is about to happen')
        if not self.repo.get_by_condition(AirlineCompany,
                                              lambda query: query.filter(AirlineCompany.id == airline_id).all()):
            print(f'Failed, we cant find  this airline company id {airline_id}')
            self.logger.logger.error(
                                   f'--FAILED--    we cant find  this airline company id {airline_id}')
            return False
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
                return
        self.repo.delete(AirlineCompany, airline_id)
        self.logger.logger.info(
                                   f'--Sucsses--  airline company id {airline_id} is removed')
        return True

    def remove_customer(self, customer_id):
        self.logger.logger.debug( f'remove customer is about to happen')
        if not self.repo.get_by_condition(Customer,
                                              lambda query: query.filter(Customer.id == customer_id).all()):
            print(f'Failed, we cant find  this Customer  id {customer_id}')
            self.logger.logger.error(
                                   f'--FAILED--    we cant find  this customer id {customer_id}')
            return False
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
        self.repo.delete(Customer, customer_id)
        self.logger.logger.info(
                                   f'--Sucsses--  customer id {customer_id} is removed')
        return True

    def remove_administrator(self, admin_id):
        self.logger.logger.debug( f'remove admin is about to happen')
        if not self.repo.get_by_condition(Administrator,
                                              lambda query: query.filter(Administrator.id == admin_id).all()):
            print(f'Failed, we cant find  this admin  id {admin_id}')
            self.logger.logger.error(
                                   f'--FAILED--    we cant find  this admin id {admin_id}')
            return False
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
        self.repo.delete(Administrator, admin_id)
        self.logger.logger.info(
                                   f'--Sucsses--  admin id {admin_id} is removed')
        return True