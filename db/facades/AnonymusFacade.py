from BaseFacade import BaseFacade
from db.tables.Administrator import Administrator
from db.tables.Customer import Customer
from errors.UserAlreadyExistException import *
from db.tables.User import User
from db.tables.AirlineCompany import AirlineCompany
from db.LoginToken import LoginToken
from db.facades.AirLineFacade import AirLineFacade
from db.facades.AdministratorFacade import AdministratorFacade
from CustomerFacade import CustomerFacade
from logger import Logger




class AnonymusFacade(BaseFacade):


    def __init__(self):
        super().__init__()
        self.logger = Logger.get_instance()


    def login(self, username, password):
        user = self.repo.get_by_condition(User, lambda query: query.filter(User.username == username).all())
        if not user:
            print('Faild, we didnt find that user.')
            self.logger.logger.error(
                                   f'--FAILED--  we didnt find that user "{username}"')
            return
        else:
            passw= self.repo.get_by_condition(User, lambda query: query.filter(User.password == password).all())
            if not passw:
                print('Faild, wrong password.')
                self.logger.logger.error(
                                       f'--FAILED--   wrong password for user "{username}"')
                return
            else:
                self.logger.logger.info(
                                   f'--Sucsses-- the password is match for user "{username}"')
                if user[0].user_role == 1:
                    airline_=self.repo.get_by_condition(AirlineCompany, lambda query: query.filter(AirlineCompany.user_id == user[0].id).all())
                    login_token = LoginToken(id=airline_[0].id, name=airline_[0].name, role=user[0].user_role)
                    self.logger.logger.info(
                                           f'--Sucsses-- the user "{username}" transferred to Airline Facade  ')
                    return (AirLineFacade(login_token))
                elif user[0].user_role == 2:
                    customer_=self.repo.get_by_condition(Customer, lambda query: query.filter(Customer.user_id == user[0].id).all())
                    login_token = LoginToken(id=customer_[0].id, name=customer_[0].first_name, role=user[0].user_role)
                    self.logger.logger.info(
                                           f'--Sucsses-- the user "{username}" transferred to Customer Facade  ')
                    return (CustomerFacade(login_token))
                elif user[0].user_role == 3:
                    self.logger.logger.info(
                                           f'--Sucsses-- the user "{username}" transferred to Admin Facade  ')
                    admin= self.repo.get_by_condition(Administrator, lambda query: query.filter(Administrator.user_id == user[0].id).all())
                    login_token = LoginToken(id=admin[0].id, name=admin[0].first_name, role=user[0].user_role)
                    return (AdministratorFacade(login_token))


    def create_new_user(self, user):
        username=self.repo.get_by_condition(User, lambda query: query.filter(User.username == user.username).all())
        if username:
            self.logger.logger.error(
                                   f'--FAILED--   The username "{username[0].username}"  is alrady exist ')
            raise UserAlreadyExistException()
        else:
            email=self.repo.get_by_condition(User, lambda query: query.filter(User.email == user.email).all())
            if email:
                print(f' Faild, the email {email[0].email} is alrady exist ')
                self.logger.logger.error(
                                       f'--FAILED--   The email "{email[0].email}"  is alrady exist ')
            self.repo.add(user)
            self.logger.logger.info(
            f'--Sucsses-- the user "{user.username}"  was created successfully, his details:   user id:{user.id} email:{user.email}, user role:{user.user_role}  ')
            return True