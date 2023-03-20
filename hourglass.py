import time
  
def hourglass(heure):
    
    time.sleep(1)
    heure_copie=list(heure)
    heure_copie[2] = heure_copie[2]+1
    if heure_copie[2] > 59:
        heure_copie[2] = 0 
        heure_copie[1] = heure_copie[1] + 1
        if heure_copie[1] > 59:
            heure_copie[1] = 0 
            heure_copie[0] = heure_copie[0] + 1
            if heure_copie[0] > 23:
                heure_copie[0] = 0
    print(heure_copie[0],"h","",heure_copie[1],"m","",heure_copie[2],"s")
    alarm(tuple(heure_copie))
    hourglass(heure_copie)


def alarm(heure_actuel):
    global alarm_user
    alarm_set=tuple(map(int,alarm_user.split(',')))
    if alarm_set == heure_actuel:
        print("DRING ! DRING ! DRING !")
    else:
        
        return 0


global alarm_user
print("Choose when your alarm will work, ex: 8, 7, 6 = 8h 7m 6s")
alarm_user = input()
hourglass((0,0,0))
