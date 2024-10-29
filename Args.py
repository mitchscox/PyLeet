"""
To run this script, you would use the following command:

```
python script_name.py 1 2 3 4
```

In this case, `1` would be parsed as an integer and `2`, `3`, and `4` would be parsed as a list of integers.

Here's how it works:

- The `argparse.ArgumentParser(description='Example script')` line creates an argument parser.
- The `parser.add_argument('integer', type=int, help='An integer argument')` line adds an argument named 'integer' that is expected to be an integer.
- The `parser.add_argument('integers', nargs='+', type=int, help='One or more integer arguments')` line adds an argument named 'integers' that can be one or more integers. The `nargs='+'` means that this
argument will take one or more values.
- The `args = parser.parse_args()` line parses the command-line arguments and returns them as a namespace object.
- The `print(f"Integer: {args.integer}")` and `print("Integers:", args.integers)` lines print out the parsed arguments.

"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='Argument script for a single integer then a list of integers')
    parser.add_argument('integer', type=int, help='An integer argument')
    parser.add_argument('integers', nargs='+', type=tuple,help='One or more integer arguments')

    args = parser.parse_args()

    print(f"Integer: {args.integer}")
    print(f"Integers:", args.integers)

if __name__ == "__main__":
    main()

