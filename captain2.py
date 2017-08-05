#-------------------------------------------------------------------------------
# Name:        Captain
# Purpose:      Lead the laggards!
# Author:      Swadhyaya
# Created:     13/02/2017
# Copyright:   (c) Swadhyaya 2017
#-------------------------------------------------------------------------------
import os,sys,random
from HTMLParser import HTMLParser
import urllib2
args= sys.argv
test=[104]
content=""
arg=""

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global arg
        if tag=="meta" and attrs[0]==('name', 'description'):
            try:
                global content
                content= attrs[1][1]
            except: pass

        start= "{\'value\': \'"+arg+"\'"
        stop="\'value\'"
        if tag=="div":
            for each in attrs:
                if each[0]=='ng-init':
                    parts= each[1].split(",")
                    flag= False
                    print start
                    for line in parts:
                        print line

def isInternetOn(link,attempt):
    try:
        urllib2.urlopen(link, timeout=4)
        print "Connected..."
        return True
    except:
        print "XXXX  Cant connect: Attempt ",attempt
        return False

def writer(name, cont, link, arg2):
    if "LeetCode Online Judge" in cont:
        cont= "Restricted question"
        print cont
    cont=cont.lstrip()
    if "/" in cont and "\\" in cont: pass
    else:
        cont= cont.replace("\r","")
    fout= open(name,"a")
    fout.write("\"\"\"\n")
    fout.write(link+"\n\n")
    fout.write(cont)
    fout.write("\n\"\"\"")
    fout.close()

def populate(filename, link, arg2):
    global arg
    arg= arg2
    flag= False
    for i in range(4):
        if isInternetOn(link,i):
            flag= True
            break
    if not flag: return
    print filename, link
    response= urllib2.urlopen(link)
    html= response.read().decode('utf-8')
    #print html
    parser= MyHTMLParser()
    print "--------"
    #parser.feed(html)
    try:
        parser.feed(html)
        writer(filename, content, link, arg2)
    except: print "parser error"

def randomSelector(arg1,arg2):
    probdict={}; easy={}; med={}; hard={}
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
    if 'ea' in arg1:
        k= random.choice(easy.keys())
    elif 'me' in arg1:
        k= random.choice(med.keys())
    elif 'ha' in arg1:
        k= random.choice(hard.keys())
    else:
        k= random.choice(probdict.keys())
    print k,probdict[k]

    if test!=[]: k=test[0] #####

    link= probdict[k][1]
    link= link.lower()
    link= link.replace(" ","-")
    httplink= "https://leetcode.com/problems/"+link
    return k,link, httplink

def main():
    print "****************"
    try: arg1= args[1] # easy, medium or hard?
    except: arg1="help" # keep easy as default
    if "-h" in arg1 or "help" in arg1:
        print "\nCommand->  python captain.py level(easy/med/hard) precode with language(python/java/cpp)"
        return
    try: arg2= args[2] # initiate prewritten code?
    except: arg2=""

    num, name, link= randomSelector(arg1, arg2) # return random number, name and link of problem

    cmd="atom ./test/"+str(num)+"_"+name+".txt"
    print "Initiating... "+cmd
    arg2= 'py' ## test
    allowed_arg2=['python','java','cpp','']
    for alw in allowed_arg2:
        if arg2 not in alw: continue
        populate(cmd.split()[1], link, alw)
        os.system(cmd)

if __name__ == '__main__':
    main()
