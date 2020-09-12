#!/usr/bin/env python
# coding: utf-8

# In[3]:


def split(word):
    return [char for char in word]

def ByteStuffing():
    x = input("Enter data to be sent :")
    flag = '@'
    esc = '$'
    list = split(x)
    #print(list)
    i=0
    while(i<len(list)):
        if list[i]==flag or list[i]==esc:
            list.insert(i,esc)
            i+=1
        i+=1

    #print(list)
    list.insert(0,flag)
    list.append(flag)
    print( "AT SENDER SIDE",list)

    #Receiver Side
    del list[0]
    del list[len(list)-1]

    i=0
    while(i<len(list)):
        if list[i]==esc:
            del list[i]
            i+=1
        i+=1
    i=0
    print("AT RECEIVER SIDE",list)

def BitStuffing():
    #sender
    y = input("Enter binary data to be sent :")
    #list2 = []
    list1 = split(y)
    for i in list1:
        if i.isalpha():
            list1.insert(i,ord(i))
    print(list1)
            
    count = 0
    for i in range(len(list1)):
        if list1[i] == '1':
            count = count + 1
        else:
            count = 0
        if count == 5:
            list1.insert(i + 1, '0')

    flag1=['0','1','1','1','1','1','1','0']
    for i in range(0,8):
        list1.insert(0,flag1[i])
        list1.append(flag1[i])
    print("after stuffing")
    print("AT SENDER SIDE",list1)

    #Receiver
    for i in range(0,8):
        del list1[0]
        list1.pop()
    count = 0
    for i in range(len(list1)-1):
        if list1[i] == '1':
            count = count + 1
        else:
            count = 0
        if count == 5:
            del list1[i + 1]


    print("AT RECEIVER SIDE",list1)

while True:
    z = int(input("enter 1 for Byte Stuffing/n 2 for bit stuffing    3 for exit:"))
    if z==1:
        ByteStuffing()
        
    elif z==2:
        BitStuffing()
       
    elif z==3:
        break
    else:
        print("enter a valid input")


# In[ ]:




