sequences = []

def create_sequence():
    while True:
        num = float(input("Enter input number: "))
        if num != -1:
            sequences.append(num)
        else:
            break
    print(f'input sequence: {sequences}')

def sorted_sequence(sequence):
    for i in range(len(sequence)):
        pass

# main
create_sequence()