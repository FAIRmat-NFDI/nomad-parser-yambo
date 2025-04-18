import logging

from nomad.datamodel import EntryArchive
from nomad_nomad_parser_yambo.parsers.myparser import MyParser


def test_parse_file():
    parser = MyParser()
    archive = EntryArchive()
    parser.parse('tests/data/example.out', archive, logging.getLogger())

    assert archive.results.material.elements == ['H', 'O']
