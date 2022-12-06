#!/usr/bin/python3
""" Module for this file """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State
    from relationship_city import Base, City

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state_obj in session.query(State):
        print("{}: {}".format(state_obj.id, state_obj.name))
        for city_obj in state_obj.cities:
            print("\t{}: {}".format(city_obj.id, city_obj.name))
