# ------------------
# Train a CNN to classify Cats vs Dogs and save the model.

import tensorflow as tf
from tensorflow import keras
from keras import layers

# -----------------------------
# SETTINGS
# -----------------------------
TRAIN_DIR = "train_data_images"   # must contain cats/ and dogs/ folders
IMG_SIZE = (150, 150)
BATCH_SIZE = 32
EPOCHS = 5                    # increase for better accuracy
# -----------------------------

# 1️⃣ Load dataset
train_ds = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

# 2️⃣ Normalize pixel values (0–1)
train_ds = (
    train_ds
    .map(lambda x, y: (x / 255.0, y), num_parallel_calls=tf.data.AUTOTUNE)
    .apply(tf.data.experimental.ignore_errors())
)


# 3️⃣ Build CNN
model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(*IMG_SIZE,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')   # binary output
])

# 4️⃣ Compile model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 5️⃣ Train model
model.fit(train_ds, epochs=EPOCHS)

# 6️⃣ Save model
model.save("cat_dog_model.h5")
print("\n✅ Model trained and saved as cat_dog_model.h5")
