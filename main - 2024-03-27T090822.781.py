import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_sequence(n):
    sequence = collatz_sequence(n)
    plt.plot(sequence, marker='o')
    plt.xlabel('Step')
    plt.ylabel('Number')
    plt.title(f'Collatz Sequence for n = {n}')
    plt.grid(True)
    plt.show()

# Example usage
starting_number = 27  # You can change this to any positive integer
plot_collatz_sequence(starting_number)
