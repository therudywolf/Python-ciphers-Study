FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-tk \
    tk \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

ENV DISPLAY=:0
ENV PYTHONUNBUFFERED=1

CMD ["python", "GUI/Visual_Algorithms_final.py"]
