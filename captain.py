#-------------------------------------------------------------------------------
# Name:        Captain
# Purpose:      Lead the laggards!
#
# Author:      Swadhyaya
#
# Created:     13/02/2017
# Copyright:   (c) Swadhyaya 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys,random
args= sys.argv

def main():
    print "****************"
    try: arg1= args[1]
    except: arg1=""
    probdict={}
    easy={}
    med={}
    hard={}
    path= sys.path[0]
    fin = open(path+"/misc/all.txt","r")
    lines= fin.readlines()
    for line in lines:
        words= line.split()
        if len(words)<2: continue
        num= int(words[0])
        if num not in probdict:
            probdict[num]=[]
            probdict[num].append(words[-1])
            subj=''
            for i in range(1, len(words)-2):
                subj= subj+words[i]+' '
            subj= subj.replace('\x92','')
            probdict[num].append(subj.rstrip())
            if 'Easy' in probdict[num][0]:
                easy[num]= probdict[num]
            elif 'Medium' in probdict[num][0]:
                med[num]= probdict[num]
            elif 'Hard' in probdict[num][0]:
                hard[num]= probdict[num]
    #print easy
    #print med
    #print hard
    if 'ea' in arg1:
        k= random.choice(easy.keys())
    elif 'me' in arg1:
        k= random.choice(med.keys())
    elif 'ha' in arg1:
        k= random.choice(hard.keys())
    else:
        k= random.choice(probdict.keys())
    print k,probdict[k]

    link= probdict[k][1]
    link= link.lower()
    link= link.replace(" ","-")
    print "https://leetcode.com/problems/"+link


if __name__ == '__main__':
    main()
