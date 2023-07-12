import psutil
import time
import argparse
import sys

def print_connections(filter_programs):
    connections = psutil.net_connections(kind='inet')
    for connection in connections:
        if connection.status == psutil.CONN_ESTABLISHED:
            pid = connection.pid
            process = psutil.Process(pid)
            if process.name() not in filter_programs:
                if connection.raddr and not connection.raddr.ip.startswith('127.0.0.'):
                    print_connection(process, connection)
                        
def print_connection(process, connection):
    print(f'Process name: {process.name()}')
    print(f'Local address: {connection.laddr}')
    print(f'Remote address: {connection.raddr}')
    print(f'PID: {connection.pid}')
    print('------')

def parse_arguments(args):
    parser = argparse.ArgumentParser(description="Print network connections, filtering out specified programs.")
    parser.add_argument('-e', '--exclude', nargs='*', default=[], help='List of program names to exclude.')
    return parser.parse_args(args)

def main(args):
    parsed_args = parse_arguments(args)
    filter_programs = parsed_args.exclude
    # infinite loop that prints connections every second
    while True:
        print_connections(filter_programs)
        time.sleep(1)

if __name__ == '__main__':
    main(sys.argv[1:])
