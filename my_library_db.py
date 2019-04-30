import argparse
import operator
import os
import re
import sys
import textwrap


def _add_new_book(db):
    db.add()

def _print_database(db):
    db.list()


class TextDB(object):

    def __init__(self, path):
        self._path = self._assert_textfile_exist(path)
        self._content = list(self._parse_textfile(path))

    def _assert_textfile_exist(self, path):
        if not os.path.isfile(path):
            open(path, 'w').close()
        return path

    def _parse_textfile(self, path):
        with open(path) as f:
            text = f.read()
            for line in text.splitlines():
                items = [item.strip() for item in line.split('  ', 2)]
                yield {
                    'bookname': items[0],
                    'writer': items[1],
                    'ISBN': items[2],
                }

    def list(self):
        for item in sorted(self._content, key=operator.itemgetter('writer'), reverse=False):
            print textwrap.dedent("""\
                Writer: {0[writer]}
                Book:   {0[bookname]}
                ISBN:   {0[ISBN]}
                """.format(item))

    def _read_input(self, prompt):
        res = raw_input(prompt)
        return re.sub(' +', ' ', res)

    def add(self):
        book = self._read_input('Name of the book: ')
        writer = self._read_input('Writer of the book: ')
        isbn = self._read_input('ISBN of the book: ')
        print 'Do you want to update database with "{}/{}/{}"?'.format(book, writer, isbn)
        result = raw_input('Agree (y/N):')
        if result.lower() == 'y':
            self._add(book, writer, isbn)
            self._save()

    def _add(self, book, writer, isbn):
        self._content.append(
            {
                'bookname': book,
                'writer': writer,
                'ISBN': isbn,
            }
        )

    def _save(self):
        with open(self._path, 'w') as f:
            for item in sorted(self._content, key=operator.itemgetter('writer')):
                f.write('{0[bookname]}  {0[writer]}  {0[ISBN]}\n'.format(item))


def menu(path):
    print(
        """Select option:
        1) Add new book
        2) Print database
        q) Quit
        """
    )
    db = TextDB(path)
    while True:
        result = raw_input('> ')
        if result.lower() == 'q':
            sys.exit()
        actions = {
            '1': _add_new_book,
            '2': _print_database,
        }.get(result)
        if actions:
            actions(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('database_textfile')
    args = parser.parse_args()
    menu(args.database_textfile)
