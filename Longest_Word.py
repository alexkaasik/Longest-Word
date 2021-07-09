a = open("Words.txt",'r')
b = ("k","m","q","v","w","x","z")
c = 0

word = a.read(0)
 
for NEWword in a:
    if len(NEWword) >> len(word):
        for p in NEWword:
            if p in b:
                c+=1
        if c == 0:
            word = NEWword
print("done")
print(word)
