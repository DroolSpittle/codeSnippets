def duplicate_count(text):
    count = 0
    text = text.lower()
    for letter in text:
        if text.count(letter) > 1:
            count = count + 1
            text = text.replace(letter, "")
    return count
