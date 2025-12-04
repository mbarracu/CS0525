import re

def analyze_text(text: str): 
    # Count word frequencies in the given text.
    lcText = text.lower()
    cleanedTxt = re.sub('[^a-z0-9]', ' ', lcText)
    splitTxt = cleanedTxt.split()

    counts = {}

    for word in splitTxt:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1


    return counts

def main ():
    userText = input("Enter a block of text:\n")

    while userText.strip() == "":
        userText = input("Text cannot be empty. Please enter a block of text:\n")
        
    wordCounts = analyze_text(userText)

    print("Word Frequencies:")

    for word, count in wordCounts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()