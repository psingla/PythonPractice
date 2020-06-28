from string import ascii_lowercase
str1 = input("input first string")
str2 = input("input second string")

dict1 = dict()
dict2 = dict()

if len(str1) != len(str2):
    print("String not anagram.Exiting...")
    exit(1)
for c in ascii_lowercase:
    dict1[c] = 0
    dict2[c] = 0

for cntr in range(0, len(str1)):
    dict1[str1[cntr].lower()] += 1
    dict2[str2[cntr].lower()] += 1

for c in ascii_lowercase:
    if dict1[c] != dict2[c]:
        print("Not a anagram.Exiting")
        exit()

print("Anagram.Exiting")