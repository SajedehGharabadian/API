FROM python

WORKDIR /expert_app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./expert_app ./expert_app

CMD ["uvicorn", "expert_app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]