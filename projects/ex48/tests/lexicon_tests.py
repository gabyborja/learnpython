from nose.tools import * 
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("NORTH south east")
    assert_equal(result, [('direction', 'NORTH'),
                         ('direction', 'south'),
                         ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill EAT")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'EAT')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the IN of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'IN'),
                          ('stop', 'of')])


def test_nouns():
    assert_equal(lexicon.scan('bear'), [('noun', 'bear')])
    result = lexicon.scan("bear PRINCESS")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'PRINCESS')])


def test_errors():
    assert_equal(lexicon.scan("ASDFASDFASADAFASF"), 
                            [('error', "ASDFASDFASADAFASF")])
    result = lexicon.scan("bear IAS princess 9")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess'),
                          ('number', 9)])
