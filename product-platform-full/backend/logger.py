from datetime import datetime

def log(msg):
    with open("data/logs.txt","a",encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {msg}\n")
