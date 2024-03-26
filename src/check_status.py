from src.database import CRUD
import datetime

c = CRUD()

async def check_status():
    d = datetime.datetime.now()
    for user_id, end_date, status in c.get_status_user_task():
        if status == "ok":
            if d > end_date:
                c.update_val(user_id, "not_sub")


    print("Всё проверено")

