A=input('Please enter name 1:')
B=input('Please enter name 2:')
C=input('Please enter name 3:')
D=input('Please enter name 4:')
E=input('Please enter name 5:')
F=input('Please enter name 6:')
G=input('Please enter name 7:')
H=input('Please enter name 8:')
I=input('Please enter name 9:')
K=input('Please enter name10:')
word = input('Please enter word:')
A = A.title()
B = B.title()
C = C.title()
D = D.title()
E = E.title()
F = F.title()
G = G.title()
H = H.title()
I = I.title()
K = K.title()

L = A.count(word) + B.count(word) + C.count(word) + D.count(word) + E.count(word) + F.count(word) + G.count(word) + H.count(word) + I.count(word) + K.count(word)

M = word.title()

N = A.count(word) + B.count(word) + C.count(word) + D.count(word) + E.count(word) + F.count(word) + G.count(word) + H.count(word) + I.count(word) + K.count(word)

print(A,B,C,D,E,F,G,H,I,K, "\n", f"{word} -> {L}")