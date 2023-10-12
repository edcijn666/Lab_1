# Create the splitting function

def split_data(arr, split_proportions, axis):
    
    # YOUR CODE HERE
    # Returns a list of numpy sub-arrays according to split proportions
    
    if len(split_proportions) == 3:
        split_indices = [int(split_proportions[0]*arr.shape[axis]), int((split_proportions[0]+split_proportions[1])*arr.shape[axis]), arr.shape[axis]]
    else:
        split_indices = [int(split_proportions[0]*arr.shape[axis]), arr.shape[axis]]
    
    print(split_indices)
    split_data_list = np.split(arr, split_indices, axis = axis)
    
    return split_data_list
