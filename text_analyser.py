
import re

def count_words(text):
  """Counts the number of words in a given text string."""
  if not isinstance(text, str):
    raise TypeError("Input must be a string.")
  if not text:
    return 0
  words = text.split()
  return len(words)

def count_characters(text, include_spaces=True):
  """Counts the number of characters in a given text string."""
  if not isinstance(text, str):
      raise TypeError("Input must be a string.")
  if include_spaces:
    return len(text)
  else:
    # Remove spaces and then count
    return len(text.replace(" ", ""))

def count_sentences(text):
  """Counts the number of sentences based on common punctuation."""
  if not isinstance(text, str):
      raise TypeError("Input must be a string.")
  if not text:
      return 0
  # Simple sentence detection based on ., !, ?
  # This is a naive implementation and might not cover all edge cases.
  sentences = re.split(r'[.!?]+', text)
  # Filter out empty strings that result from splitting (e.g., ending punctuation)
  actual_sentences = [s for s in sentences if s.strip()]
  # Handle cases where there's text but no terminating punctuation
  if not actual_sentences and text.strip():
      return 1
  return len(actual_sentences)

def get_word_frequency(text):
    """Calculates the frequency of each word in the text (case-insensitive)."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    if not text:
        return {}
    # Simple cleaning: lowercase and remove punctuation for basic frequency
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    words = cleaned_text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency