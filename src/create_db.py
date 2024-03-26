from database import engine
from models import Users


def creat():
    Users.metadata.create_all(engine)


creat()