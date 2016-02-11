import sys
f = open("anagram_out.txt","w")
def anagram(str1,str2) :
    if ( len(str1) == 1 ):
        list1.append(str2+str1)
        return
    i=0
    while  i < len(str1) :

        anagram(str1[0:i]+str1[i+1:],str2+str1[i:i+1])
        i=i+1

    return

x=str(sys.argv[1])
list1 = []
anagram(x,"")
list1=sorted(list1)

for y in range(0,len(list1)):
    f.write(list1[y])
    f.write("\n")
