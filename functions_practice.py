def hello(): 
    print("")

def pack(x,y,z):
   return[x,y,z]

def eat_lunch(list):
    if len(list) == 0:
        print("my lunch box is empty")
    else: 
            for x in range(len(list)):
                if x == 0:
                    print (f"First I eat {list[0]}")
                else:
                        print(f"Next I eat {list[x]}")


hello()
print(pack("x","y","z"))
eat_lunch(["gum", "biscuits", "kiwi", "strawberry"])
