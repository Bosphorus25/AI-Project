# sort_cats_dogs.py
# -----------------
# Load trained cat_dog_model.h5 and sort images in mixed folder.

import tensorflow as tf
from tensorflow import keras
import numpy as np
import os, shutil

# -----------------------------
# SETTINGS
# -----------------------------
MODEL_PATH = "cat_dog_model.h5"  # trained model
MIXED_DIR = "test_data_images"       # folder of unsorted images
SORTED_DIR = "sorted"            # output folder
IMG_SIZE = (150, 150)
# -----------------------------

# 1️⃣ Load trained model
model = keras.models.load_model(MODEL_PATH)
print("✅ Model loaded successfully.")

# 2️⃣ Make output folders
os.makedirs(os.path.join(SORTED_DIR, "cats"), exist_ok=True)
os.makedirs(os.path.join(SORTED_DIR, "dogs"), exist_ok=True)

# 3️⃣ Process and sort each image
for filename in os.listdir(MIXED_DIR):
    filepath = os.path.join(MIXED_DIR, filename)
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    # Load and preprocess image
    img = keras.utils.load_img(filepath, target_size=IMG_SIZE)
    img_array = keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict (0 = cat, 1 = dog)
    pred = model.predict(img_array, verbose=0)[0][0]
    label = "dogs" if pred > 0.5 else "cats"

    # Copy file to target folder
    dest = os.path.join(SORTED_DIR, label, filename)
    shutil.copy(filepath, dest)
    print(f"{filename} → {label}")

print("\n✅ Sorting complete! Check 'sorted/cats' and 'sorted/dogs' folders.")
