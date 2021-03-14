import yaml
import os

CONFIG_FILE = 'config.yml'


def read():
    if not os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as config_file:
            write_default_config(config_file)
            print(f'{config_file.name} created, configure it.')
            exit(0)

    with open(CONFIG_FILE, 'r') as config_file:
        return yaml.load(config_file, yaml.FullLoader)


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
                'host': 'mc.hypixel.net',
                'port': 25565,
                'timeout': 1,
                'tags': {
                    'server_name': 'Hypixel',
                    'server_type': 'mg',
                    'server_region': 'US'
                }
            }
        ],
        "ping_period": 1
    }

    yaml.dump(config, config_file, indent=2, allow_unicode=True, sort_keys=False)
