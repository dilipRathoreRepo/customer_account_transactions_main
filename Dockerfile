FROM python:3.7-slim as runtime
WORKDIR /home
COPY src /home
COPY requirements.txt /home
RUN pip3 install -r requirements.txt
FROM runtime as test
ENV PYTHONPATH=/home
ENTRYPOINT ["python3"]
CMD ["main.py"]