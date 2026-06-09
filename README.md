# Gudkova_AS_final_project
Дипломная работа

## Фреймворк автоматизации тестирования для сервиса «Кинопоиск»
Фреймворк предназначен для автоматизации функционального тестирования веб‑сервиса «Кинопоиск». Он позволяет проверять корректность работы UI и API, обеспечивая высокое покрытие тестами ключевых сценариев взаимодействия пользователя с сервисом.

### Стек технологий:
- pytest — фреймворк для написания и запуска тестов;
- selenium — автоматизация взаимодействия с веб‑браузером;
- requests — работа с HTTP‑запросами (в т. ч. API);
- allure — генерация наглядных отчётов по результатам тестирования;

### Структура:
- /test - тесты
- /pages - описание страниц
- requirements.txt - список зависимостей
- README.md - документация к проекту
- conftest.py - фикстура для тестов

### Ключевые компоненты
1. Использование Page Object
2. Конфигурация: файл .env хранит BASE_API_URL сервиса кинопоск, токен API Кинопоиск и BASE_URL сервиса Кинопоск
3. Тесты разделены на группы:
- UI‑тесты (test/test_ui.py) — проверяют корректность отображения элементов и работу интерфейса;
- API‑тесты (test/test_api.py) — тестируют бизнес‑логику через прямые вызовы API

### Шаги  по настройке и запуску
#### Создание удаленного репозитория
- Склонировать проект 'git clone https://github.com/astiwet/Gudkova_AS_final_project.git

#### Установление зависимостей:
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
= pip install requests

#### Получение токена для сервиса Кинопоиск
1. Перейдите в телеграм-бота: @kinopoiskdev_bot
2. Нажмите Start (или /start), затем нажмите кнопку 🔑 Получить токен (Get token)
3. Бот пришлет вам ключ вида XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX. Скопируйте его

#### Настройка токена
1. Откройте файл .env.
2. Добавьте строку: API-KEY = 'ваш_скопированный_токен'
3. Использовать os.getenv("API_KEY") вместо ключа

#### Запуск тестов
Проект поддерживает три режима запуска через маркеры:
- pytest -m "ui"
- pytest -m "api"
- pytest

### Полезные ссылки
 https://docs.pytest.org/en/stable/ — официальная документация фреймворка pytest.
 https://www.selenium.dev/documentation/ — руководство по работе с Selenium WebDriver.
 https://allurereport.org/docs/— настройка и использование Allure Reports.
 https://requests.readthedocs.io/en/latest/ - документация библиотеки Requests
 https://www.markdownguide.org/basic-syntax/— шпаргалка по синтаксису Markdown.
 https://testanastasia.yonote.ru/share/84763900-b249-4118-bbc6-b52f8f7a3c61 - финальный проект по ручному тестированию