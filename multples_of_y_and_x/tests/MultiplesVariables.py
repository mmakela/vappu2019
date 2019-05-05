from textwrap import dedent


def _(text):
    return dedent(text).strip()


VALID_DATA = {
    'in': _("""
        2 7 26
        5 8 31
        """),
    'out': _("""
        31: 5 8 10 15 16 20 24 25 30
        26: 2 4 6 7 8 10 12 14 16 18 20 21 22 24
        """),
}

INVALID_DATA = {
    'in': _("""\
        2 7 26
        unexpected text
        """),
    'out': _("""
        Bad line in input file:
        unexpected text
        """),
}


# ${NEWLINE}    \n
# ${CONTENT_1}    2 7 26${NEWLINE}5 8 31
# ${OUTPUT_1}    31: 5 8 10 15 16 20 24 25 30${NEWLINE}26: 2 4 6 7 8 10 12 14 16 18 20 21 22 24
# ${CONTENT_2}    2 7 26${NEWLINE}unexpected text
# ${OUTPUT_2}    Bad line in input file:${NEWLINE}unexpected text

# &{VALID_DATA}    in=${CONTENT_1}    out=${OUTPUT_1}
# &{INVALID_DATA}    in=${CONTENT_2}    out=${OUTPUT_2}
