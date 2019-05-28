from app import database as db
from datetime import datetime
import hug
from falcon import HTTP_400, HTTP_401, HTTP_200
from dateutil.parser import parse
from sqlalchemy import types, and_, or_
from sqlalchemy import (
    func
)


@hug.get("/")
def home(request, response, **kwargs):

    database_session = db.get_session()
    employees_count = (
        database_session.query(db.Employee).count()
    )
    if employees_count == 0:
        for i in range(5):
            _i = str(i)
            employee = db.Employee(
                emp_number="TS0000" + _i,
                phone_number="082042314" + _i,
                first_name="Z" + _i,
                last_name="ZS" + _i
            )
            database_session.add(employee)
            database_session.commit()

    return "Hi"


@hug.post("/leave/")
def post(request, response, **kwargs):

    response.status = HTTP_400
    start_date_obj = None
    end_date_obj = None
    database_session = None
    employee = None

    if "employee_pk" not in kwargs:
        return {"message": "employee_pk is required."}
    elif kwargs["employee_pk"] == "":
        return {"message": "employee_pk is required."}

    if "start_date" not in kwargs:
        return {"message": "start_date is required."}
    elif kwargs["start_date"] == "":
        return {"message": "start_date is required."}
    else:
        try:
            start_date_obj = parse(kwargs["start_date"]).date()
        except:
            return {"message": "an invalid start_date was supplied."}

    if "end_date" not in kwargs:
        return "end_date is required"
    elif kwargs["end_date"] == "":
        return "end_date is required"
    else:
        try:
            end_date_obj = parse(kwargs["end_date"]).date()
        except:
            return {"message": "an invalid end_date was supplied."}

    if end_date_obj < start_date_obj:
        return {"end_date cannot be earlier than the start_date."}

    employee_key = kwargs["employee_pk"]
    if employee_key.isdigit():
        database_session = db.get_session()
        employee = database_session.query(db.Employee).get(employee_key)
        if employee is None:
            return {"message": "employee could not be found."}

    date_delta = (end_date_obj - start_date_obj).days + 1

    try:
        leave = db.Leave(
            start_date=start_date_obj,
            end_date=end_date_obj,
            employee_pk=employee_key,
            status="New",
            days_of_leave=date_delta)

        employee.leave.append(leave)
        database_session.commit()
    except Exception as e:
        print(e)
        return {"message": "an error occurred while submitting leave, please try again later."}

    response.status = HTTP_200
    return {"message": "your leave was successfully submitted! Thank you!"}


if __name__ == "__main__":
    home()
