import time
mytime=int(input("enter the time un second:"))
for x in range(mytime,0,-1):
    second=x%60
    minutes=int(x/60)%60
    print(f"00:{minutes:02}:{second:02}")
    time.sleep(1)

print("time is up")