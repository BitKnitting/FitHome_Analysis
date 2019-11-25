from flask import Blueprint
from flask import request

from .extensions import mongo
from datetime import datetime

main = Blueprint('main', __name__)

MICROWAVE_ON = 0
@main.route('/')
def index():
    now = datetime.now()

# Add a monitor reading to the db
@main.route('/monitor', methods=['POST'])
def monitor():
    global MICROWAVE_ON
    if request.is_json:
        req = request.get_json()
        try:
            now = datetime.now()
            timestamp_str = str(datetime.timestamp(now))
            monitor_collection = mongo.db.monitor
            # E.g.: Reading came in from monitor.
            reading = {"timestamp": timestamp_str,
                       "Pa": req['Pa'], "I": req['I'], "Pr": req['Pr'], "microwave": MICROWAVE_ON, }
            monitor_collection.insert(reading)
        except KeyError as error:
            return (f'The key {error} does not exist.', 400)
        except Exception as error:
            return (f'An error occurred: {error}', 400)

        return 'Added a Reading!', 200
    else:
        return "Request was not JSON", 400
