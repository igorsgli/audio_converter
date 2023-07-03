# Audio Converter (from wav to mp2) / Аудио Конвертер (из wav в mp3)
A mini web service that allows the user to convert audio recordings from wav format to mp3 format, save the converted recordings to a database and provide links for downloading the audio recording.
The user in the database is created with the username. When a user is created, a unique user ID and UUID access token (as a string) is generated for that user.
When passing an audio recording in wav format, a unique user ID and an access token to the web service, the audio recording is converted to mp3 format, saved to the database, and a unique UUID identifier for the recording is generated.
An audio recording is accessed via a URL link containing information about the UUID of the audio recording ID and the UUID of the user ID.
The repository provides instructions for building a docker image of the service, configuring it, and running it. As well as examples of requests to web service methods.
***********************
Мини веб-сервис, позволяющий пользователю преобразовывать аудиозаписи из формата wav в формат mp3, сохранять конвертированные записи в базу данных и предоставлять ссылки для скачивания аудиозаписи.
Пользователь в базе данных создается по заданному имени, при этом генерируется уникальный идентификатор пользователя и UUID токен доступа (в виде строки) для этого пользователя.
При передаче в веб-сервис аудиозаписи в формате wav, уникального идентификатора пользователя и токена доступа, аудиозапись преобразуется в формат mp3, сохраняется в базу данных, и генерируется уникальный UUID идентификатор записи.
Доступ к аудиозаписи осуществляется по URL ссылке содержащей информацию c UUID идентификатора аудиозаписи и UUID идентификатора пользователя.
В репозитории предоставлены инструкции по сборке докер-образа сервиса, их настройке и запуску. А также примеры запросов к методам веб-сервиса.

**Stack / Стек**:
* Python
* FastAPI
* PostgresSQL
* SQLAlchemy
* Pydantic
* pydub/ffmpeg
* Gunicorn
* Docker
* Swagger

## Launch the project / Инструкции по запуску

### 1. Git clone / Клонировать репозиторий:
```
git clone https://github.com/igorsgli/audio_converter.git
cd audio_converter
```
### 2. Install depencies / Установить зависимости:
```
pip install -r requirements.txt
```
### 3. Rename .env_example to .env / Переименовать файл .env_example в .env:
```
mv ./.env_example ./.env
```
### 4. Run docker-compose / Запустить docker-compose:
```
docker-compose up -d --build
```
### 5. Project documentation is available at / Документация доступна по адресу:
```
http://localhost:8000/docs
```
### 6. API requests examples / Примеры API запросов:
1. User creation. Username is passed in the body of the POST request. / Создание пользователя. В теле POST запроса передается имя пользователя.
```
POST http://localhost:8000/users/
Request body / Тело запроса
{
  "username": "user1"
}
Response / Ответ
{
  "id": "05ac7e00...",
  "access_token": "44cd9cd8..."
}
```
2. Receiving by user of his data by id. / Получение пользователем своих данных по id.
```
GET http://localhost:8000/users/me?user_id=05ac7e00-a7d1...
Response / Ответ
{
  "id": "05ac7e00...",
  "username": "user1",
  "access_token": "44cd9cd8...",
  "created_at": "2023-07-01T18:43:35.091Z"
}
```
3. Adding record by user by user_id and access_token. / Добавление пользователем аудиозаписи по user_id и access_token.
```
POST http://localhost:8000/add_record?user_id=05ac7e00...&access_token=44cd9cd8...
Request body / Тело запроса
file (Upload file)
string($binary)

Response / Ответ
"http://localhost:8000/record?id=8e8bc00a...&user=05ac7e00..."
```
4. Getting record to download by record id and user id. / Получение аудиозаписи для загрузки по id (id аудиозаписи) и user (id пользователя).
```
GET http://localhost:8000/record?id=8e8bc00a...&user=05ac7e00...
Response / Ответ
Download file (link to download file)
```
5. Getting a list of user's records by their id and access_token. / Получение списка аудиозаписей пользователя по его id и access_token.
```
GET http://localhost:8000/get_records_list?user=05ac7e00...&access_token=44cd9cd8...
Response / Ответ
[
  {
    "id": "8e8bc00a...",
    "user": "05ac7e00...",
    "filename": "sample.mp3"
  }
  ...
]
```
