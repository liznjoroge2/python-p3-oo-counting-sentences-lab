import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        """Returns True if the value ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the value ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Returns the number of sentences in the value."""
        # Replace multiple sentence-ending punctuations with a single period
        text = re.sub(r'[.!?]+', '.', self.value)
        # Split the text by periods
        sentences = text.split('.')
        # Remove any empty strings from the list
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
