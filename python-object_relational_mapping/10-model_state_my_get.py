#!/usr/bin/python3
# task 10
"""
prints the State object with the name passed as argument from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    rows = session.query(State).all()

    res = ""
    for row in rows:
        if argv[4] in row.__dict__['name']:
            res = row.__dict__['id']

    if res == "":
        print("Not Found")
    else:
        print(res)

    session.close()
