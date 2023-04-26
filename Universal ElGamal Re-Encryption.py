from tkinter import *
import gmpy2

global x, y, m, r, s, X, Y, W, Z
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
    global r
    r = InputRand.get()
    print("User entered random number:", r)


def submitRands():
    global s
    s = InputRands.get()
    print("User entered random number s:", s)


def displayEnc():
    global X, W, Y, Z
    # Compute X
    A_r = gmpy2.powmod(int(y), int(r), int(p))
    X = gmpy2.f_mod(int(A_r) * int(m), int(p))
    # print("X : ", X)

    # Compute Y
    Y = gmpy2.powmod(int(g), int(r), int(p))
    print("Y : ", int(Y))
    # Compute W
    W = gmpy2.powmod(int(y), int(s), int(p))
    print("W : ", int(W))
    # Compute Z
    Z = gmpy2.powmod(int(g), int(s), int(p))
    print("Z : ", int(Z))

    EncMsg = (int(X), int(Y), int(W), int(Z))
    subheadDisplayEnc.configure(text=f"{EncMsg}")


def decrypt():
    Ypowx = gmpy2.powmod(int(Y), int(x), int(p))
    div = gmpy2.invert(int(Ypowx), int(p))
    print("div =", div)
    numerator = X * div
    decryptMsg = gmpy2.mod(int(numerator), int(p))
    print("Decrypted message = ", decryptMsg)

    Zpowx = gmpy2.powmod(int(Z), int(x), int(p))
    divi = gmpy2.invert(int(Zpowx), int(p))
    numerator1 = W * divi
    to_check = gmpy2.invert(numerator1, p)
    print("To Check = ", to_check)
    decryptMsg = gmpy2.mod(int(numerator), int(p))
    failedMsg = "𝑊/𝑍^𝑎 =1 mod p does not exist M rejected"
    if to_check != 0:
        subheadDisplayM.configure(text=f"{decryptMsg}")
    else:
        subheadDisplayM.configure(text=f"{failedMsg}")


top = Tk()
top.geometry("650x250")
head = StringVar()
label = Label(top, textvariable=head, relief=RAISED)
head.set("Universal ElGamal Re-Encryption")
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

# Choose Random number r
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

# Choose Random number s
frameRands = Frame(top)
rans = StringVar()
subheadRands = Label(frameRands, textvariable=rans)
rans.set("4.2 Choose a random number s     s =")
subheadInputRands = Label(frameRands, text="", relief="solid", width=250)

# Create an entry widget
InputRands = Entry(subheadInputRands)

# Create a button to submit the input
BInputRands = Button(frameRands, text="Submit", command=submitRands)

subheadRands.pack(side="left")
subheadInputRands.pack(side="left")
InputRands.pack(side="left")
BInputRands.pack(side="left")
frameRands.pack(anchor="w", padx=10)

# Encryption of message M
frameComputeEnc = Frame(top)
CompEnc = StringVar()
subheadEnc = Label(frameComputeEnc, textvariable=CompEnc)
CompEnc.set("4.3 Compute (X,Y,W,Z) : encryption of the message M ")

BComputeEnc = Button(frameComputeEnc, text="Com", command=displayEnc)
dispEnc = Label(frameComputeEnc, text="Encrypted message=")
subheadDisplayEnc = Label(frameComputeEnc, text="", relief="solid", width=250)

subheadEnc.pack(side="left")
BComputeEnc.pack(side="left")
dispEnc.pack(side="left")
subheadDisplayEnc.pack(side="left")
frameComputeEnc.pack(anchor="w", padx=10)

# Compute m by decrypting
frameComputeM = Frame(top)
M = StringVar()
subheadCompM = Label(frameComputeM, textvariable=M)
M.set("M = X/Y^a ")

BComputeM = Button(frameComputeM, text="Com", command=decrypt)
dispM = Label(frameComputeM, text="m=")
subheadDisplayM = Label(frameComputeM, text="", relief="solid", width=250)

subheadCompM.pack(side="left")
BComputeM.pack(side="left")
dispM.pack(side="left")
subheadDisplayM.pack(side="left")
frameComputeM.pack(anchor="w", padx=20)

top.mainloop()
