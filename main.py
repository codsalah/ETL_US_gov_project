import argparse
from data_transformer import transform_data

def main():
    parser = argparse.ArgumentParser(description='Transform JSON data to CSV.')
    parser.add_argument('-i', '--input', required=True, help='Input JSON file path.')
    parser.add_argument('-o', '--output', required=True, help='Output directory path.')
    parser.add_argument('-u', '--unix', action='store_true', help='Keep timestamps in UNIX format.')

    args = parser.parse_args()

    transform_data(args.input, args.output, keep_unix=args.unix)

if __name__ == '__main__':
    main()