from datetime import datetime
now = datetime.now()
current_time = now.strftime(" %H : %M : %S ")
while True:

    print ("It's"+' '+ current_time+ "\n" +"I can tell you how many seconds have past until this time of the day \nplease Enter The Current hour:")
    h = input()
    m = input("Now Enter the minute please\n")
    s = input ("Now enter the second\n")
    secondstot = (int(h)*3600) + (int(m)*60) +(int(s)) + 15
    #هر بار اجرای برنامه و کامل وارد کردن اعداد تقریبا 15 ثانیه طول می کشد س =))))
    will = input ("The total seconds which has passed until almost now is: "+str(secondstot)+' \ndo you want to continue?\nY to reset N to go back to wasting your seconds')
    
    if will == 'N':
        print ('Have fun, time flies')
        break