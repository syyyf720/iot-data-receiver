from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///data.db'

engine = create_engine(DATABASE_URI, echo=True)

Session = sessionmaker(bind=engine)