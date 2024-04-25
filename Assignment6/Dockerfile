FROM python

WORKDIR /SQL_app

# 
COPY ./requirements.txt ./requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
#
COPY ./SQL_app ./SQL_app
# 
CMD ["uvicorn", "SQL_app.main:app","--proxy-headers", "--host", "0.0.0.0", "--port", "80"]