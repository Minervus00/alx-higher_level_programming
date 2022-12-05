#!/usr/bin/python3
""" Module for this file """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import Base, City

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State.name, City.id, City.name).join(
            State, City.state_id == State.id).order_by(City.id):
        print(f"{state[0]}: ({state[1]}) {state[2]}")
