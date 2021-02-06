# Celery
from celery import Celery
from celery.schedules import crontab
# Sqlite
from sqlalchemy import create_engine
# Utils
from  dotenv  import  load_dotenv
from os import getenv
import uuid
import requests
from datetime import datetime


load_dotenv(verbose=True)
db_connect = create_engine('sqlite:///database/data.db')

broker= "redis://:p53460ffb5359262bb4fa7060ce87f349dcb35ac43ad7361e4eaf744c9a58e84e@ec2-54-175-165-24.compute-1.amazonaws.com:11769"
app = Celery('project', broker=broker)

@app.task
def check_weather():
    response = requests.get('https://dweet.io:443/get/latest/dweet/for/thecore', timeout=2)
    content = response.json().get('with')[0].get('content')
    temperature = content.get('temperature')
    humidity = content.get('humidity')

    conn = db_connect.connect()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(f'insert into weather (id, variable, value, created_at) values (1, "temperature", {temperature}, "03/21/2020");')
    conn.execute(f'insert into weather (id, variable, value, created_at) values (2, "humidity", {humidity}, "06/12/2020");')


app.conf.beat_schedule = {
    "check_the_weather": {
        "task": "project.check_weather",
        "schedule": crontab(minute="*")
    }
}
