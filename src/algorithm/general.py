# use this to remove duplicate character from text preserving the order.
# Example: remove_duplicate_char('testacoba') -> tesacob 
def remove_duplicate_char(text):
    return "".join(dict.fromkeys(text))

# use this to remove character from text.
# Example: remove_char('test', 't') -> es 
def remove_char(text, char):
    return text.replace(char, '')

# sanitize will remove space, number, and puctuation from given text
def sanitize(text):
    # TODO: lukas implement Fungsi buang = Angka, spasi, dan tanda baca
    return text

# use this to replace a character with another character.
# Example: replace_char('test', 't', 'b') -> besb 
def replace_char(text, old_char, new_char):
    return text.replace(old_char, new_char)