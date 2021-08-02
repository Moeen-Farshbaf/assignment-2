Active = True
count = 0
while Active:
    user_no = int(input("Please Enter numbers that you want to sum up when you were done Enter 0!:\n"))
    will = input('Are you done?'+'\n'+'N for keep adding Y for having results')
    count = count + user_no
    if will == 'Y':
        print (count)
        Exit = input ('again? yes/no')
        if Exit =='no':
                break



