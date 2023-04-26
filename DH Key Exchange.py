from tkinter import *
import gmpy2

global x, X, y, Y, k1, k2
p = 65537
g = 3


def submit():
    global x
    x = InputRand.get()
    print("User entered random number:", x)


def submitY():
    global y
    y = InputRandy.get()
    print("User entered random number:", y)


def displayX():
    global X
    X = gmpy2.powmod(int(g), int(x), int(p))
    print("Computed X", X)
    subheadDisplayX.configure(text=f"{X}")


def displayY():
    global Y
    Y = gmpy2.powmod(int(g), int(y), int(p))
    print("Computed Y", Y)
    subheadDisplayY.configure(text=f"{Y}")


def displayK1():
    global k1
    k1 = gmpy2.powmod(int(Y), int(x), int(p))
    subheadDisplayK1.configure(text=f"{k1}")


def displayK2():
    global k2
    k2 = gmpy2.powmod(int(X), int(y), int(p))
    subheadDisplayK2.configure(text=f"{k2}")


top = Tk()
top.geometry("650x250")
head = StringVar()
label = Label(top, textvariable=head, relief=RAISED)
head.set("Diffie-Hellman Key Exchange")
label.pack()
frame = Frame(top)
disp = StringVar()
subhead1 = Label(frame, textvariable=disp)
disp.set("0. Given a large prime p=65537, a primary root g=3")
subhead1.pack(side="left")
frame.pack(anchor="w")

# Input a random number, x
frameRand = Frame(top)
rand = StringVar()
subheadRand = Label(frameRand, textvariable=rand)
rand.set("1. Choose a random number x")
subheadInputRand = Label(frameRand, text="", relief="solid", width=250)

# Create an entry widget
InputRand = Entry(subheadInputRand)

# Create a button to submit the input
BInputRand = Button(frameRand, text="Submit", command=submit)

subheadRand.pack(side="left")
subheadInputRand.pack(side="left")
InputRand.pack(side="left")
BInputRand.pack(side="left")
frameRand.pack(anchor="w")

# Compute X=g^x mod p
frameComputeX = Frame(top)
textX = StringVar()
subheadX = Label(frameComputeX, textvariable=textX)
textX.set("2. Compute X=g^x mod p")

BComputeX = Button(frameComputeX, text="Com", command=displayX)
dispX = Label(frameComputeX, text="X=")
subheadDisplayX = Label(frameComputeX, text="", relief="solid", width=250)

subheadX.pack(side="left")
BComputeX.pack(side="left")
dispX.pack(side="left")
subheadDisplayX.pack(side="left")
frameComputeX.pack(anchor="w")

# Input a random number, y
frameRandy = Frame(top)
randy = StringVar()
subheadRandy = Label(frameRandy, textvariable=randy)
randy.set("3. Choose a random number y")
subheadInputRandy = Label(frameRandy, text="", relief="solid", width=250)

# Create an entry widget
InputRandy = Entry(subheadInputRandy)

# Create a button to submit the input
BInputRandy = Button(frameRandy, text="Submit", command=submitY)

subheadRandy.pack(side="left")
subheadInputRandy.pack(side="left")
InputRandy.pack(side="left")
BInputRandy.pack(side="left")
frameRandy.pack(anchor="w")

# Compute Y=g^y mod p
frameComputeY = Frame(top)
textY = StringVar()
subheadY = Label(frameComputeY, textvariable=textY)
textY.set("4. Compute Y=g^y mod p")

BComputeY = Button(frameComputeY, text="Com", command=displayY)
dispY = Label(frameComputeY, text="Y=")
subheadDisplayY = Label(frameComputeY, text="", relief="solid", width=250)

subheadY.pack(side="left")
BComputeY.pack(side="left")
dispY.pack(side="left")
subheadDisplayY.pack(side="left")
frameComputeY.pack(anchor="w")

# Calculate the session key K=gxymod p
frameK = Frame(top)
dispK = StringVar()
subheadK = Label(frameK, textvariable=dispK)
dispK.set("5. Calculate the session key K=g^xy mod")
subheadK.pack(side="left")
frameK.pack(anchor="w")

# Compute K1
frameComputeK1 = Frame(top)
K1Text = StringVar()
subheadK1 = Label(frameComputeK1, textvariable=K1Text)
K1Text.set("K=Y^x mod p=")

subheadDisplayK1 = Label(frameComputeK1, text="", relief="solid", width=50)
BComputeK1 = Button(frameComputeK1, text="Com", command=displayK1)



# Compute K2
K2Text = StringVar()
subheadK2 = Label(frameComputeK1, textvariable=K2Text)
K2Text.set("K=X^y mod p=")

subheadDisplayK2 = Label(frameComputeK1, text="", relief="solid", width=50)
BComputeK2 = Button(frameComputeK1, text="Com", command=displayK2)

subheadK1.pack(side="left")
subheadDisplayK1.pack(side="left")
BComputeK1.pack(side="left")

subheadK2.pack(side="left")
subheadDisplayK2.pack(side="left")
BComputeK2.pack(side="left")
frameComputeK1.pack(anchor="w")

top.mainloop()
