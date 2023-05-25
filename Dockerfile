FROM python:3.9
WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
# Set the environment variable for Flask
ENV FLASK_APP=api.app:create_app
ENV FLASK_ENV=production

CMD ["python", "-m", "api.app", "development", "--port=5000"]
