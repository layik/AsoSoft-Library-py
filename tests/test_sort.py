from asosoft import kurdish_sort


def test_kurdish_sort_correctness():
    inputList = ['ب', 'پ', 'ئ', 'ت']
    expected = ['ئ', 'ب', 'پ', 'ت']
    assert kurdish_sort(inputList) == expected, f"Expected {expected}, got {kurdish_sort(inputList)}"


def test_kurdish_sort_non_kurdish_characters():
    # Assuming non-Kurdish chars are sorted as usual or placed at the end
    inputList = ['x', 'b', 'a']
    expected = ['a', 'b', 'x']
    assert kurdish_sort(inputList) == expected, f"Expected {expected}, got {kurdish_sort(inputList)}"


def test_kurdish_sort_case_sensitivity():
    inputList = ['ب', 'پ', 'ئ', 'ت', 'ئ']
    expected = ['ئ', 'ئ', 'ب', 'پ', 'ت']
    assert kurdish_sort(inputList) == expected, f"Expected {expected}, got {kurdish_sort(inputList)}"


def test_kurdish_sort_empty_list():
    inputList = []
    expected = []
    assert kurdish_sort(inputList) == expected, f"Expected {expected}, got {kurdish_sort(inputList)}"


def test_kurdish_sort_single_element_list():
    inputList = ['ت']
    expected = ['ت']
    assert kurdish_sort(inputList) == expected, f"Expected {expected}, got {kurdish_sort(inputList)}"


def test_kurdish_sort_duplicates():
    inputList = ['ت', 'ت', 'ب', 'ب']
    expected = ['ب', 'ب', 'ت', 'ت']
    assert kurdish_sort(inputList) == expected, f"Expected {expected}, got {kurdish_sort(inputList)}"
