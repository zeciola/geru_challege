from dataclasses import dataclass
from sqlalchemy import (Column, Integer, Text, Table, Date, Float)

from .meta import Base


@dataclass
class UserSession(Base):
    __tablename__ = 'user_session'
    id = Column(Integer, primary_key=True)
    session_date = Column(Date)
    session_path = Column(Text)
    session_browser = Column(Text)
    session_timestamp = Column(Float)
    session_pdtb_id = Column(Text)
