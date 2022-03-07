def gcd(a,b):
   if a==0:
      return b 
   elif b==0:
      return a 
   elif b>a:
      return gcd(b,a)
   else:
      return gcd(b,a%b)

for i in range(int(input())):
   n = int(input())
   a = list(map(int,input().split()))
   if len(a)==1:
      print(1)
   else:
      leftgcd = [0]*n
      rightgcd = [0]*n
      midgcd = [0]*n
      
      temp = 0
      for key,val in enumerate(a):
         leftgcd[key] = temp
         if temp==0:
            temp = val 
         else:
            temp = gcd(temp,val) 
      temp = 0
      for i in range(n-1,-1,-1):
         key = i 
         val = a[key] 
         rightgcd[key] = temp 
         if temp==0:
            temp = val 
         else:
            temp = gcd(temp,val)

            
      for i in range(n):
         if leftgcd[i]==0:
            midgcd[i] = rightgcd[i]
         elif rightgcd[i]==0:
            midgcd[i] = leftgcd[i]
         else:
            midgcd[i] = gcd(leftgcd[i],rightgcd[i])
      mx = [0,0]
      for key,val in enumerate(midgcd):
         mx = max(mx,[val,a[key]])
      for key,val in enumerate(midgcd):
         if val==mx[0] and a[key]==mx[1]:
            temp = key
            tempval = val 
      a[temp] = tempval
      sum = 0
      for item in a:
         sum+=item//tempval
      print(sum)