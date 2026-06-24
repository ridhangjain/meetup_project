from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The Magic Connection String
# Format: postgresql://username:password@server_address:port/database_name
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD_HERE@localhost:5432/meetup_db"

# Engine is the actual bridge
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is the vehicle that carries data over the bridge
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the blueprint for our Python models
Base = declarative_base()