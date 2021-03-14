# GimmePing

Minecraft servers pinger with `InfluxDB` backend.

Supports mc `1.7+ versions`.

## Requirements

- Python 3

## Installation

0. Grab the latest version from releases
1. Run `pip3 install -r requirements.txt`
2. Run `python3 main.py`
3. Configure `config.yml`
4. Repeat `step 2`

## Configuration format

```
influx_db:                 # InfluxDB configuration
  host: localhost          # Host
  port: 8086               # Port
  username: root           # Username
  password: root           # Password
  database: _internal      # Database
  # You can specify more parameters: https://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdbclient

servers:                   # Servers for ping
  - host: mc.hypixel.net   # Server host
    port: 25565            # Server port
    timeout: 1.0           # Max ping timeout in seconds
    tags:                  # Tags for Influx point
      server_name: Hypixel # Server name
      server_type: mg      # Server type
      server_region: US    # Server region 
      # You can add more tags here or remove some of them

ping_period: 1.0           # Delay between pings in seconds
```