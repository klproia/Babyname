#begining 
print ("Names are now being processed")
namelist = list()
list1 = list()
list2 = list()
list3 = list()

#opening the files
try:
    femalelist = open('FemaleNames.txt', 'r')
except:
    print ("Error: FemaleNames.txt cannot be opend")
    quit() 

try:
    malelist = open('MaleNames.txt', 'r')
except:
    print ("Error: MaleNames.txt cannot be opened")
    quit()

#read files into the namelist
for name in femalelist:    
   # namelist.append(name.rstrip())
    namelist += [name.rstrip()]
    #print(name.rstrip())       
femalelist.close()
    
for name in malelist:
    #namelist.append(name.rstrip())
    namelist += [name.rstrip()]
    #print(name.rstrip())
malelist.close()

#sort the names
namelist.sort()

f1 = open("AtoInames.txt", "w")
f2 = open("JtoRnames.txt", "w")
f3 = open("StoZnames.txt", "w")
for name in namelist:
    if (name.startswith('A')) or (name.startswith('B')) or (name.startswith('C')) or (name.startswith('D')) or (name.startswith('E')) or (name.startswith('F')) or (name.startswith('G')) or (name.startswith('H')) or (name.startswith('I')) :
        list1 += [name]        
        f1.write(name)
        f1.write(' ') 
        #print(name)
        continue

    elif (name.startswith('J')) or (name.startswith('K')) or (name.startswith('L')) or (name.startswith('M')) or (name.startswith('N')) or (name.startswith('O')) or (name.startswith('P')) or (name.startswith('Q')) or (name.startswith('R')) :
        list2 += [name]        
        f2.write(name)
        f2.write(' ') 
        #print(name)
        continue

    elif (name.startswith('S')) or (name.startswith('T')) or (name.startswith('U')) or (name.startswith('V')) or (name.startswith('W')) or (name.startswith('X')) or (name.startswith('Y')) or (name.startswith('Z')) :
        list3 += [name]        
        f3.write(name)
        f3.write(' ') 
        #print(name)
        continue






#list1 = namelist.startswith('A')#('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
#list2 = namelist.sort()#('J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R')
#list3 = namelist.sort()#('S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

#list1 = open('AtoInames.txt', 'a')
#list2 = open('JtoRnames.txt', 'a')
#list3 = open('StoZnames.txt', 'a')

#open and read the file after the appending:
f1 = open("AtoInames.txt", "r")
f2 = open("JtoRnames.txt", "r")
f3 = open("StoZnames.txt", "r")

#print(f1.read())
#print(f2.read())
#print(f3.read())

f1.close()
f2.close()
f3.close()

#print names and output

print('Names beginning with A - I:  ', list1)
print('Names beginning with J - R:  ', list2)
print('Names beginning with S - Z:  ', list3) 
    

#open output files
#try:
#    a2inames =
#    j2rnames =
#    s2znames =

#    for names in namelist:
#        print(name)
#        if

 #       elif

#        elif
#except:
#    print ('Error: Problem writing to file')
 #   quit() 
