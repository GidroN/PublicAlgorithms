def cesar(word, enc=True, step=4):

    def encrypt():
        output_mass = []

        input_mass = list(word)
        for n in input_mass:
            m = n
            n = ord(n)
            n += step
            if n > 122 and m.islower() is True:
                n -= 123
                n += 97

            elif n > 90 and m.isupper() is True:
                n -= 91
                n += 65

            if 65 <= n <= 90 or 97 <= n <= 122:
                n = chr(n)
                output_mass.append(n)
            else:
                n -= step
                n = chr(n)
                output_mass.append(n)

        str1 = "".join([str(i) for i in output_mass])
        return (f"Encrypted word: {str1}")

    def decrypt():
        output_mass = []

        input_mass = list(word)
        for n in input_mass:
            m = n
            n = ord(n)
            n -= step

            if n < 97 and m.islower() is True:
                n = 96 - n
                n = 122 - n

            elif n < 65 and m.isupper() is True:
                n = 64 - n
                n = 90 - n

            if 65 <= n <= 90 or 97 <= n <= 122:
                n = chr(n)
                output_mass.append(n)
            else:
                n += step
                n = chr(n)
                output_mass.append(n)

        str1 = "".join([str(i) for i in output_mass])
        return (f"Decrypted word: {str1}")

    try:
        if enc is True:
            return encrypt()
        else:
            return decrypt()

    except ValueError:
        return ("Incorrect input!")


while True:
    cipher = input("Encrypt / Decrypt? (1 / 2): ")
    word = input("Enter the word: ")
    step = input("Enter the step (Default - 4): ")
    if not step:
        step = 4
    if cipher == 1:
        print(cesar(word, enc=True, step=step))
        print()
    else:
        print(cesar(word, enc=False, step=step))
        print()