FROM python:3

WORKDIR /app/backend

COPY ./backend/requirements.txt /app/backend/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend /app/backend

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]