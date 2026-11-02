#  #files
# x-> this mode will only create the file and if alreadynexists we will get an error back
# w
# a
# r 
# #
# MODE 1: X-> JUST TO CREate the FileExistsError#open ("garba.txt","x")
# #mode 2:w
# file =open("garba.txt","w")
# file.write("enjoy karo job hi job hai")

# #mode 3:a-> add the text at last.
# file = ope3n ("garbna.txt","a")
# file.write ("\n this message is newly added")
# file=open("garba.txt","r")
# print 

# """mode 4: r=read the content inside of the file 
# file=open("garba.txt","r")
# print(file.read())
# """

# with open("sample.txt","w") as file:
#     file.write("garba.txt")


def create_folder():
    name=input("tell your folder name:-")
    p=path(name)

    if p.exists():
        print("this folder name already exists plz try again")
        create_folder()
    else:
        p.mkdir()
        print("folder created")

print("press 1 for creating a new file:")
print("press 2 for reading any file")
print("press 3 for updating a folder ")
print("press 4 for deleting a folder")
print("press 5 for creating a file")
print("press 6 for reading a file")
print("press 7 for  updating a file")
print("press 8 for deleting a file")

res=int(input("tell your responses:-"))

if res==1:
    create_folder()
else:
    p.mkdir()
    print("folder craeted successfully!")
def create_folder():
    p
        
def read_folder():
    p=path("")
    name=list(p.rglob("*"))

    for i in range(len(names)):
        print(f"{i+1}:{names[i]}")
