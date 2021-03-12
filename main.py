import socket
import time
import traceback

from influxdb import InfluxDBClient

import config
import pinger


def ping_servers(servers, influx_client):
    points = []
    for server in servers:
        try:
            ping_data = pinger.ping(**server)
            if not ping_data:
                continue
        except socket.timeout:
            continue
        except:
            print(f'Error pinging {server["host"]}:{server.get("port", 25565)}. Timeout was {server.get("timeout", 1)}')
            traceback.print_exc()
            continue

        points.append({
            "measurement": "servers_stats",
            "tags": {
                "server": server['server_name']
            },
            "time": int(round(time.time() * 1000)),
            "fields": {
                'online': ping_data['players']['online']
            }
        })

    if points:
        try:
            influx_client.write_points(points, time_precision='ms')
        except:
            print(f'Error writing points to influx db: {points}')
            traceback.print_exc()


def main():
    cfg = config.read()

    influx_client = InfluxDBClient(**cfg['influx_db'])
    servers = cfg['servers']

    ping_period = cfg.get('ping_period', 1)

    while True:
        ping_servers(servers, influx_client)
        time.sleep(ping_period)


if __name__ == '__main__':
    main()
