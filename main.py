"""
This function sums the line per line if it's a is_number
otherwise it will call recursivley the sum function

@argument --file -f: the first file to start summing
@return: the sum
"""


def sum_per_line(override_file=False):
    from argparse import ArgumentParser

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def sum_per_line_recursive(file, acc):
        for line in open(file, 'r'):
            if is_number(line):
                acc += float(line)
            else:
                acc = sum_per_line_recursive(line.strip(), acc)
        return acc

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", help="the FILE", metavar="FILE")
    args = parser.parse_args()

    file_path = override_file if override_file else args.filename

    result = sum_per_line_recursive(file_path, 0)
    print(file_path, result)
    return result


# Starts the process
sum_per_line()

# sum_per_line('A.txt')
# sum_per_line('B.txt')
# sum_per_line('C.txt')
