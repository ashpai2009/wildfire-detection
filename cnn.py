# Importing all the images from directory structure in the project home directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=.2, vertical_flip=True, horizontal_flip=True, zoom_range=.2)
train = train_datagen.flow_from_directory(directory='data/train', target_size=(128, 128), class_mode='binary')

test_datagen = ImageDataGenerator(rescale=1./255)
test = test_datagen.flow_from_directory(directory='data/test', target_size=(128, 128), class_mode='binary')

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten

# Initializing the CNN
cnn = Sequential()

# Making CNN architecture
cnn.add(Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[128, 128, 3]))
cnn.add(MaxPool2D(pool_size=2))

cnn.add(Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(MaxPool2D(pool_size=2))

cnn.add(Flatten())

# The flattened output from the CNN will now be inputted into an ANN
# Making the ANN portion of the architecture
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=1, activation='sigmoid'))

# Compiling full neural network
cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Fitting the CNN onto training dataset and validating it with test dataset. Training for 100 epochs.
cnn.fit(x=train, validation_data=test, epochs=50, batch_size=32)

# Saving the model
cnn.save('model', save_format='tf')