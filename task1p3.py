a = input('vedite tekst: ')
bolshoy = 0
menshiy = 0
for i in a:
    if ord(i) > 64 and ord(i) < 91:
        bolshoy += 1
    elif ord(i) > 96 and ord(i) < 123:
        menshiy += 1
print('kolichestvo bolshih bukv= ',bolshoy)
print('kplichestvo menshih bukv= ',menshiy)
procent_bol = (bolshoy / (bolshoy + menshiy)) * 100
procent_men = (menshiy / (bolshoy + menshiy)) * 100
print("Procent bolshih bukv= ", procent_bol)
print('Procent meshih bukv= ', procent_men)