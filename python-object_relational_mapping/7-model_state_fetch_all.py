#!/usr/bin/python3
# task 7
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    rows = session.query(State).all()

    for row in rows:
        print("{}: {}".format(row.__dict__['id'], row.__dict__['name']))

    session.close()
