# GimmePing

Minecraft servers pinger with `InfluxDB` backend.

Supports mc `1.7+ versions`.

## Requirements

- Python 3

## Installation

0. Grab the latest version from releases
1. Run `pip3 install -r requirements.txt`
2. Run `python3 main.py`
3. Configure `config.json`
4. Repeat `step 2`

## Configuration format

        {
            "influx_db": {                        # InfluxDB configuration
                "host": 'localhost',              # Host
                "port": 8086,                     # Port
                "username": 'root',               # Username
                "password": 'root',               # Password
                "database": '_internal'           # Database
            },
            "servers": [                          # Servers for ping
                {
                    'host': 'mc.hypixel.net',     # Server host
                    'port': 25565,                # Server port
                    'timeout': 1.0,               # Max ping timeout in seconds
                    'tags': {                     # Tags for Influx point
                        'server_name': 'Hypixel', # Server name
                        'server_type': 'mg',      # Server type (optional)
                        'server_region': 'US'     # Server region (optional)
                        # You can add more tags here or remove some of them
                    }
                }
                # You can add more servers here
            ],
            "ping_period": 1.0                    # Servers ping period in seconds
        }

#### Note

This is example only. You have to configure generated `config.json` file.