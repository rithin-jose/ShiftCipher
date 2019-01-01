import pickle
list1=[]
list2=[]
list3=[]

print "\t\t\tCeaser Cypher ver:2.0"
print "1.Encode"
print "2.History"

choice=raw_input("Enter your choice:")
if choice==1:
	n=int(input("Enter the length of the message"))
	shift_index=int(input("Enter the shift index"))

	for i in range(0,n):
		b=raw_input("Enter cypher letter:")
		list1[i].append(b)


	f1=open("decoded.txt",'w')
	pickle.dump(1,f1)

	for i in range(0,n):
		list1[i]=ord(list[i])+shift_index
	f2=open("encode.txt",'w')
	for i in range(0,n):
		list1[i]=chr(list[i])
	pickle.dump(list1,f2)
	f1.close()
	f2.close()

elif choice==2:
	f1=open("decoded.txt",'r')
	f2=open("encode.txt",'r')
	print pickle.load(f1)
	print pickle.load(f2)
	f1.close()
	f2.close()
