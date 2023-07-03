import uuid
from sqlalchemy import UUID, Column, DateTime, String
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    access_token = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __str__(self):
        return f'User {self.username}'
