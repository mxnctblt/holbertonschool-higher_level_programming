#!/usr/bin/python3
# task 13
"""
deletes all State objects with a name containing the letter a from the database
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

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()

    session.close()
