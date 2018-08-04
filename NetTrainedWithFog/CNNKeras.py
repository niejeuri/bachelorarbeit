import tensorflow as tf
from tensorflow.python.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Activation, Dropout
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.losses import categorical_crossentropy
from tensorflow.python.keras.callbacks import Callback

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator

from tensorflow.python.keras import backend as k

image_width = 100
image_height = 60
colour_channels = 3

#input_shape = (image_width, image_height, colour_channels)
batch_size = 15
number_of_epochs = 40
number_of_classes = 2

train_data_directory = 'data/train'
validation_data_directory = 'data/validation'

number_of_training_images = 2400
number_of_validation_images = 80

if k.image_data_format() == 'channels_first':
    input_shape = (3, image_width, image_height)
else:
    input_shape = (image_width, image_height, 3)





def create_cnn_model():
    cnn_model = Sequential()
    cnn_model.add(Conv2D(32, (5, 5), activation='relu', input_shape=input_shape))
    cnn_model.add(MaxPooling2D(pool_size=(2,2)))
    cnn_model.add(Conv2D(64, (5,5), activation='relu'))
    cnn_model.add(MaxPooling2D(pool_size=(2,2)))
    cnn_model.add(Flatten())
    cnn_model.add(Dense(64, activation='relu'))
    cnn_model.add(Dropout(0.5))
    cnn_model.add(Dense(1))
    cnn_model.add(Activation('sigmoid'))
    return cnn_model

model = create_cnn_model()
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

train_datagenerator = ImageDataGenerator(rescale=1./255)
train_generator = train_datagenerator.flow_from_directory('data/train', target_size=(image_width, image_height), batch_size=batch_size, class_mode='binary')

validation_datagenerator = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagenerator.flow_from_directory('data/validation', target_size=(image_width, image_height), batch_size=batch_size, class_mode='binary')

model.fit_generator( train_generator, steps_per_epoch=number_of_training_images // batch_size, epochs=number_of_epochs, validation_data=validation_generator, validation_steps=number_of_validation_images // batch_size)

model.save_weights('weight_01.h5')

#model.compile(loss=categorical_crossentropy, optimizer=Adam(), metrics=['accuracy'])
#model.fit(streets, nostreets, batch_size=batch_size, epochs=number_of_epochs, verbose=1, validation_data=(streets_te, nostreets_te), callbacks=[history])
#score = model.evaluate(streets_te, nostreets_te, verbose=0)
#print('Test loss:', score[0])
#print('Test accuracy:', score[1])
