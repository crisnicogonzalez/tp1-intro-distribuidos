import argparse


parser = argparse.ArgumentParser(description='TP1 - Introducción Distribuidos 75.43')

parser.allow_abbrev = False

parser.add_argument("-v", "--verbose", help="increase output verbosity", metavar='')
parser.add_argument("-q", "--quiet", help="decrease output verbosity", metavar='')
parser.add_argument("-s", "--server", help="server IP address", metavar='')
parser.add_argument("-c", "--count", help="stop after < count > replies", metavar='')
parser.add_argument("-p", "--ping", action="store_true", help="direct ping")
parser.add_argument("-r", "--reverse", help="reverse ping", metavar='')
parser.add_argument("-d", "--dest", help="destination IP address", metavar='')

args = parser.parse_args()
print(args.count)
print(args.server)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
