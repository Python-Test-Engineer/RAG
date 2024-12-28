# imports the pymupdf library
import re

# match left and right single quotes
single_quote_expr = re.compile(r"[\u2018\u2019]", re.U)
# match all non-basic latin unicode
unicode_chars_expr = re.compile(r"[\u0080-\uffff]", re.U)


def cleanse_unicode(s):
    if not s:
        return ""

    temp = single_quote_expr.sub("'", s, re.U)
    temp = unicode_chars_expr.sub("", temp, re.U)
    return temp
