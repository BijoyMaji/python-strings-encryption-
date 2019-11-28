print('DDDDDD     EEEEEEE    CCCCCCC      OOOOOOOO      EEEEEEEE   RRRRRR')
print('DD      DD   EE            CC               OO         OO      EE             RR     RR')
print('DD      DD   EEEEEE     CC               OO         OO      EEEEEE      RRRRRR'  )
print('DD      DD   EE            CC               OO         OO      EE             RR  RR   ')
print('DDDDDD     EEEEEEE   CCCCCCC       OOOOOOOO      EEEEEEEE   RR     RR')
print(' '*20+'Version: Decoder v0.0.1.5')
print('.'*150)
print('@copyright Bijoy_Maji')
print('By - Bijoy Maji. Email:- majibijoy00@gmail.com')
print('Note: There have a problem with some key. if you find it , please mail me the key at majibijoy00@gmail.')
print('.'*150)
import math as m
key=input('Input your key:')
key_2=['@','$', 'G','A','#','%','X','!','_','+','/','&','z','r','H','Q','W','D','Y','~']
key_1=[key[i] for i in range(len(key))]
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
out_come=key_1[:10]
word_with_key=[]
for p in out_come:
    word_with_key.append(8-int(p))
for q in word_with_key:
    if q==8:
        word_with_key.remove(q)

for i in word_with_key:
    if word_with_key.count(i)>1:
        word_with_key.remove(i)
for i in range(8):
    if i not in word_with_key:
        word_with_key.append(i)
#print(word_with_key)
in_put=input('Enter your encoded string:')
output=[in_put[i] for i in range(len(in_put))]
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
new_words_list=[]
for i in word_with_key:
    new_words_list.append(words_list1[i])
words_list2=[]
for i in new_words_list:
    words_list2=words_list2+i
result=""
try:
    for i in in_put:
        #print(i,words_list2.index(i))
        result+=words[words_list2.index(i)]
    print('Your decoded string is:',result)
except IndexError:
    print('Input corret values....')
