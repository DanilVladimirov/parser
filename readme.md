# Для запуску проекту потрібно:

### 1. Підняти базу даних, запустивши скрипт start_db.sh або ж самому ввести 2 команди

```
docker network inspect project_parser >/dev/null 2>&1 || docker network create --driver bridge project_parser
```

```
docker-compose --env-file=backend/.env up -d --build
```

після чого бд автоматично запустить dump.sql, який містить зібрані дані.


### 2. перейти в директорію backend, встановити та активувати venv, після чого запустити бекенд командою:

```commandline
uvicorn main:app --port 8000 --reload
```

# Ендпоінти проекту

### 1. Отримання даних з вхідного файлу по domain
http://127.0.0.1:8000/redoc#tag/urls/operation/get_urls_by_domain_urls_get_urls_by_domain_post

### 2. Отримання даних з вхідного файлу останнього відвіданого URL
http://127.0.0.1:8000/redoc#tag/urls/operation/get_latest_url_info_urls_latest_url_info_post

повна документація доступна ось тут

http://127.0.0.1:8000/redoc
