from src.database import engine
from src.models import Users


def creat():
    Users.metadata.create_all(engine)


creat()