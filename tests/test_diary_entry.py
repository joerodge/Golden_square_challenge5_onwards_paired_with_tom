from lib.diary_entry import *
import pytest

"""
Test that 2 arguments are passed into __init__()
"""
def test_init_receives_2_args():
    #check type error is thrown
    pass


"""
Test with correct inputs, returns correctly formatted diary entry
"""
def test_format_with_correct_args():
    #check output is formatted correctly
    diary = DiaryEntry("Day 1", "Today I went to the park")
    result = diary.format()
    assert result == "Day 1: Today I went to the park"


"""
Check that the correct word count is returned
"""
def test_correct_word_count_is_returned():
    diary = DiaryEntry("Day 1", "Today I went to the park")
    assert diary.count_words() == 8


"""
Check that no error is thrown when inputs are empty for count_words()
"""
def test_no_error_when_inputs_are_empty_in_count_words():
    diary = DiaryEntry("", "")
    assert diary.count_words() == 0


"""
Check that the output is an int
"""
def test_output_is_int():
    diary = DiaryEntry("Day 1", "Today I went to the park")
    assert type(diary.count_words()) == int


"""
Check that correct time estimate is returned for reading_time()
for word counts which are evenly divisible by wpm. 
e.g. 100 words and 100 wpm should be 1
"""
def test_check_correct_time_est_for_evenly_divisible_wpm_and_words():
    diary = DiaryEntry('hello', 'hello '*99)
    result = diary.reading_time(100)
    assert result == 1


"""
Check that estimated time is rounded correctly in reading_time(). It 
should always be rounded up to the nearest minute and return an int
"""
def test_reading_time_rounded_up_correctly():
    # 150 words at 100 wpm should be 1.5 minutes so output should be 2
    diary = DiaryEntry('Title', 'Body ' * 149)
    result = diary.reading_time(100)
    assert result == 2


"""Same as above test rounding, but this time a reading time that
would normally be rounded down using traditional rounding method
"""
def test_reading_time_rounded_up_correctly2():
    # 450 words at 200 wpm should be 2.25 minutes so output should be 3
    diary = DiaryEntry('Title', 'Body ' * 449)
    result = diary.reading_time(200)
    assert result == 3


"""
check that the output of reading_time is an int
"""
def test_reading_time_output_is_an_int():
    body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    diary = DiaryEntry('Lorem ipsum', body * 1000)
    result = diary.reading_time(150)
    assert type(result) == int


"""
Check that error is thrown for reading_time() when WPM is <= 0
"""
def test_error_for_reading_time_if_wpm_is_0():
    diary = DiaryEntry('Hello', 'hello ' * 1000)
    with pytest.raises(Exception) as e:
        result = diary.reading_time(0)
    assert str(e.value) == "wpm must be greater than zero"

def test_error_for_reading_time_if_wpm_is_less_than_0():
    diary = DiaryEntry('Hello', 'hello ' * 1000)
    with pytest.raises(Exception) as e:
        result = diary.reading_time(-100)
    assert str(e.value) == "wpm must be greater than zero"


"""
Check all contents is read in the time given. So if there are only
100 words then output should be all the text if wpm is 100 and time 1 min
"""
def test_reading_chunk_all_words_read():
    diary = DiaryEntry('Title', 'hello ' * 99 + 'goodbye')
    result = diary.reading_chunk(100, 1)
    assert result.startswith('hello') and result.endswith('goodbye')

def test_reading_chunk_less_than_all_text_returns_correct_text():
    diary = DiaryEntry('Title', ('hello ' * 99) + 'middle ' + ('goodbye ' * 100))
    result = diary.reading_chunk(100, 1)
    assert result.startswith('hello') and result.endswith('middle')

"""
Check that calling function for a second time does not return you to the start of the contents,
but where you left off
"""
def test_reading_chunk_second_time_returns_text_from_where_you_left_off():
    diary = DiaryEntry('Title', ('hello ' * 99) + 'middle ' + ('goodbye ' * 100))
    result = diary.reading_chunk(100, 1)
    result2 = diary.reading_chunk(100, 1)
    assert result2.startswith('goodbye')


"""
Check that no error is returned when not enough words are present in the contents
"""
def test_reading_chunk_where_less_text_than_what_can_be_read():
    diary = DiaryEntry('Title', ('hello ' * 4))
    result = diary.reading_chunk(5, 1)
    assert result == 'hello hello hello hello'


"""
Check that once all text is read, once called again, the user starts from the beginning.
"""
def test_reading_chunk_where_all_text_prev_read_returns_to_start():
    diary = DiaryEntry('Title', ('hello ' * 99) + 'middle ' + ('goodbye ' * 100))
    diary.reading_chunk(100, 1)
    diary.reading_chunk(100, 1)
    result = diary.reading_chunk(100, 1)
    # assert back at start
    assert result.startswith('hello')

"""
Check that error is thrown when WPM is <= 0
"""
def test_reading_chunk_error_thrown_for_wpm_0():
    diary = DiaryEntry('Title', 'Body '* 500)
    with pytest.raises(Exception) as e:
        diary.reading_chunk(0, 2)
    assert str(e.value) == "WPM must be greater than 0"

"""
Check that no error is thrown when minutes <= 0 just empty
string is returned as that's how much would be read in 0 mins
"""
def test_reading_chunk_error_thrown_for_minutes_0():
    diary = DiaryEntry('Title', 'Body '* 500)
    result = diary.reading_chunk(100, 0)
    assert result == ''