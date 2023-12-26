import argparse
import logging

parser = argparse.ArgumentParser()

parser.add_argument("num1", help="the first number", type=int)
parser.add_argument("num2", help="the second number", type=int)

parser.add_argument("op", help="the desired arithmetic operation", choices=['add', 'sub'])

parser.add_argument("-v", "--verbose", help="tuen on verbose output", action="store_true")

opts = parser.parse_args()

if opts.verbose:
    logging.basicConfig(level=logging.DEBUG)

logging.debug(f"First number: {opts.num1}")
logging.debug(f"Second number: {opts.num2}")
logging.debug(f"Operation: {opts.op}")

if opts.op == "add":
    result = opts.num1 + opts.num2

else:
    result = opts.num1 - opts.num2

print(result)