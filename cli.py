import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    'domain',
    help = 'The domain to scan'
)

parser.add_argument(
    '-o', '--output',
    help = 'A file to output likely origin servers to',
    dest = 'output_file'
)
