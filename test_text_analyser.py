import pytest
from text_analyser import count_words, count_characters, count_sentences, get_word_frequency

# --- Tests for count_words ---
def test_count_words_simple():
  assert count_words("Hello world") == 2

def test_count_words_empty_string():
  assert count_words("") == 0

def test_count_words_with_extra_spaces():
  assert count_words("  leading and trailing spaces  ") == 4

def test_count_words_with_punctuation():
  # split() handles punctuation attached to words correctly for word count
  assert count_words("Hello, world!") == 2

def test_count_words_non_string_input():
    with pytest.raises(TypeError):
        count_words(123)

# --- Tests for count_characters ---
def test_count_characters_with_spaces():
  assert count_characters("Hello world") == 11 # Default includes spaces

def test_count_characters_without_spaces():
  assert count_characters("Hello world", include_spaces=False) == 10

def test_count_characters_empty_string():
  assert count_characters("") == 0
  assert count_characters("", include_spaces=False) == 0

def test_count_characters_non_string_input():
    with pytest.raises(TypeError):
        count_characters(None)
    with pytest.raises(TypeError):
        count_characters(['list'], include_spaces=False)
# --- ADDED: Tests for count_sentences ---
def test_count_sentences_multiple():
    text = "First sentence. Second sentence! Third one? Yes."
    assert count_sentences(text) == 4

def test_count_sentences_empty():
    assert count_sentences("") == 0

def test_count_sentences_no_terminator():
    assert count_sentences("Just one phrase") == 1

def test_count_sentences_only_punctuation():
    assert count_sentences(".!?") == 0 # No actual content between terminators

def test_count_sentences_trailing_punctuation():
     assert count_sentences("Ends with dot.") == 1

def test_count_sentences_non_string_input():
    with pytest.raises(TypeError):
        count_sentences(42)

# --- ADDED: Tests for get_word_frequency ---
def test_get_word_frequency_simple():
    text = "test word test"
    expected = {"test": 2, "word": 1}
    assert get_word_frequency(text) == expected

def test_get_word_frequency_case_insensitive():
    text = "Test word test WORD"
    expected = {"test": 2, "word": 2}
    assert get_word_frequency(text) == expected

def test_get_word_frequency_with_punctuation():
    text = "Hello, world! Hello again."
    expected = {"hello": 2, "world": 1, "again": 1}
    assert get_word_frequency(text) == expected

def test_get_word_frequency_empty():
    assert get_word_frequency("") == {}

def test_get_word_frequency_non_string_input():
    with pytest.raises(TypeError):
        get_word_frequency(["list", "is", "not", "string"])