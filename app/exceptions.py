from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Пользователь не найден'


class TokenIncorrectException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный токен'


class UserIncorrectException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'У пользователя нет такой записи'


class AudiofileTypeIncorrectException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Неверный формат аудиофайла'


class AudiorecordNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Запись не найдена'
