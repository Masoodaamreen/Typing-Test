import time

text ="The quick brown fox jumps over the lazy dog"
print("Type this:")
print(text)

start = time.time()
typed = input("Start typing: ")
end = time.time()

if typed == text:
    print(f"Great! You took {round(end - start, 2)} seconds.")
else:
    print("Oops! You typed it wrong.")