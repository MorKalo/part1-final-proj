import pytest
from Init_db import *
import time
from db.DbRepo import DbRepo
from db.facades.AirLineFacade import AirLineFacade
from db.facades.CustomerFacade import CustomerFacade
from db.facades.AdministratorFacade import AdministratorFacade

repo=DbRepo(local_session)

@pytest.fixture(scope='session', autouse=True)
def dao_connection_test():
    return AnonymusFacade()


@pytest.fixture(scope='function', autouse=True)
def dao_reset_db(dao_connection_test):
    init=Init_db()
    init.reset_all_db()
    create_all_entities()
    init.insert_test_db()
    return

@pytest.fixture(scope='function', autouse=True)
def dao_init():
    print('testing initialize')
    yield()
    print('cleanup, after')
    time.sleep(3)

@pytest.mark.parametrize('username, password, expected', [('turkish', '97', AirLineFacade)
                                                         ,('pninosh', '786', CustomerFacade),
                                                          ('Moti5k', '232', AdministratorFacade),
                                                          ])
def test_login(dao_connection_test, username, password, expected):
    actual=dao_connection_test.login(username, password)
    assert isinstance(actual, expected)