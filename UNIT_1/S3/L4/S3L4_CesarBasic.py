def main():
    usrInp = input("Enter a string to decypher: ")
    inpLower = usrInp.lower()

    alphabet = "abcdefghilmnopqrstuvz"

    alphabet_map = {letter: index+1 for index, letter in enumerate(alphabet)}
    reverse_map = {index+1: letter for index, letter in enumerate(alphabet)}

    for key in range(1, 22):
        deciphered = ""

        for char in inpLower:
            if char not in alphabet:
                deciphered += char  
                continue

            index = int(alphabet_map[char]) - key

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