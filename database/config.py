import os.path

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

Base = declarative_base()

CREATE_CHARACTER_TABLE = """ CREATE TABLE IF NOT EXISTS characters (
    id integer PRIMARY KEY,
    name string NOT NULL
);
"""

CREATE_DIALOG_TABLE = """ CREATE TABLE IF NOT EXISTS dialogs (
    id integer PRIMARY KEY,
    choice_path integer NOT NULL,
    character_id integer NOT NULL,
    FOREIGN KEY (character_id) REFERENCES characters (id)
);
"""

def initialize():
    database_path = os.path.join("database", "dialogues.db")
    # Create a new database file if it does not yet exist.
    if not os.path.isfile(database_path):
        open(database_path, "w+")

    # Create tables.
    connection = None
    try:
        connection = sqlite3.connect(database_path)
    except sqlite3.Error as ex:
        print("Unable to connect to database.")
        print(ex)
        return None
    try:
        cursor = connection.cursor()
        cursor.execute(CREATE_CHARACTER_TABLE)
        cursor.execute(CREATE_DIALOG_TABLE)
    except sqlite3.Error as ex:
        print("Unable to create new tables.")
        print(ex)
        return None
    connection.close()
    

    # Connect to the database.
    engine = create_engine(f"sqlite:///{database_path}")
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    # connection = engine.connect()

    return session

# character_dialog = Table(
#     "character_dialog",
#     Base.metadata,
#     Column("character_id", Integer, ForeignKey("character.id")),
#     Column("dialog_id", Integer, ForeignKey("dialog.id"))
# )

class Character(Base):
    """A character is one that speaks the dialogs.
    One character can have multiple dialogs.
    """
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dialogs = relationship(
        "Dialog", backref=backref("dialogs") # secondary=character_dialog,
    )
    
class Dialog(Base):
    """Dialogue objects contain multiple questions/statements.
    A dialogue flows based on the 4 choices that are made.
    Each dialogue part is 4 bits, based on the choice the player made.
    All dialogue parts are strewn together, creating a series of bits. (choice path)
    """    
    __tablename__ = "dialogs"
    id = Column(Integer, primary_key=True)
    choice_path = Column(Integer)
    character_id = Column(Integer, ForeignKey("characters.id"))

