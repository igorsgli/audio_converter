import os
import uuid

from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from app.audiorecords.schemas import SAudioInfo

from app.audiorecords.utlils import (
    add_audiorecord_to_db, audiofile_path, check_audiorecord,
    check_file_and_get_filename, check_user, convert_wav_to_mp3,
    prepare_record_for_download, records_list
)
from app.config import settings


router = APIRouter(
    prefix='',
    tags=['Audiorecords'],
)


@router.post('/add_record')
async def convert_and_add_record(
    user_id: uuid.UUID,
    access_token: str,
    file: UploadFile
) -> str:
    await check_user(user_id, access_token)
    file_name = check_file_and_get_filename(file)
    convert_wav_to_mp3(file, file_name)
    record = await add_audiorecord_to_db(file_name, user_id)
    url_download = os.path.join(
        settings.URL_PATH,
        f'record?id={record.id}&user={user_id}'
    )
    return url_download


@router.get('/get_record')
async def get_and_download_record(id: uuid.UUID, user: uuid.UUID):
    record = await check_audiorecord(id, user)
    file_mp3_path = audiofile_path('audio_file', 'mp3')
    await prepare_record_for_download(record, file_mp3_path)
    return FileResponse(
        file_mp3_path,
        media_type='application/octet-stream',
        filename=record.filename
    )


@router.get('/get_records_list')
async def get_records_list(
    user: uuid.UUID, access_token: str
) -> list[SAudioInfo]:
    await check_user(user, access_token)
    return await records_list(user)
