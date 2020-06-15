import pickle
temp=""

print ("\t\t\tCeaser Cypher ver:2.0")
print ("1.Encode")
print ("2.Decode")

choice=int(input("Enter your choice:"))
if choice==1:
	shift_index=int(input("Enter the shift index: "))
	uncoded=input("Enter cypher String: ")
	length=len(uncoded)
	for i in range(0,length):
		a=ord(uncoded[i])+shift_index
		temp = temp + chr(a)
	print("Encoded string is: "+ temp)

elif choice==2:
	shift_index=int(input("Enter the shift index: "))
	uncoded=input("Enter encoded String: ")
	length=len(uncoded)
	for i in range(0,length):
		a=ord(uncoded[i])-shift_index
		temp = temp + chr(a)
	print("decoded string is: "+ temp)
