#python code to check if a string has any repeating characters
def is_isogram(string):
  string = string.lower()
  for letter in string:
    if string.count(letter) > 1:
      return False
  return True
