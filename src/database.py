import datetime

from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from src.models import Users

DB_NAME = "subscriptions.sqlite"

engine = create_engine(f'sqlite:///{DB_NAME}')
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        return db
    finally:
        db.close()


class CRUD:

    def create_user(self, user_id, end_date, role=0, status="not_sub"):
        with get_db() as session:
            query = session.query(Users).filter(Users.user_id == user_id).first()
            if query:
               return "f"
            date = datetime.datetime.now() + datetime.timedelta(days=end_date)
            data = Users(user_id=user_id, end_date=date, role=role, status=status)
            session.add(data)
            session.commit()
            session.refresh(data)
            return data

    def get_admin_id(self, role):
        with get_db() as session:
            query = session.query(Users).filter(Users.role == role).first()
            if query:
                return query.user_id
            else: None

    def get_status_user(self, user_id):
        with get_db() as session:
            query = session.query(Users).filter(Users.user_id == user_id).first()
            if query:
                return query.status
            else: return 404

    def get_status_user_task(self):
        with get_db() as session:
            query = session.query(Users.user_id, Users.end_date, Users.status)  # Указать желаемые столбцы
            results = query.all()
            return results

    def get_endtime_user(self, user_id):
        with get_db() as session:
            query = session.query(Users).filter(Users.user_id == user_id).first()
            if query:
                return query.end_date
            else: return 404
    def update_val(self, user_id, new_status):
        with get_db() as session:
            stmt = update(Users).values(status=new_status).where(Users.user_id==user_id)
            session.execute(stmt)
            session.commit()


