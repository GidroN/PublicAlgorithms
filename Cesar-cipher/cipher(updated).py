def rot13(message: str, step = 13):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    lst = list(message)
    result = []
    for index, element in enumerate(lst):
        if element.lower() not in alphabet:
            result.append(element)
        else:
            element = element.lower()
            letter = alphabet[alphabet.find(element) +step] if alphabet.find(element) + step < len(alphabet) else alphabet[alphabet.find(element) + step - len(alphabet)]
            result.append(letter)
    
    for i in range(len(lst)):
        if lst[i].isupper():
            result[i] = result[i].upper()
            
    return "".join(result)