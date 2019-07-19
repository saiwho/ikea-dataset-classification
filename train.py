# Importing libraries
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense, Conv2D
from keras.layers import Activation, BatchNormalization, MaxPooling2D

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from keras.models import load_model

np.random.seed(8)

# Constants and Hyperparameters.
img_width, img_height = 128, 128
train_data_dir = 'data/train'
validation_data_dir = 'data/valid'
nb_train_samples = 1600
nb_validation_samples = 400
epochs = 5
batch_size = 32
chanDim = -1
input_shape = (img_width, img_height, 3)
classes = 4


# Convolutional model
# CONV -> RELU -> POOL
model = Sequential()
model.add(Conv2D(32, (3, 3), padding="same",input_shape=input_shape))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# CONV -> RELU -> POOL 
model.add(Conv2D(32, (3, 3), padding="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# FC -> RELU 
model.add(Flatten())
model.add(Dense(512))
model.add(Activation("relu"))
model.add(Dropout(0.5))

# Softmax
model.add(Dense(classes))
model.add(Activation("softmax"))

# Compiling the model with Adam optimizer
model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.Adam(lr=1e-3, beta_1=0.9, beta_2=0.999, epsilon=1e-15, decay=0.0),metrics=['accuracy'])

# Data Augmentation only used for rescaling planned to use for zoom and flipping for increasing data set
train_datagen = ImageDataGenerator(
    rescale=1. / 255)
    # ,zoom_range=0.2,
    # horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(128, 128),
    batch_size=batch_size,
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(128, 128),
    batch_size=batch_size,
    class_mode='categorical')

# Fine-tuning the model
H = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples//batch_size,
    epochs=epochs,
    verbose = 2,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples//batch_size,
    shuffle = True)

# print(validation_generator.class_indices)

# Saving the model
model.save('5epochs.h5')

from keras import backend as K
K.clear_session()

# Plotting results
N = np.arange(0, epochs)
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, H.history["acc"], label="train_acc")
plt.plot(N, H.history["val_acc"], label="val_acc")
plt.plot()
plt.title("Training, Valid Accuracy & Loss")
plt.xlabel("#Epoch")
plt.ylabel("Accuracy & Loss")
plt.legend()
plt.show()