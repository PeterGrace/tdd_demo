"""The primary module for this skeleton application."""
import argparse
from .functions import multiply


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("first")
    parser.add_argument("second")
    args = parser.parse_args()
    print(multiply(int(args.first), int(args.second)))

if __name__ == '__main__':
    main()
