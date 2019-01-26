FROM python:3.6-slim

WORKDIR /Sunshine
COPY . /Sunshine

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "Sunshine.py"]
