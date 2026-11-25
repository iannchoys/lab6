\# Лабораторная работа №6



\*\*ФИО:\*\* Егорова Анна Антоновна



\*\*Группа:\*\* 220042-11



\*\*Вариант:\*\* 5



\*\*Дисциплина:\*\* Методы и технологии программирования



\## Тема



Веб-программирование на Python. Flask, FastAPI, REST API, WebSocket и Pydantic.



\## Выполненные задания



\### Задания средней сложности



\- №1 — Flask-приложение Hello World.

\- №5 — веб-страница с использованием Bootstrap.

\- №7 — FastAPI endpoint, возвращающий JSON.



\### Задания повышенной сложности



\- №6 — многопользовательский чат с использованием WebSocket и FastAPI.

\- №8 — использование Pydantic-схем для проверки и обработки данных.



\## Структура проекта



\- `task\_medium\_1.py` — Flask Hello World.

\- `task\_medium\_5.py` — Flask-приложение с Bootstrap.

\- `task\_medium\_7.py` — FastAPI JSON endpoint.

\- `task\_hard\_6.py` — WebSocket-чат.

\- `task\_hard\_8.py` — API с Pydantic-схемами.

\- `templates/` — HTML-шаблоны.

\- `tests/` — автоматические тесты.



\## Установка зависимостей



```bash

python -m pip install -r requirements.txt

```



\## Запуск приложений



Flask Hello World:



```bash

python task\_medium\_1.py

```



Bootstrap:



```bash

python task\_medium\_5.py

```



FastAPI JSON:



```bash

python -m uvicorn task\_medium\_7:app --reload --port 8000

```



WebSocket-чат:



```bash

python -m uvicorn task\_hard\_6:app --reload --port 8001

```



Pydantic API:



```bash

python -m uvicorn task\_hard\_8:app --reload --port 8002

```



\## Проверка проекта



Компиляция:



```bash

python -m py\_compile task\_medium\_1.py task\_medium\_5.py task\_medium\_7.py task\_hard\_6.py task\_hard\_8.py

```



Проверка PEP 8:



```bash

python -m flake8 . --exclude=.git,\_\_pycache\_\_,.venv,venv

```



Автоматические тесты:



```bash

python -m unittest discover -s tests -p "test\_\*.py" -v

```



\## Примечание



Для WebSocket-чата используется браузерный интерфейс. Данные студентов в Pydantic-приложении хранятся в оперативной памяти и сбрасываются после перезапуска сервера.

