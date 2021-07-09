#I WAS DUMB REAL DUMB
a = open("Words.txt",'r')
b = 0
BAD = ["K","M","Q","T","V","W","X","Z"]
bad = ["k","m","q","t","v","w","x","z"]
word = a.read(0)

for NEWword in a:
    if len(NEWword) >= len(word):
        print(list(NEWword))
        for p in NEWword:
            if p in (bad or BAD):
                print("bad")
            elif p not in (bad or BAD):
                print ("good")
        print(p)
        print("done")
    b += 1
    if b == 20:
        break
print(word)
print("final")

