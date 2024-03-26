FROM python:3.8

WORKDIR /app

COPY app .

CMD python -m pip install --upgrade pip 
RUN pip install --progress-bar off --no-cache-dir -r requirements.txt 

EXPOSE 8051 

CMD python app.py 
