FROM python:3.9-slim

WORKDIR /bot

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY bot/bot.py .

CMD ["python", "bot.py"]