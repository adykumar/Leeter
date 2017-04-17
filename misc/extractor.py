

if __name__=="__main__":
	fin= open("./all.txt","r")
	all= fin.readlines()
	dic={}
	for line in all:
		parts= line.split()
		if len(parts)>=2:
			part1= parts[0]
			if part1 not in dic:
				dic[int(part1)]= []
				dic[int(part1)].append(	parts[-1] )
				txt=""
				for i in range(1, len(parts)-2):
					txt= txt+parts[i].lower()+"-"
				txt= txt.replace('\x92','')
				txt= txt.replace('\x96','')
				txt= txt.replace('--','-')
				dic[int(part1)].append( txt )
					
			

	fout= open("ProblemSource.txt","w")
	for key in dic:
		fout.write("\n"+str(key)+"##")
		fout.write(dic[key][0].lower()+"##")
		fout.write(dic[key][1].lower().rstrip("-"))
	fout.close()
	
			
