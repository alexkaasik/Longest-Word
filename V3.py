a = open("Words.txt",'r')
b = 0
BAD = ["K","M","Q","T","V","W","X","Z"]
bad = ["k","m","q","t","v","w","x","z"]
word = a.read(0)

for NEWword in a:
    if len(NEWword) >= len(word):
        word = NEWword




print (list(word))
for word2 in word:
    if word2 not in (bad or BAD):
        print(f"{word2}-good") 
    else:
        print (f"{word2}-bad")
print("final")

