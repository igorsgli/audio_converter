import uuid
from sqlalchemy import UUID, Column, ForeignKey, LargeBinary, String
from app.database import Base


class Audiorecord(Base):
    __tablename__ = 'audiorecords'

    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    filename = Column(String, nullable=False)
    file = Column(LargeBinary, nullable=False)
    user = Column(ForeignKey('users.id'), nullable=False)

    def __str__(self):
        return f'Audiorecord {self.filename}'
