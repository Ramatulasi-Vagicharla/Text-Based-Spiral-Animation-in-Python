import time

def draw_spiral():
    delay = 0.1  # Delay between frames (in seconds)
    size = 20    # Size of the spiral

    for i in range(size):
        # Clear the screen (simulated by printing newlines)
        print("\n" * 50)

        # Draw the spiral
        for j in range(size):
            for k in range(size):
                if j == i and k < size - i:
                    print("*", end=" ")
                elif k == size - i - 1 and j < size - i:
                    print("*", end=" ")
                elif j == size - i - 1 and k >= i:
                    print("*", end=" ")
                elif k == i and j >= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

        # Pause for a moment to create animation
        time.sleep(delay)

# Run the spiral animation
draw_spiral()