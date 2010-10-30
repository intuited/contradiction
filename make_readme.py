#!/usr/bin/env python
"""Simple makefile to build ``README.txt``."""

import sys, string, StringIO, contextlib

import contradiction

@contextlib.contextmanager
def borrow_stdout(new_out):
    orig = sys.stdout
    sys.stdout = new_out
    yield new_out
    sys.stdout = orig

with borrow_stdout(StringIO.StringIO()) as docs:
    help(contradiction.contradiction)

with open('README.template', 'r') as template_file:
    with open('README.txt', 'w') as output_file:
        template = string.Template(template_file.read())
        output_file.write(template.substitute({'docs': docs.getvalue()}))
