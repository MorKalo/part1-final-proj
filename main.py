from db.DbRepo import DbRepo
from db.Db_config import local_session, create_all_entities
from Init_db import Init_db


repo = DbRepo(local_session)

init=Init_db()
init.reset_all_db()
create_all_entities()
init.insert_test_db()

