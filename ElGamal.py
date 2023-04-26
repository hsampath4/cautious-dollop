from tkinter import *
import gmpy2

global x, y, m, r, R, c1, c2
p = 65537
g = 3


def submit():
    global x
    x = InputPri.get()
    print("User entered private key:", x)


def displayPubKey():
    global y
    y = gmpy2.powmod(int(g), int(x), int(p))
    print("Computed y", y)
    subheadDisplayPub.configure(text=f"{y}")


def submitM():
    global m
    m = InputM.get()
    print("User entered message:", m)


def submitRand():
    global r, R
    r = InputRand.get()
    R = gmpy2.powmod(int(y), int(r), int(p))
    print("User entered random number:", r)


def displayC1():
    global c1
    c1 = gmpy2.powmod(int(g), int(r), int(p))
    subheadDisplayC1.configure(text=f"{c1}")


def displayC2():
    global c2
    c2 = gmpy2.f_mod(int(m) * int(R), int(p))
    subheadDisplayC2.configure(text=f"{c2}")


def decrypt():
    div = gmpy2.invert(int(R), int(p))
    print("div =", div)
    numerator = c2 * div
    decryptMsg = gmpy2.mod(int(numerator), int(p))
    print("Decrypted message = ", decryptMsg)
    subheadDisplayM.configure(text=f"{decryptMsg}")


top = Tk()
top.geometry("650x250")
head = StringVar()
label = Label(top, textvariable=head, relief=RAISED)
head.set("ElGamal Encryption/Decryption")
label.pack()
frame = Frame(top)
disp = StringVar()
subhead1 = Label(frame, textvariable=disp)
disp.set("0. Given a large prime p=65537, a primary root g=3")
subhead1.pack(side="left")
frame.pack(anchor="w")

# Input private key
framePri = Frame(top)
pri = StringVar()
subheadPri = Label(framePri, textvariable=pri)
pri.set("1. Choose a private key x x =")
subheadInputPri = Label(framePri, text="", relief="solid", width=250)

# Create an entry widget
InputPri = Entry(subheadInputPri)

# Create a button to submit the input
BInputPri = Button(framePri, text="Submit", command=submit)

subheadPri.pack(side="left")
subheadInputPri.pack(side="left")
InputPri.pack(side="left")
BInputPri.pack(side="left")
framePri.pack(anchor="w")

# Computing public key
frameComputePub = Frame(top)
pubK = StringVar()
subheadPub = Label(frameComputePub, textvariable=pubK)
pubK.set("2. Compute the corresponding public key y=g^x mod p")

BComputePub = Button(frameComputePub, text="Com", command=displayPubKey)
dispPub = Label(frameComputePub, text="y=")
subheadDisplayPub = Label(frameComputePub, text="", relief="solid", width=250)

subheadPub.pack(side="left")
BComputePub.pack(side="left")
dispPub.pack(side="left")
subheadDisplayPub.pack(side="left")
frameComputePub.pack(anchor="w")

# Input Message
frameM = Frame(top)
Mes = StringVar()
subheadM = Label(frameM, textvariable=Mes)
Mes.set("3. Input a message m  m=")
subheadInputM = Label(frameM, text="", relief="solid", width=250)

# Create an entry widget
InputM = Entry(subheadInputM)

# Create a button to submit the input
BInputM = Button(frameM, text="Submit", command=submitM)

subheadM.pack(side="left")
subheadInputM.pack(side="left")
InputM.pack(side="left")
BInputM.pack(side="left")
frameM.pack(anchor="w")

# Encryption
frameE = Frame(top)
dispEnc = StringVar()
subheadE = Label(frameE, textvariable=dispEnc)
dispEnc.set("4. Encrypt")
subheadE.pack(side="left")
frameE.pack(anchor="w")

# Choose Random number
frameRand = Frame(top)
ran = StringVar()
subheadRand = Label(frameRand, textvariable=ran)
ran.set("4.1 Choose a random number r     r =")
subheadInputRand = Label(frameRand, text="", relief="solid", width=250)

# Create an entry widget
InputRand = Entry(subheadInputRand)

# Create a button to submit the input
BInputRand = Button(frameRand, text="Submit", command=submitRand)

subheadRand.pack(side="left")
subheadInputRand.pack(side="left")
InputRand.pack(side="left")
BInputRand.pack(side="left")
frameRand.pack(anchor="w", padx=10)

# Compute c1
frameComputeC1 = Frame(top)
C1 = StringVar()
subheadC1 = Label(frameComputeC1, textvariable=C1)
C1.set("4.2 Compute c1=g^r mod p")

BComputeC1 = Button(frameComputeC1, text="Com", command=displayC1)
dispC1 = Label(frameComputeC1, text="c1=")
subheadDisplayC1 = Label(frameComputeC1, text="", relief="solid", width=250)

subheadC1.pack(side="left")
BComputeC1.pack(side="left")
dispC1.pack(side="left")
subheadDisplayC1.pack(side="left")
frameComputeC1.pack(anchor="w", padx=10)

# Compute c2
frameComputeC2 = Frame(top)
C2 = StringVar()
subheadC2 = Label(frameComputeC2, textvariable=C2)
C2.set("4.3 Compute c2=m* y^r mod p")

BComputeC2 = Button(frameComputeC2, text="Com", command=displayC2)
dispC2 = Label(frameComputeC2, text="c2=")
subheadDisplayC2 = Label(frameComputeC2, text="", relief="solid", width=250)

subheadC2.pack(side="left")
BComputeC2.pack(side="left")
dispC2.pack(side="left")
subheadDisplayC2.pack(side="left")
frameComputeC2.pack(anchor="w", padx=10)

# Decryption
frameD = Frame(top)
dispDec = StringVar()
subheadD = Label(frameD, textvariable=dispDec)
dispDec.set("5. Decrypt C=(c1,c2 )")
subheadD.pack(side="left")
frameD.pack(anchor="w")

# Compute m by decrypting
frameComputeM = Frame(top)
M = StringVar()
subheadCompM = Label(frameComputeM, textvariable=M)
M.set("m=c2/(y ^ r)  mod p")

BComputeM = Button(frameComputeM, text="Com", command=decrypt)
dispM = Label(frameComputeM, text="m=")
subheadDisplayM = Label(frameComputeM, text="", relief="solid", width=250)

subheadCompM.pack(side="left")
BComputeM.pack(side="left")
dispM.pack(side="left")
subheadDisplayM.pack(side="left")
frameComputeM.pack(anchor="w", padx=20)

top.mainloop()
