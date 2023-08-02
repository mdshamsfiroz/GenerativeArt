import numpy as np
import matplotlib.pyplot as plt

# Set the dimensions of the image
width, height = 100, 100

# Create a blank canvas (3 channels for RGB colors)
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# Define the number of iterations to create the generative art
num_iterations = 10000

# Iterate and randomly fill the canvas with colors and patterns
for _ in range(num_iterations):
    x, y = np.random.randint(0, width), np.random.randint(0, height)
    r, g, b = np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)
    size = np.random.randint(1, 10)  # Random size for the pattern
    canvas[y -2* size:y + 7*size, x - 6*size:x + 5*size] = [r, g, b]

# Display the generative art image
plt.imshow(canvas)
plt.axis('off')  # Turn off axis ticks and labels
plt.show()
