FROM kivy/buildozer:latest

ENV USE_SYSTEM_PACKAGES=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

RUN buildozer android debug
