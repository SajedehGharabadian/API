FROM python

WORKDIR /app  

# 
COPY ./requirements.txt ./requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
#
COPY ./app ./app
# 
CMD ["uvicorn", "app.main:app","--proxy-headers", "--host", "0.0.0.0", "--port", "80"]