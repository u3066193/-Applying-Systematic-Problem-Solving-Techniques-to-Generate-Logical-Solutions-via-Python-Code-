u3066193
 
Date: 17/09/2025

def diagram_a(A, B, C):
    # Intermediate steps
    D = A and B
    E = not (B and C)
    F = not A
    G = D or E
    H = F and C
    I = G or H
    J = not I
    return int(J)  # Output X

def diagram_b(A, B, C):
    K = not A
    L = K or B
    M = L and C
    return int(M)  # Output Y

# Accept binary inputs from user
def get_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val in [0, 1]:
                return val
            else:
                print("Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

# Main program
if __name__ == "__main__":
    print("Enter binary inputs (0 or 1) for A, B, and C:")
    A = get_input("A: ")
    B = get_input("B: ")
    C = get_input("C: ")

    X = diagram_a(A, B, C)
    Y = diagram_b(A, B, C)

    print(f"\nResults:")
    print(f"Diagram (a) Output (X): {X}")
    print(f"Diagram (b) Output (Y): {Y}")






