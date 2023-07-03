import aiofiles
import base64
import os
import pydub
import shutil
import uuid

from fastapi import UploadFile

from app.audiorecords.dao import AudiorecordDAO
from app.users.dao import UserDAO
from app.config import settings
from app.exceptions import (
    AudiofileTypeIncorrectException, AudiorecordNotFoundException,
    TokenIncorrectException, UserIncorrectException,
    UserNotFoundException
)


async def check_user(user_id: uuid.UUID, access_token: str):
    user = await UserDAO.find_one_or_none(id=user_id)
    if user is None:
        raise UserNotFoundException
    if user.access_token != access_token:
        raise TokenIncorrectException
    return user


def check_file_and_get_filename(file: UploadFile):
    file_name, ext = file.filename.split('.')
    if ext != 'wav':
        raise AudiofileTypeIncorrectException
    return file_name


def audiofile_path(filename: str, extension: str):
    return os.path.join(settings.PATH_AUDIO, f'{filename}.{extension}')


def convert_wav_to_mp3(file: UploadFile, file_name: str):
    file_wav_path = audiofile_path(file_name, 'wav')
    file_mp3_path = audiofile_path(file_name, 'mp3')
    with open(file_wav_path, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)
        sound = pydub.AudioSegment.from_wav(file_wav_path)
        sound.export(file_mp3_path, format='mp3')
        os.remove(file_wav_path)


async def add_audiorecord_to_db(file_name: str, user_id: uuid.UUID):
    file_mp3_path = audiofile_path(file_name, 'mp3')
    async with aiofiles.open(file_mp3_path, 'rb') as file_object:
        audio_file = base64.b64encode(await file_object.read())
        data = {
            'filename': f'{file_name}.mp3',
            'file': audio_file,
            'user': user_id,
        }
        record = await AudiorecordDAO.add(**data)
        os.remove(file_mp3_path)
        return record


async def check_audiorecord(id: uuid.UUID, user: uuid.UUID):
    record = await AudiorecordDAO.find_one_or_none(id=id)
    if record is None:
        raise AudiorecordNotFoundException
    if record.user != user:
        raise UserIncorrectException
    return record


async def prepare_record_for_download(record, path):
    record_file = base64.b64decode(record.file)
    async with aiofiles.open(path, 'wb') as file_object:
        await file_object.write(record_file)


async def records_list(user_id: uuid.UUID):
    records = await AudiorecordDAO.find_all(user=user_id)
    result = []
    for record in records:
        result.append(
            {
                'id': record.id,
                'user': record.user,
                'filename': record.filename,
            }
        )
    return result
