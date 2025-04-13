# Import statements
import os
import keras
import matplotlib.pyplot as plt
import numpy as np

# Clean up the data

# Set the number to skipped
num_skipped = 0
# Iterating through the different folder names
for folder_name in ("glioma", "meningioma", "notumor", "pituitary"):
    # Joining the paths for each folder 
    folder_path = os.path.join("/Users/alishuf/Downloads/brain-tumor-mri-dataset/Training", folder_name)
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        try:
            fobj = open(fpath, "rb")
            is_jfif = b"JFIF" in fobj.peek(10)
        finally:
            fobj.close()
        # Deleting the file if its not cleaned
        if not is_jfif:
            num_skipped += 1
            # Delete corrupted image
            os.remove(fpath)

print(f"Deleted {num_skipped} images.")

image_size = (180, 180) # Setting a consistent image size
batch_size = 128 # How many training examples used in one iterations of training

train_ds, val_ds = keras.utils.image_dataset_from_directory(
    "/Users/alishuf/Downloads/brain-tumor-mri-dataset/Training",
    validation_split=0.2,
    subset="both",
    seed=1337, # Randomizing the data
    image_size=image_size,
    batch_size=batch_size,
)

# Setting the display size for each of the pictures
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9): # Setting the range of images to displat
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(np.array(images[i]).astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")