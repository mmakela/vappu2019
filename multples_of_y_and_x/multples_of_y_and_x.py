import itertools
import sys


class Result(object):

    def __init__(self, x, y, goal_number):
        self._goal_number = goal_number
        self._store = set()
        self._add(x)
        self._add(y)

    def __str__(self):
        return '{}: {}'.format(
            self._goal_number,
            ' '.join(self)
        )

    def __len__(self):
        return len(self._store)

    def __iter__(self):
        ret = list([str(item) for item in self._store])
        ret.sort(key=int)
        return iter(ret)

    def _add(self, number):
        self._store.update(list(self._find_multiples(number)))

    def _find_multiples(self, number):
        for i in itertools.count(1):
            ret = i * number
            if ret < self._goal_number:
                yield ret
            else:
                raise StopIteration


def _read_lines(infile):
    with open(infile) as f:
        for line in f.read().splitlines():
            try:
                x, y, goal_number = [int(i) for i in line.split()]
            except ValueError:
                print 'Bad line in input file:\n{}'.format(line)
                sys.exit(1)
            yield x, y, goal_number


def _write_lines(outfile, output):
    with open(outfile, 'w') as f:
        f.write(output)


def main(infile, outfile):
    results = [Result(*args) for args in _read_lines(infile)]
    output = '\n'.join([str(result) for result in sorted(results, reverse=True)])
    print output
    _write_lines(outfile, output)


if __name__ == '__main__':
    try:
        infile, outfile = sys.argv[1:]
    except ValueError:
        print 'usage: {0[0]} INPUT OUTPUT'.format(sys.argv)
        sys.exit(1)
    main(infile, outfile)
