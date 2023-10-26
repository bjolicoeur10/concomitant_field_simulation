import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import h5py
from matplotlib.animation import FuncAnimation

def split_matrix(original_matrix):
    N, _, _, M = original_matrix.shape
    submatrix_size = 2
    std_deviations = []

    for i in range(N - submatrix_size + 1):
        for j in range(N - submatrix_size + 1):
            for k in range(N - submatrix_size + 1):
                submatrix = original_matrix[i:i+submatrix_size, j:j+submatrix_size, k:k+submatrix_size, :]
                std_deviation = np.std(submatrix)  # Calculate the standard deviation
                std_deviations.append(std_deviation)
                del submatrix  # Delete the submatrix to free memory

    return std_deviations

# Open the MATLAB v7.3 file using h5py
with h5py.File('Bc.mat', 'r') as file:
    Bc = file['Bc'][:]  # Load the data

# Reshape the data to the desired shape (11x11x11x60)
Bc = Bc.transpose(3, 2, 1, 0)
array_shape = Bc.shape
print(array_shape)
std_deviations_list = []

# for i in range(array_shape[3]):
#     temp = Bc[:,:,:,i]
#     temp = temp[:,:,:,np.newaxis]
#     std_deviations = split_matrix(temp)
#     std_deviations_list.append(std_deviations)
    
# std_deviations_list = np.array(std_deviations_list)
# print(std_deviations_list.size)
# new_shape = (array_shape[0]-1,array_shape[1] -1 , array_shape[2] -1, array_shape[3])
# reshaped_matrix = std_deviations_list.reshape(new_shape)
# print(reshaped_matrix.shape)


# Bc = reshaped_matrix
# Bc = Bc.transpose(2, 0, 1, 3)
# array_shape = Bc.shape
# print(array_shape)
def update(frame):
    ax.clear()
    sc = ax.scatter(x, y, z, c=Bc[:, :, :, frame].flatten(), cmap='viridis')  # Change 'viridis' to any colormap you prefer

    tick2[0] += 1  # Increment the value inside the list

    ax.set_xlabel(f'X {array_shape[0]} mm')
    ax.set_ylabel(f'Y {array_shape[1]} mm')
    ax.set_zlabel(f'Z {array_shape[2]} mm')
    ax.set_title(f'Magnetic Field mT: {frame} ms')
    
    # cbar = fig.colorbar(sc)
    left = 0.2
    bottom = 0.1
    width = 0.6  # Adjust the width to control the size
    height = 0.02  # Adjust the height to control the size
    cax = plt.axes([left, bottom, width, height])
    cbarlabel = 'Magnetic Field mT'
    cbar = fig.colorbar(sc, cax = cax,orientation='horizontal', label=cbarlabel)

    if (tick2[0] < 2):
    
        cbar.set_label(cbarlabel)
    else:
        cbar.remove()
        
        cbar.set_label(cbarlabel)
    
    return sc

# Set the number of frames based on the size of the Bc array
num_frames = array_shape[3]
tick2 = [0]  # Store the counter in a list

# Create a meshgrid for x, y, and z based on the array shape
x, y, z = np.meshgrid(np.arange(array_shape[0]), np.arange(array_shape[1]), np.arange(array_shape[2]))
x = x.flatten()
y = y.flatten()
z = z.flatten()

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, repeat=True, interval=500)  # Adjust interval as needed
print(Bc[20,20,20,50])
plt.show()

