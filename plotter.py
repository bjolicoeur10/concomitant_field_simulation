import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import h5py
from matplotlib.animation import FuncAnimation

# Open the MATLAB v7.3 file using h5py
with h5py.File('Bc.mat', 'r') as file:
    Bc = file['Bc'][:]  # Load the data

# Reshape the data to the desired shape (11x11x11x60)
Bc = Bc.transpose(3, 2, 1, 0)

# Get the shape of the Bc array
array_shape = Bc.shape
print(array_shape)
# Create a meshgrid for x, y, and z based on the array shape
x, y, z = np.meshgrid(np.arange(array_shape[0]), np.arange(array_shape[1]), np.arange(array_shape[2]))

# Flatten the 3D coordinates
x = x.flatten()
y = y.flatten()
z = z.flatten()

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define a function to update the scatter plot for each frame
def update(frame):
    ax.clear()
    sc = ax.scatter(x, y, z, c=Bc[:, :, :, frame].flatten(), cmap='viridis')  # Change 'viridis' to any colormap you prefer
    return sc

# Set the number of frames based on the size of the Bc array
num_frames = array_shape[3]

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, repeat=True)  # Set repeat to True

# You can save the animation as a video file (e.g., .mp4) using ani.save('output.mp4')
# Or display it in a Jupyter Notebook using plt.show()

plt.show()
