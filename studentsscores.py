studscount = int(input("How many students you got?"))
studsgrads = []
for i in range(studscount):
    grade = float(input("Enter their grades when you were done enter done:"))
    studsgrads.append(grade)
    studsgrads.sort()
if len(studsgrads) == studscount:
    score_average = sum(studsgrads)/studscount
    print ("Average score is: "+str(score_average))
    print ("Highest score was:"+str(studsgrads[studscount-1]))
    print ("Lowest score was:"+str(studsgrads[0]))
    print (studsgrads)
    print ('Here is a list of grades:')
    for grade in studsgrads:
        print(str(grade) + '\n')
