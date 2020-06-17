from text2digits.t2d import Text2Digits
from text2digits.rules import CombinationRule, ConcatenationRule


def test_parer_combination_rule():
    cases = [('twenty one thousand three hundred', 5), ('twenty one', 2), ('hundred twenty one', 3)]
    rule = CombinationRule()
    t2d = Text2Digits()

    for example, number in cases:
        assert rule.match(t2d._lex(example)) == number


def test_parer_concatenation_rule():
    cases = [('one ten', 2), ('three', 1), ('nineteen', 1)]
    rule = ConcatenationRule()
    t2d = Text2Digits()

    for example, number in cases:
        assert rule.match(t2d._lex(example)) == number
