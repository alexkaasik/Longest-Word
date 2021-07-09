a = open("Words.txt",'r')
b = 0
BAD = ["K","M","Q","T","V","W","X","Z"]
bad = ["k","m","q","t","v","w","x","z"]
word = a.read(0)

for NEWword in a:
    if len(NEWword) >= len(word):
        print(list(NEWword))
        for p in NEWword:
            if p not in (bad or BAD):
                print(f"{p}-good") 
            else:
                print (f"{p}-bad")
            print("done")
    b += 1
    if b == 10:
        break

print(word)
print("final")
