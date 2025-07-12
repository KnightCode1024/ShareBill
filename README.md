# 🧾 ShareBill

<div align="center">

![ShareBill Logo](https://img.shields.io/badge/ShareBill-Split%20Bills%20Easily-blue?style=for-the-badge&logo=calculator)

**Умное приложение для совместного учета и деления расходов между пользователями**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.3-green.svg)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.16.0-red.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📋 Содержание

- [🚀 О проекте](#-о-проекте)
- [✨ Возможности](#-возможности)
- [🛠 Технологии](#-технологии)
- [📦 Установка](#-установка)
- [🔧 Разработка](#-разработка)
- [📚 API Документация](#-api-документация)
- [🤝 Вклад в проект](#-вклад-в-проект)
- [📄 Лицензия](#-лицензия)

---

## 🚀 О проекте

ShareBill — это современное веб-приложение для удобного разделения счетов и расходов между друзьями, коллегами или участниками мероприятий. Приложение автоматически сканирует QR-коды чеков и распределяет позиции между участниками.

### 🎯 Основные преимущества

- **📱 Автоматическое сканирование чеков** через QR-коды
- **👥 Групповое управление** мероприятиями и участниками
- **💰 Точный расчет** долей каждого участника
- **🔐 Безопасная авторизация** с JWT токенами
- **📊 Детальная аналитика** расходов

---

## ✨ Возможности

### 🧾 Управление чеками
- Загрузка и сканирование QR-кодов чеков
- Автоматическое извлечение данных о покупках
- Детализация по позициям с ценами и количеством

### 👥 Группы и мероприятия
- Создание групп участников
- Организация мероприятий с привязкой к группам
- Система приглашений через уникальные токены

### 👤 Пользователи
- Регистрация и авторизация пользователей
- Профили с фотографиями и датами рождения
- Управление личными данными

### 💰 Распределение расходов
- Выбор позиций из чека для каждого участника
- Автоматический расчет долей
- Учет чаевых и дополнительных расходов

---

## 🛠 Технологии

### Backend
- **Python 3.8+** — основной язык программирования
- **Django 5.2.3** — веб-фреймворк
- **Django REST Framework 3.16.0** — API фреймворк
- **Django REST Framework JSON API** — JSON API спецификация
- **Djoser 2.3.1** — аутентификация и авторизация
- **Pillow 11.3.0** — обработка изображений

### База данных
- **SQLite** — для разработки
- **PostgreSQL** — для продакшена (рекомендуется)

### Разработка
- **Black** — форматирование кода
- **Flake8** — линтинг
- **Pytest** — тестирование
- **Pytest-Django** — тестирование Django приложений

---

## 📦 Установка

### Предварительные требования

- Python 3.8 или выше
- pip (менеджер пакетов Python)
- Git

### Пошаговая установка

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/your-username/ShareBill.git
   cd ShareBill
   ```

2. **Создание виртуального окружения**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Установка зависимостей**
   ```bash
   pip install -r requirements/dev.txt
   ```

4. **Настройка переменных окружения**
   ```bash
   cp .env.example .env
   # Отредактируйте .env файл с вашими настройками
   ```

5. **Применение миграций**
   ```bash
   cd backend
   python manage.py migrate
   ```

6. **Создание суперпользователя**
   ```bash
   python manage.py createsuperuser
   ```

7. **Запуск сервера разработки**
   ```bash
   python manage.py runserver
   ```

Приложение будет доступно по адресу: http://localhost:8000

---

## 🔧 Разработка

### Структура проекта

```
ShareBill/
├── backend/                 # Django приложение
│   ├── api/v1/             # API версия 1
│   │   ├── events/         # Модуль мероприятий
│   │   ├── receipts/       # Модуль чеков
│   │   └── users/          # Модуль пользователей
│   ├── config/             # Настройки Django
│   ├── media/              # Загруженные файлы
│   └── manage.py           # Django management
├── requirements/            # Зависимости
│   ├── dev.txt            # Для разработки
│   ├── prod.txt           # Для продакшена
│   └── test.txt           # Для тестирования
└── README.md              # Документация
```

### Команды разработки

```bash
# Форматирование кода
black backend/

# Проверка стиля кода
flake8 backend/

# Запуск тестов
pytest

# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание фикстур
python manage.py dumpdata > fixtures/initial_data.json

# Загрузка фикстур
python manage.py loaddata fixtures/initial_data.json
```

### Переменные окружения

Создайте файл `.env` в корне проекта:

```env
# Django
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Email (для подтверждения email)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Social Auth (опционально)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

---

## 📚 API Документация

### Аутентификация

API использует JWT токены для аутентификации. Получите токен через эндпоинт `/api/v1/users/token/`.

### Основные эндпоинты

#### Пользователи
- `POST /api/v1/users/` — регистрация пользователя
- `POST /api/v1/users/token/` — получение JWT токена
- `GET /api/v1/users/me/` — информация о текущем пользователе

#### Мероприятия
- `POST /api/v1/events/` — создание мероприятия с чеком
- `GET /api/v1/events/{id}/` — получение информации о мероприятии
- `PUT /api/v1/events/{id}/` — обновление мероприятия
- `DELETE /api/v1/events/{id}/` — удаление мероприятия

#### Группы
- `POST /api/v1/events/group/join/{invite_token}/` — присоединение к группе

#### Позиции чеков
- `POST /api/v1/events/select/receipt/item/{id}/` — выбор позиции из чека
- `GET /api/v1/events/receipts/{id}/` — получение позиций чека

### Примеры запросов

#### Создание мероприятия
```bash
curl -X POST http://localhost:8000/api/v1/events/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "name=Ужин в ресторане" \
  -F "tips=10" \
  -F "receipt_img=@receipt.jpg"
```

#### Получение информации о мероприятии
```bash
curl -X GET http://localhost:8000/api/v1/events/1/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

---

## 🚧 Статус разработки

### ✅ Реализовано
- [x] Базовая структура Django проекта
- [x] Модели данных (User, Event, Receipt, ReceiptItem)
- [x] API эндпоинты для основных операций
- [x] JWT аутентификация
- [x] Сканирование QR-кодов чеков
- [x] Система групп и приглашений
- [x] Распределение позиций между участниками

### 🔄 В разработке
- [ ] Подтверждение email через SMTP сервер
- [ ] Социальная авторизация (Google, VK)
- [ ] Мобильное приложение
- [ ] Уведомления о новых расходах

### 📋 Планируется
- [ ] Интеграция с банковскими API
- [ ] Экспорт отчетов в PDF/Excel
- [ ] Многоязычность
- [ ] Темная тема
- [ ] Push-уведомления

---

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта! Вот как вы можете помочь:

1. **Fork** репозиторий
2. Создайте **feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** изменения (`git commit -m 'Add amazing feature'`)
4. **Push** в branch (`git push origin feature/amazing-feature`)
5. Откройте **Pull Request**

### Стандарты кода

- Используйте **Black** для форматирования
- Следуйте **PEP 8** стандартам
- Пишите **тесты** для новой функциональности
- Обновляйте **документацию**

---