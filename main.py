
def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  word_count = count_words(book_text)
  letter_count = count_letters(book_text)
  print(f"{word_count} words found in document")
  for letter in letter_count:
    print(f"The character {letter} was found {letter_count[letter]} times")

def get_book_text(book_path):
  with open(book_path) as f:
    return f.read()

def count_words(text):
  words = text.split()
  return len(words)

def count_letters(text):
  letter_count = {}
  for letter in text:
    letter = letter.lower()
    if letter in letter_count:
      letter_count[letter] += 1
    else:
      letter_count[letter] = 1
  return letter_count

main()