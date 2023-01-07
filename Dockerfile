FROM python:3.9-alpine
WORKDIR /ranked
COPY ./ /ranked
RUN apk update && python -m pip install --upgrade pip && pip install -r /ranked/requirements.txt --no-cache-dir
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
