print(" #fghyui    hu      ]W    gtfyhi=loo     erw4!45op     Ert&(pxo    #@*h+lport    iuuurtWe.")
print(" #f           #  k    W     .D              RT         Io     As         lk   hj               kl      ko")
print(" #ukokk    hj    h }$      hu             ko         $5     Pk        kl    buhy9         rtoppkGY"  )
print(" #r          er      kpl     ,l               hy         ji       qi        yu    ji                ji   RR   ")
print(" #yjikoo    ko       lo      mkjippp-    p[pp[[[[pp       ncxxxxxx     kookokoko    Qo    rR")
print(' '*20+'Version: Encoder v0.0.1.5')
print('.'*150)
print('@copyright Bijoy_Maji')
print('By - Bijoy Maji. Email:- majibijoy00@gmail.com')
print('Note: There have a problem with some key. if you find it , please mail me the key at majibijoy00@gmail.')
print('.'*150)
import random
import math as m
#input stering
in_put=input('Enter your string:')
#genarate a key for encription

output=[in_put[i] for i in range(len(in_put))]
#gggggsjgfdvghggjgsjg
words_list1=[['l', 'z', 'x', 'c', 'v', 'b','u','i','o','p','a','s'],
            ['d', 'f', 'g', 'h', 'j', 'k', 'q','w','e','r','t','y'],
            ['n', 'm', '~', '!', '#', '$', '%', '^', '&', '*', '(', ')'],
            ['_', '+', '@', '-', '=', '{', '}', '|', '[', ']', ':', '"'],
            ['`', ';', "'", '<', '>', '?', ',', '.', '/', '€', '¤', ' '],
            ['Z', 'X', 'C', 'V', 'B', 'Y', 'U', 'I', 'O', 'P', 'A', 'S'],
            ['D', 'F', 'G', 'H', 'J', 'K', 'L','Q', 'W', 'E', 'R', 'T' ],
            ['N', 'M', '0','5', '6', '7', '8', '9','1', '2', '3', '4']]
lower_words="qwertyuiopasdfghjklzxcvbnm"
upper_words=lower_words.upper()
number="0123456789"
symbols='''~!#$%^&*()_+@-={}|[]:"`;'<>?,./€¤ '''
words=lower_words+symbols+upper_words+number
words_list=[words[i] for i in range(len(words))]
output1=[words_list.index(i) for i in output]

xp,yp,zp=[],[],[]
chack_key=input("Have you a key ? (y/n):")
yes1=['y','Y','yes','Yes']
no1=['n','N','No','no']
key=[]
if chack_key in no1:
#key work
        key=[str(int(random.uniform(0,9))) for i in range (10) ]
elif chack_key in yes1:
        key_in=input('Input our key: ')
        key_2=['@','$', 'G','A','#','%','X','!','_','+','/','&','z','r','H','Q','W','D','Y','~']
        key_1=[key_in[i] for i in range(len(key_in))]
        j=int(key_1[10])
        key_3=[]
        key_4=[]
        position=[]
        z=[]
        for i in range(12,len(key_1),2):
            key_3.append(key_1[i])
        for k in key_1[:10]:
            if k in key_2:
                key_4.append(k)
                z.append(key_1.index(k))
                position.append(key_2.index(k)-j)
        y=[]
        for l in range (min(position),max(position)+1):
            y.append(key_3[position.index(l)])
        c=0
        for a in z:
            key_1[a]=y[c]
            c=c+1
        key=key_1[:10]
else:
    print('Sorry!')
    
# mixing word with key
word_with_key=[]
for p in key:
    word_with_key.append(8-int(p))
for q in word_with_key:
    if q==8:
        word_with_key.remove(q)

for i in word_with_key:
    if word_with_key.count(i)>1:
        word_with_key.remove(i)

key_len_en=len(word_with_key)
for i in range(8):
    if i not in word_with_key:
        word_with_key.append(i)

#print ('word_with_key: ',word_with_key)
new_words_list=[]
for i in word_with_key:
    new_words_list.append(words_list1[i])
for j in output1 :
    a1=int((j+1)/12)
    b1=int((j+1)%12)
    yp.append(b1-1)
    if (j+1)%12==0:
        xp.append(a1-1)
        zp.append(new_words_list[a1-1][b1-1])
    else:
        xp.append(a1)
        zp.append(new_words_list[a1][b1-1])



key_2=['@','$', 'G','A','#','%','X','!','_','+','/','&','z','r','H','Q','W','D','Y','~']
j=int(random.uniform(-1,5))
main_constant=j
x=[]
for i in key:
    position=key.index(i)
    counter =0
    if key.count(i)>1:
        x.append(i)
        j3=int(random.uniform(0,len(key_2)))
        x.append(key_2[j3])
        position1=key.index(i)
        j+=1
        key[key.index(i,position1+1)]=key_2[j]
key.append(str(main_constant))
j2=int(random.uniform(11,len(key_2)))
key.append(key_2[j2])
key=key+x
key_3=key[0]
for key_in_word in range(1,len(key)):
    key_3=key_3+key[key_in_word]
print('Your key is: ',key_3)
#print('Words=',new_words_list)
#print('Your encoded string:',output)
#print('Out put:',output1)
#print(xp,yp,zp)
result=zp[0]
for key_in_word in range(1,len(zp)):
    result=result+zp[key_in_word]
print('Encoded string is :',result)

