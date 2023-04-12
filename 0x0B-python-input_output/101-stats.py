import sys
import signal

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

def print_metrics(signal, frame):
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    sys.exit(0)

signal.signal(signal.SIGINT, print_metrics)

for line in sys.stdin:
    line = line.strip()
    ip_address, _, _, status_code, file_size = line.split(' ')
    total_size += int(file_size)
    status_codes[status_code] += 1
    line_count += 1
    if line_count == 10:
        print_metrics(None, None)
