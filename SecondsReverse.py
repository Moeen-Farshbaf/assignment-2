
prompt = 'Give me a total amount of seconds and I will give t back in HH:MM:SS format'

prompt += '\nEnter the number here:'

totsec = int(input(prompt))

HH = int (totsec / 3600)
MM = int((totsec%3600) / 60)
SS = int((totsec%3600)%60)


print (str(HH)+':'+str(MM)+':'+str(SS))


















