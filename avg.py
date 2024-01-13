import numpy as np
from PIL import Image

def calculate_ndvi(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB if it's not already
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Convert the image to a numpy array
    image_array = np.array(image)

    # Extract the red and near-infrared bands
    red_band = image_array[:, :, 0]
    nir_band = image_array[:, :, 2]

    # Calculate the NDVI
    ndvi = np.true_divide((nir_band - red_band), (nir_band + red_band), where=(nir_band + red_band) != 0)

    return ndvi

def calculate_average_ndvi(ndvi, threshold_low, threshold_high):
    # Create a mask for dense and sparse vegetation based on the thresholds
    dense_mask = (ndvi >= threshold_low) & (ndvi <= threshold_high)
    sparse_mask = (ndvi >= threshold_low) & (ndvi <= threshold_high)

    # Calculate the average NDVI for dense and sparse vegetation
    dense_avg = np.nanmean(ndvi[dense_mask])
    sparse_avg = np.nanmean(ndvi[sparse_mask])

    return dense_avg, sparse_avg

# Path to the jpg image
image_path = r'D:\Napane_March-June\JPG\June.jpg'

# NDVI thresholds for dense and sparse vegetation
dense_threshold_low = 0.36
dense_threshold_high = 1.00
sparse_threshold_low = 0.27 
sparse_threshold_high = 0.36

# Calculate the NDVI
ndvi = calculate_ndvi(image_path)

# Calculate the average NDVI for dense and sparse vegetation
dense_avg, sparse_avg = calculate_average_ndvi(ndvi, sparse_threshold_low, sparse_threshold_high)

# Print the results
print("Average NDVI for sparse vegetation:", sparse_avg)

# Calculate the average NDVI for dense vegetation
dense_avg, _ = calculate_average_ndvi(ndvi, dense_threshold_low, dense_threshold_high)

# Print the result
print("Average NDVI for dense vegetation:", dense_avg)

# Create a mask for the whole vegetation
whole_mask = (ndvi >= sparse_threshold_low) & (ndvi <= dense_threshold_high)

# Calculate the average NDVI for the whole vegetation within the specified range
whole_avg = np.nanmean(ndvi[whole_mask])

# Print the result
print("Average NDVI for the whole vegetation:", whole_avg)