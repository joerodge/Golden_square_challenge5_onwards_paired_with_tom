from lib.grammar import *

def test_check_returns_true_if_correct_grammar_full_stop():
    gram = GrammarStats()
    result = gram.check("Hello my name is Joe.")
    assert result == True

def test_check_returns_true_if_correct_grammar_bang():
    gram = GrammarStats()
    result = gram.check("Hello my name is Joe!")
    assert result == True

def test_check_returns_true_if_correct_question_mark():
    gram = GrammarStats()
    result = gram.check("Hello my name is Joe?")
    assert result == True

def test_check_returns_false_incorrect_end_punctuation():
    gram = GrammarStats()
    result = gram.check("Hello my name is Joe,")
    assert result == False

def test_check_returns_False_if_no_capital_or_punctuation():
    gram = GrammarStats()
    result = gram.check("hello my name is Joe")
    assert result == False

def test_check_returns_false_no_capital_but_has_punctuation():
    gram = GrammarStats()
    result = gram.check("hello my name is Joe.")
    assert result == False

def test_returns_false_if_zero_length_string():
    gram = GrammarStats()
    result = gram.check("")
    assert result == False

def test_check_when_input_isnt_string_should_not_be_error():
    gram = GrammarStats()
    result = gram.check(12453)
    assert result == False



# Percent_good() tests
def test_percent_good_all_good_returns_100():
    gram = GrammarStats()
    gram.check("Hello my name is Joe.")
    gram.check("Hello my name is Joe!")
    gram.check("Hello my name is Joe?")
    gram.check("Hi, how are you?")
    assert gram.percentage_good() == 100

def test_percent_good_all_bad_is_0():
    gram = GrammarStats()
    gram.check("hello my name is Joe.")
    gram.check("Hello my name is Joe")
    gram.check("hello my name is Joe")
    gram.check("hi, how are you")
    assert gram.percentage_good() == 0

"""test that percent of correct calls to .check() results in
correct percentage and that it is round to int"""
def test_percent_some_good_some_bad():
    gram = GrammarStats()
    gram.check("Hello my name is Joe.")
    gram.check("Hello my name is Joe")
    gram.check("hello my name is Joe")
    assert gram.percentage_good() == 33

"""No expection is thrown when .percentage_good() is called but
no checks have been done. It just returns 0. No divide by zero
error should be thrown"""
def test_percent_good_when_no_checks_have_been_done():
    gram = GrammarStats()
    assert gram.percentage_good() == 00