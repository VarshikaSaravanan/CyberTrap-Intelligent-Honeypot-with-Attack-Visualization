import json
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "logs.txt")

def log_attack(ip, port, data):
    log = {
        "time": str(datetime.now()),
        "ip": ip,
        "port": port,
        "data": data
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log) + "\n")