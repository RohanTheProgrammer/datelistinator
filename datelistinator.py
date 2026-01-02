import datetime
import argparse
import sys

# initialize argparse
parser = argparse.ArgumentParser(
                    prog='datelistinator.py',
                    description='Creates a list of dates.',
                    epilog='Made by rohanhax')

# add arguments to get initial and last date to create a list. Also optional argument for output file name.
parser.add_argument('-i', metavar='INITIAL_DATE', type=str, help='initial date (DD-MM-YYYY), ex- 01-01-2001', required=True)
parser.add_argument('-l', metavar='LAST_DATE', type=str, help='last date (DD-MM-YYYY), ex- 01-01-2001', required=True)
parser.add_argument('-f', metavar='OUTPUT_FORMAT', help='output date format (default: %%d%%m%%y)', default='%d%m%y')
parser.add_argument('-o', metavar='OUTPUT_FILE', type=str, help='filename to write output to (default: datelist.txt)', default='datelist.txt')
args = parser.parse_args()

# Check date format (DD-MM-YYYY)
try:
    ini = datetime.datetime.strptime(args.i, '%d-%m-%Y').date()
    end = datetime.datetime.strptime(args.l, '%d-%m-%Y').date()
except ValueError:
    print('[!] Invalid date format. Use DD-MM-YYYY.')
    sys.exit(1)

# Check output format
try:
    ini.strftime(args.f)
except Exception:
    print('[!] Invalid strftime format supplied.')
    sys.exit(1)

# Logical validation
if ini > end:
    print('[!] Initial date cannot be after last date.')
    sys.exit(1)

# create a list with ini as starting date and keep adding the next date until last date occurs
with open(args.o, 'w') as datelist:
    while ini <= end:
        datelist.write(ini.strftime(args.f) + '\n')
        ini += datetime.timedelta(days=1)

print(f'[+] Date list written to {args.o}')