#!/usr/bin/env python3

from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from os.path import expanduser, isfile

from sak import subnet, ioc, hash, checkip

# command-line arguments and commands
parser = ArgumentParser(description='SOC Army Knife')
subparser = parser.add_subparsers(title='Commands', dest='command')
subparser.required = True

parser_subnet = subparser.add_parser('subnet', help='IP subnet calculator')
parser_subnet.add_argument('cidr', help='IP in CIDR format')

parser_ioc = subparser.add_parser('ioc', help='Extracts IoCs from files')
parser_ioc.add_argument('-i', '--input', 
    nargs=1, 
    type=FileType('r'), 
    required=True, 
    help='Input file')

parser_hash = subparser.add_parser('hash', help='Calculates the hash of a file')
parser_hash.add_argument('-a', '--algo',
    nargs=1,
    choices=['sha256', 'sha1', 'md5'], 
    default=['sha256'],
    help='The hash algorithm to be used')
parser_hash.add_argument('-i', '--input', 
    nargs=1, 
    type=FileType('rb'), 
    required=True, 
    help='Input file')

parser_checkip = subparser.add_parser('checkip', help='Get more information about an IP')
parser_checkip.add_argument('addr', help='IP address')
parser_checkip.add_argument('-e', '--engine',
    nargs=1,
    choices=['abuseipdb'],
    default=['abuseipdb'],
    help='The data source to be used')

args = parser.parse_args()


# configuration file
config = ConfigParser()
config_file = expanduser('~/.sak.conf')
if isfile(config_file):
    config.read(config_file)


def run():
    if args.command == 'subnet':
        subnet.ip_info(args.cidr)
    elif args.command == 'ioc':
        ioc.extract(args.input[0])
    elif args.command == 'hash':
        hash.calculate(args.input[0], args.algo[0])
    elif args.command == 'checkip':
        checkip.lookup(args.addr, args.engine[0], config['KEYCHAIN'][args.engine[0]])
