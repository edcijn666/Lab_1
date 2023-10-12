# Create the scaling function

# YOUR CODE HERE


def scale_data(arr):
    
    x_arr = np.array(arr[:, 0:1])
    y_arr = np.array(arr[:, 1:2])
    z_arr = np.array(arr[:, 2:3])
    eta_arr = np.array(arr[:, 3:4])
    phi_arr = np.array(arr[:, 4:5])
    energy_arr = np.array(arr[:, 5:6])
    
    x_arr = (x_arr - np.mean(x_arr))/np.std(x_arr)
    y_arr = (y_arr - np.mean(y_arr))/np.std(y_arr)
    z_arr = (z_arr - np.mean(z_arr))/np.std(z_arr)
    eta_arr = (eta_arr - np.mean(eta_arr))/np.std(eta_arr)
    phi_arr = (phi_arr - np.mean(phi_arr))/np.std(phi_arr)
    energy_arr = (energy_arr - np.mean(energy_arr))/np.std(energy_arr)
    
    scaled_data = np.concatenate((x_arr, y_arr, z_arr, eta_arr, phi_arr, energy_arr), axis = 1)    
    
    return scaled_data
