FROM python

WORKDIR /usr/src

# 
COPY ./requirements.txt ./requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
#
COPY ./SQL_app ./SQL_app
# 
CMD ["uvicorn", "main:app","--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
