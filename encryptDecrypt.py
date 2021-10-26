#Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.




def encrypt(text, n):
    if text == "":
        return text
    if n <= 0:
        return text
    oddString = ''
    evenString = ''
    i = 0
    while n > 0:
        while i < len(text):
            if i % 2 == 0:
                evenString = evenString + text[i]
            else:
                oddString = oddString + text[i]
            i = i + 1
        text = oddString + evenString
        evenString = ''
        oddString = ''
        i = 0
        n = n - 1
    return text

def decrypt(encrypted_text, n):
    if encrypted_text == '':
        return encrypted_text
    if n <= 0:
        return encrypted_text
    half = int(len(encrypted_text)/2)
    firstHalf =  encrypted_text[:half]
    secondHalf = encrypted_text[half:]
    i = 0
    while n > 0:
        text = ''
        while i < half:
            text = text + secondHalf[i] + firstHalf[i]
            i = i + 1
        if len(encrypted_text) % 2 != 0:
            text = text + secondHalf[i]
        firstHalf = text[:half]
        secondHalf = text[half:]
        i = 0
        n = n - 1
    return text
    
    
##############
##Better Way##
##############


def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
