# Entities Extractor

## Описание

Сервис предназначен для поиска именованных сущностей в тексте.

Умеет находить следующие виды сущностей:

- `PER` - Person
- `LOC` - Location
- `DATE` - Date
- `EVE` - Event
- `ORG` - Organization
- `DIS` - Disease
- `MEDIA` - Media

## Ядро

Ядром сервиса является предобученная модель [ner-english-fast](https://huggingface.co/flair/ner-english-fast). Дополнительно модель была обучена на датасете [multinerd](https://github.com/Babelscape/multinerd).

F1-score модели: 0.7

## Конфигурация

Модель можно запустить как на CPU, так и на GPU. Для запуска на графическом ядре необходимо выставить переменную окружения `USE_GPU=1`

## Deployment

Билд образа:

```bash
docker build -t entities_extractor:stable .
```

Запуск:

```bash
docker run -p 7890:7890 entities_extractor:stable
```

Пример docker-compose файла

```yml
version: '3'

services:
  entities_extractor:
    container_name: entities_extractor
    image: entities_extractor:stable
    environment:
        - USE_GPU=1
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```
