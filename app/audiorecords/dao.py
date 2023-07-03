from app.dao.base import BaseDAO
from app.audiorecords.models import Audiorecord


class AudiorecordDAO(BaseDAO):
    model = Audiorecord
