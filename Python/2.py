import sys
import crypt

passfile = open('2_dict.txt', 'r')
for word in passfile.readlines():
    if crypt.crypt(word.strip(), "MS") == sys.argv[1]:
        print(f"Password found: {word.strip()}")
        break
else:
    print("Password not found")
