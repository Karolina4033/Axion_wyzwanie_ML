import numpy as np

zero=np.array([1,0], dtype=complex)
one=np.array([0,1], dtype=complex)

# Bramki jednokubitowe:
I = np.array([[1, 0],
                    [0, 1]], dtype=complex)

X = np.array([[0,1],
                    [1,0]], dtype=complex)

Z = np.array([[1,0],
                    [0,-1]], dtype=complex)

H = np.array([[1,1],
                    [1,-1]], dtype=complex)/ np.sqrt(2)

def Ry(theta):
    gate = np.array([[np.cos(theta/2), -np.sin(theta/2)],
                     [np.sin(theta/2), np.cos(theta/2)]], dtype=complex)
    return gate

#Bramki dwukubitowe
CNOT = np.array([ #patrz - KOLUMNY
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=complex)

#dodatkowo chciałabym sprawdzić (wiedza z kolejnych wykładów) działania bramki CZ
CZ = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, -1]
], dtype=complex)

def apply_gate(gate, state):
    return gate @ state # @ - mnożenie macierzowe

def measure(state):
    probabilities = np.abs(state) ** 2 #prawdopodobienstwa danych stanów
    result = np.random.choice(len(state), p=probabilities) #wybieramy 1/0 z danym prawdopodobienstwem
    n = int(np.log2(len(state))) #liczy ile kubitów
    return format(result, f"0{n}b")

# TEST 1: H * H |0> = |0>
print("\nCzy  H * H |0> = |0>")
state = zero
state = apply_gate(H, state)
print("Stan po pierwszym H\n", state)
state = apply_gate(H, state)
print("Stan po H * H:\n", state)

#TEST 2: BRAMKA Ry
state = Ry(np.pi) @ zero
print("\n Działanie bramki Ry:")
print("Stan początkowy: ", zero)
print("Stan po Ry(pi)" , np.round(state, 5))




# TEST 3: STAN BELLA
zero_zero=np.kron(zero, zero)
H_first = np.kron(H, I)
X_first = np.kron(X, I)
Z_first = np.kron(Z, I)


# Stan Phi+
phi_plus = CNOT @ H_first @ zero_zero

# Stan Phi-
phi_minus = Z_first @ CNOT @ H_first @ zero_zero

# Stan Psi+
psi_plus = X_first @ CNOT @ H_first @ zero_zero

# Stan Psi-
psi_minus = Z_first @ X_first @ CNOT @ H_first @ zero_zero
print("\n\nstany Bella:" )
print("Phi+:\n", phi_plus)
print("Phi-:\n", phi_minus)
print("Psi+:\n", psi_plus)
print("Psi-:\n", psi_minus)

#Sprawdźmy stany Bella dla wielokrotnego pomiaru:
def stany_bella(stan):
    results = {"00": 0, "01": 0, "10": 0, "11": 0}
    for _ in range(10000):
        outcome = measure(stan)
        results[outcome] += 1
    return results

print("\nWyniki dla 10000 pomiarów dla stanu phi + :",stany_bella(phi_plus))
print("\nWyniki dla 10000 pomiarów dla stanu phi - :",stany_bella(phi_minus))
print("\nWyniki dla 10000 pomiarów dla stanu psi + :",stany_bella(psi_plus))
print("\nWyniki dla 10000 pomiarów dla stanu psi - :",stany_bella(psi_minus))



#TEST 4: Zbudowanie CNOT z CZ i dwóch bramek H?
H_second = np.kron(I, H)

CNOT_from_CZ = H_second @ CZ @ H_second

print("\n\nCNOT z CZ i 2 H")
print(np.round(CNOT_from_CZ), 5)
print("\nZwykły CNOT")
print(CNOT)
print("\nCzy CNOT to CZ i 2 H?", np.allclose(CNOT,CNOT_from_CZ))
