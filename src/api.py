from flask import Flask, Response, request
from dotenv import load_dotenv

import os, pathlib, schedule, time

import threading

root_path = pathlib.Path(__file__).parent.resolve()
envars = f'{root_path}/../.env'
load_dotenv(envars)

HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')

app = Flask(__name__)

def job(seconds):
    print(f"I'm working after {seconds}s...")
    return schedule.CancelJob

def run_scheduler_check():
    while True:
        schedule.run_pending()
        time.sleep(0.100)

@app.route("/")
def index():
    return "Ok"

@app.route('/create', methods=["POST"])
def create():
    content = request.json

    if "seconds" not in content:
        return "Missing seconds", 400

    seconds = content["seconds"]
    
    try:
        schedule.every(seconds).seconds.do(job, seconds=seconds)
        print(seconds)
        schedule.run_pending()
        return "Task scheduled", 201
    except Exception as e:
        return f"Error creating schduler {str(e)}"


thread = threading.Thread(target=run_scheduler_check)
thread.daemon = True                            
thread.start() 

if __name__ == "__main__":
    app.run(host=HOSTNAME, port=PORT)


