from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

# Table 1: The Room (Meetup Plan)
class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(String(50), primary_key=True)
    created_at = Column(DateTime, server_default=func.now())

# Table 2: The Data Bucket (Friends' Info)
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(50), ForeignKey("sessions.session_id"))
    latitude = Column(Numeric, nullable=False)
    longitude = Column(Numeric, nullable=False)
    budget = Column(Numeric)

# Table 3: The Flex Table (Final Meetup Details)
class FinalMeetup(Base):
    __tablename__ = "final_meetups"

    meetup_id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(50), ForeignKey("sessions.session_id"))
    venue_name = Column(String)
    venue_type = Column(String)
    final_budget = Column(Numeric)