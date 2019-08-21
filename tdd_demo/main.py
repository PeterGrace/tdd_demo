"""The primary module for this skeleton application."""
import argparse
from .functions import multiply
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("first")
    parser.add_argument("second")
    args = parser.parse_args()
    try:
        print(multiply(int(args.first), int(args.second)))
    except Exception:
        log.error("You specified invalid values for either first or second argument.")

if __name__ == '__main__':
    main()
