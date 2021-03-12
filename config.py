import json
import os

CONFIG_FILE = 'config.json'


def read():
    if not os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as config_file:
            write_default_config(config_file)
            print(f'{config_file.name} created, configure it.')
            exit(0)

    with open(CONFIG_FILE, 'r') as config_file:
        return json.loads(json.load(config_file))


def write_default_config(config_file):
    config = {
        "influx_db": {
            "host": 'localhost',
            "port": 8086,
            "username": 'root',
            "password": 'root',
            "database": '_internal'
        },
        "servers": [
            {
                'server_name': 'Hypixel',
                'host': 'mc.hypixel.net',
                'port': 25565,
                'timeout': 1,
            }
        ],
        "ping_period": 1
    }

    json.dump(json.dumps(config), config_file, indent=4)
