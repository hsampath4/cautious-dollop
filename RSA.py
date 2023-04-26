from tkinter import *
import random
import sympy
import gmpy2

global p, q, e, d, m, n, cipher
top = Tk()
top.geometry("650x250")
head = StringVar()
label = Label(top, textvariable=head, relief=RAISED)
head.set("RSA Encryption/Decryption")
label.pack()
frame = Frame(top)
prime = StringVar()
subhead1 = Label(frame, textvariable=prime)
prime.set("1. Generate primes p and q")


def genPrime():
    # Generate two random prime numbers p and q
    gen_p = random.randint(1000, 5000)
    while not sympy.isprime(gen_p):
        gen_p = random.randint(1000, 5000)

    gen_q = random.randint(2, 4999)
    while not sympy.isprime(gen_q):
        gen_q = random.randint(2, 4999)

    return gen_p, gen_q


def displayPrime():
    genp = genPrime()[0]
    genq = genPrime()[1]
    global p, q
    p = genp
    q = genq
    subhead4.configure(text=f"{genp}")
    subhead6.configure(text=f"{genq}")


def displayN():
    global n
    n = p * q
    subheadDisplayN.configure(text=f"{n}")


def submit():
    global e
    e = InputE.get()
    print("User entered encryption key:", e)


def submitM():
    global m
    m = InputM.get()
    print("User entered message:", m)


def calD():
    global d
    Phi_n = (p - 1) * (q - 1)
    if gmpy2.gcd(int(e), Phi_n) == 1:
        d = gmpy2.invert(int(e), Phi_n)
        print(d)
    subheadDisplayD.configure(text=f"{d}")


def encrypt():
    global cipher
    cipher = gmpy2.powmod(int(m), int(e), int(n))
    subheadDisplayC.configure(text=f"{cipher}")


def decrypt():
    decryptText = gmpy2.powmod(int(cipher), int(d), int(n))
    subheadDisplayMsg.configure(text=f"{decryptText}")


B2 = Button(frame, text="Gen", command=displayPrime)
primeLimit = StringVar()
subhead2 = Label(frame, textvariable=primeLimit)
primeLimit.set("( 1000 < p, q < 5000 )")

subhead1.pack(side="left")
B2.pack(side="left")
subhead2.pack(side="left")
frame.pack(anchor="w")

# Displaying p value
frame1 = Frame(top)
display_p = StringVar()
subhead3 = Label(frame1, textvariable=display_p)
display_p.set("p = ")
subhead3.pack(side="left")
frame1.pack(anchor="w")

subhead4 = Label(frame1, text="", relief="solid", width=250)
# subhead4.config()
subhead4.pack(side="left")
frame1.pack(anchor="w")

# Displaying q value
frame2 = Frame(top)
display_q = StringVar()
subhead5 = Label(frame2, textvariable=display_q)
display_q.set("q = ")
subhead5.pack(side="left")
frame2.pack(anchor="w")

subhead6 = Label(frame2, text="", relief="solid", width=250)
subhead6.pack(side="left")
frame2.pack(anchor="w")

# Computing n
frameCompute = Frame(top)
numb = StringVar()
subheadN = Label(frameCompute, textvariable=numb)
numb.set("2. Compute n=pq")

BCompute = Button(frameCompute, text="Com", command=displayN)
disp = Label(frameCompute, text="n=")
subheadDisplayN = Label(frameCompute, text="", relief="solid", width=250)

subheadN.pack(side="left")
BCompute.pack(side="left")
disp.pack(side="left")
subheadDisplayN.pack(side="left")
frameCompute.pack(anchor="w")

# Input encryption key
frameE = Frame(top)
En = StringVar()
subheadE = Label(frameE, textvariable=En)
En.set("3. Set public key e  e=")
subheadInputE = Label(frameE, text="", relief="solid", width=250)

# Create an entry widget
InputE = Entry(subheadInputE)

# Create a button to submit the input
BInputE = Button(frameE, text="Submit", command=submit)

subheadE.pack(side="left")
subheadInputE.pack(side="left")
InputE.pack(side="left")
BInputE.pack(side="left")
frameE.pack(anchor="w")

# Computing decryption key d
frameComputeD = Frame(top)
De = StringVar()
subheadComputeD = Label(frameComputeD, textvariable=De)
De.set("4. Calculate the private key d")

BComputeD = Button(frameComputeD, text="Cal", command=calD)
dispD = Label(frameComputeD, text="d=")
subheadDisplayD = Label(frameComputeD, text="", relief="solid", width=250)

subheadComputeD.pack(side="left")
BComputeD.pack(side="left")
dispD.pack(side="left")
subheadDisplayD.pack(side="left")
frameComputeD.pack(anchor="w")

# Input Message
frameM = Frame(top)
Mes = StringVar()
subheadM = Label(frameM, textvariable=Mes)
Mes.set("5. Input a message m  m=")
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

# Computing Ciphertext
frameComputeC = Frame(top)
ciph = StringVar()
subheadC = Label(frameComputeC, textvariable=ciph)
ciph.set("6. Encrypt c=m^e mod n")

BComputeC = Button(frameComputeC, text="Enc", command=encrypt)
dispC = Label(frameComputeC, text="c=")
subheadDisplayC = Label(frameComputeC, text="", relief="solid", width=250)

subheadC.pack(side="left")
BComputeC.pack(side="left")
dispC.pack(side="left")
subheadDisplayC.pack(side="left")
frameComputeC.pack(anchor="w")

# Decrypting to find message
frameComputeMsg = Frame(top)
msg = StringVar()
subheadMsg = Label(frameComputeMsg, textvariable=msg)
msg.set("7. Decrypt m=c^d mod n")

BComputeMsg = Button(frameComputeMsg, text="Dec", command=decrypt)
dispMsg = Label(frameComputeMsg, text="m=")
subheadDisplayMsg = Label(frameComputeMsg, text="", relief="solid", width=250)

subheadMsg.pack(side="left")
BComputeMsg.pack(side="left")
dispMsg.pack(side="left")
subheadDisplayMsg.pack(side="left")
frameComputeMsg.pack(anchor="w")

top.mainloop()
