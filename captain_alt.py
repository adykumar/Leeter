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

def help_menu():
	print "\nCommand:\npython captain_alt.py <level> <language> <optional:editor>"
        return
	
def main():
	##### HELP #####
	try:
		if "help" in args[1] or "-h" in args[1]:
			help_menu()
			return
	except: 
		help_menu()
		return
	################
		
	print "\n------------------Starting Leeter Auto:------------------"	
	
	""" Validating the arguments
	Arg1: level- easy/medium/hard
	Arg2: language- python, java, c++ etc.
	Arg3(optional): specify the editor to initiate automatically. Example: atom, npp etc.
	"""
	
	### Taking Arguments ###
	if   "ea" in args[1].lower(): level= "easy"
	elif "me" in args[1].lower(): level= "medium"
	elif "ha" in args[1].lower(): level= "hard"
	else:
		print "\nImproper Argument 1: Rerun and specify easy/medium/hard"
		return
	
	try:
		if   "py" in args[2].lower(): lang= "python"
		elif "ja" in args[2].lower(): lang= "java"
		elif "cp" in args[2].lower() or "c+" in args[2].lower(): lang= "c++" 
	except:
		print "\nUnsupported or Missing Language in Argument 2: Rerun and specify python/java/c++ etc "
		return
	try: 
		editor= args[3]
	except:
		editor=""
		pass

	##########################
	print level, lang, editor
	
	##### Get the Random Problem ####
	
"""
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

"""
if __name__ == '__main__':
    main()
