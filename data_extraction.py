# Extract only x, y, z, eta, phi and energy columns from the dataset and stack them along column direction
# Name this new 2D array CMS_calori_dataset_np_sub. 
# The array should have dimension 420 (rows) x 6 (columns)

# YOUR CODE HERE

CMS_calori_dataset_np_sub = CMS_calori_dataset_np[:, 1:7]
print(CMS_calori_dataset_np_sub)
print(CMS_calori_dataset_np_sub.shape)
