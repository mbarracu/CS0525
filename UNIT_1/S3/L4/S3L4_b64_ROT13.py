import base64

def main():
    usrInp = input("Enter a Base64 string to decode and decypher: ")

    try:
        decoded_bytes = base64.b64decode(usrInp)
        decoded_text = decoded_bytes.decode("utf-8")
    except Exception as e:
        print("Error: invalid Base64 input:", e)
        return

    print("\n[+] Base64 decoded text:")
    print(decoded_text)
    print("\n------------------------\n")

    inpLower = decoded_text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    alphabet_map = {letter: index+1 for index, letter in enumerate(alphabet)}
    reverse_map = {index+1: letter for index, letter in enumerate(alphabet)}

    for key in range(1, 27):
        deciphered = ""

        for char in inpLower:
            if char not in alphabet_map:
                deciphered += char  
                continue

            index = alphabet_map[char] - key

            if index < 1:
                index += 26  

            deciphered += reverse_map[index]

        print(f"\nCurrent key: {key}\n")
        print(deciphered)

        resInput = input("\nDoes this look correct? (y/n): ")
        if resInput.lower() == "y":
            print("\n[+] Final deciphered text:")
            print(deciphered)
            break

if __name__ == "__main__":
    main()
