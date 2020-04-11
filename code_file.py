#Implement the Booth's algorithm for multiplying binary numbers
print("IMPLEMENTING BOOTHS ALGORITHM")

#print(("{0:0%db}" % 10).format(m))
#int('[binary_value]',2)          ---converts binary to decimal

def twocom(s):                 #this function takes a binary value and returns the two's complement of it
    tw=""
    for i in s:              #in this loop we find the one's complement
        if(i=="1"):
            tw+="0"
        else:
            tw+="1"
    tw=badd(tw,"1")       #to the one's complement found we add 1
    return tw

def badd(a,b):                #this function takes two binary number and returns the sum in binary
    fans=""
    if(len(a)>len(b)):         #we make both the number in equal length by adding zero to the begining
        b="0"*(len(a)-len(b))+b
    else:
        a="0"*(len(b)-len(a))+a
    l=len(a)
    c=0                  #initialise carry bit with 0
    for i in range(l):
        d=int(a[l-i-1])+int(b[l-i-1])+c
        if(d==0):
            fans="0"+fans
            c=0
        elif(d==1):
            fans="1"+fans
            c=0
        elif (d == 2):
            fans = "0" + fans
            c=1
        elif (d == 3):
            fans = "1" + fans
            c=1
    return(fans)

def rshif(s):       #this function takes binary number and returns arithematic shift right value
    fc=s[0]
    fans=s[:-1]     #we first all digit of given number leaving the last digit to the final answer
    fans=fc+fans    #we add the first digit of given number to the final answer
    return(fans)

print("Enter the first variable  ",end="")
a=int(input())
print("Enter the second variable  ",end="")
b=int(input())
#create a copy of a and b
ca,cb=a,b
print("Enter bit length of first variable  ",end="")             #please enter an extra bit than required bits to store the value
alen=int(input())
if(a>=0):
    a = ("{0:0%db}" % alen).format(a)       #converts to binary value
else:
    a = twocom(("{0:0%db}" % alen).format(a))  #first converts to binary value then to its two's complement

print("Enter bit length of second variable  ",end="")         #please enter an extra bit than required bit
blen=int(input())
if(b>=0):
    b = ("{0:0%db}" % blen).format(b)
else:
    b = twocom(("{0:0%db}" % blen).format(b))

fp=alen*"0"+b+"0"      #final product adding q-1 initially as 0 only
m=a+((blen+1)*"0")
mm=twocom(a)+(blen+1)*"0"
for i in range(blen):
    c=fp[-2:]      #here c is Q0Q-1 value    thats the last two digit of fp variable
    print("Value of Q0Q-1=",c)
    if(c=='01'):
        fp=badd(fp,m)   #we add 1st variable to the accumulator
        #print("after adding m to fp we get",fp)
    elif(c=="10"):
        fp=badd(fp,mm)   #we subtract 1st variable from the accumulator or add two's complement of 1st variable to accumulator
        #print("after adding mm to fp we get", fp)
    fp=rshif(fp)       #we arithmetic shift right the value in accumulator register and q register
    print('Value of AC(accumulator)  Q and Q-1 after ',(i+1),'interation:')
    print("\t",fp[0:alen],"\t   ",fp[alen:-1],"  ",fp[-1])
    #print("after shifing(ars) fp by 1 value", fp)
fp=fp[:-1]  #removing the last bit(Q-1) which we added for implementation
print()
print("FINAL ANSWER IN BINARY EQUIVALENT=",fp)
if((ca<0 and cb>0)  or (ca>0 and cb<0)):
    fp=twocom(fp)
    print("FINAL ANSWER     :  ",-1*(int(fp,2)))
else:
    print("FINAL ANSWER     :  ",int(fp, 2))