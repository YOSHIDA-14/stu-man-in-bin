def create():
    with open("mark.dat","+ab") as f:
        name=input("Enter the name:")
        Roll=int(input("Enter the roll No:"))
        marks=int(input("enter the marks:"))
        l=[Roll,name,marks]
        import pickle as pi 
        pi.dump(l,f)
x=[]
def mod():
    with open ("mark.dat","rb+") as m:
        import pickle as pi
        while True:
                    try : 
                          x.append(pi.load(m))
                    except EOFError:
                          break
        Roll=int(input("Enter the Roll no to alter:"))
        for i in range(len(x)):
              if x[i][0]==Roll:
                    name=input("ENter the new name:")
                    Roll=int(input("ennter the Marks :"))
                    x[i][1]=name
                    x[i][2]=Roll
                    print(x[i])
    with open("mark.dat","wb+") as f:
          import pickle as pi 
          for i in x:
                pi.dump(i,f)







while True:
        respons=int(input("Type 1 to add records \n Type 2 to alter records"))
        if respons==1:
            create()
        elif respons==2:
           mod()
        else:
              print("Ill take a leave")
              break