import datetime
import argparse

# initialize argparse
parser = argparse.ArgumentParser(
                    prog='datelistinator.py',
                    description='Creates a list of dates.',
                    epilog='Made by rohanhax')

# add arguments to get initial and last date to create a list. Also optional argument for output file name.
parser.add_argument('-i', metavar='initial_date',type=str,help='initial date (YYY-MM-DD)',required=True)
parser.add_argument('-l', metavar='last_date',type=str,help='last date (YYY-MM-DD)',required=True)
parser.add_argument('-o', metavar='output_file',type=str,help='filename to write output to (default: datelist.txt)',default='datelist.txt')
args = parser.parse_args()

# convert arguments to variables
iin = args.i
lin = args.l
ofile = args.o

# breakup full dates in day, month, year
iyear,imonth,iday=list(map(int, iin.split('-')))
lyear,lmonth,lday=list(map(int, lin.split('-')))

# put them in datetime object
ini = datetime.date(iyear,imonth,iday)
end = datetime.date(lyear,lmonth,lday)

# create a list with ini as starting date and keep adding the next date until last date occurs
with open(ofile,'w') as datelist:
    while ini<=end:
        datelist.write(ini.strftime('%d%m%y')+'\n')
        ini=ini+datetime.timedelta(days=1)
    datelist.close()