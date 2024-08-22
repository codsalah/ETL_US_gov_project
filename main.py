import argparse
from data_transformer import transform_data

def main():
    parser = argparse.ArgumentParser(description='Transform JSON to CSV')
    parser.add_argument('-i', '--input', required=True, help='Input JSON file path')
    parser.add_argument('-o', '--output', required=True, help='Output directory path')
    parser.add_argument('-f', '--filename', required=True, help='Output file name')
    parser.add_argument('-u', '--keep_unix', action='store_true', help='Keep Unix timestamp format')
    args = parser.parse_args()

    # Transform data
    transform_data(args.input, args.output, args.filename, args.keep_unix)

if __name__ == '__main__':
    main()