#TOKENIZER

import sys

line = sys.stdin.readline()
cnt = 0
line = line.strip()

while line:

    cnt = cnt + 1
    print('# sent_id = ',cnt)
    text2 = line

    print('# text =', text2)
    apostr = '\' '
    
    for line in text2 :
        text3 = text2.replace('.',' .').replace('\'', apostr).replace(', ', ' , ').replace(': ', ' : ').replace(' (', ' ( ').replace(') ', ' ) ').replace('"', ' " ')
   

    space = ' '
    text4 = text3.replace(space, ('\n'))

    words = []

    for line in text4.split('\n'):
        words.append(line)

    count = 0
    for w in words:
        
        count = count + 1
        form = '%-5i %-20s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s' 
        print (form % (count,w,str('-'),str('-'),str('-'),str('-'),str('-'),str('-'),str('-'),str('-')))
    print()
    line = sys.stdin.readline()
    line = line.strip()

