import  sys
import time
print"numero:"
d = input()
i = 0
while(True):
    i =i+1
    if((i % d) ==0):
        sys.stdout.write("El %d  es multiplo de %d \n " %(i,d))
    else:
        sys.stderr.write("NO!!! ALARMA: el %d No es multiplo de %d!!!\n" %(i,d))
    time.sleep(1)
