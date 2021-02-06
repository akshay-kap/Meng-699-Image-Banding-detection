# -*- coding: utf-8 -*-
"""

@author: Akshay Kapoor
"""
# Importing relevant Libraries
# Tensorflow  GPU version 2.1.0 is used to train the classifier.
import tensorflow as tf 
import tensorflow.compat.v1 as tf
from tf.keras.preprocessing.image import ImageDataGenerator


# executing the main function
if __name__ == "__main__":
    
    # loading the training dataset on tensorflow's ImageDataGenerator
    # training directory should have respective images in folders of each category
    TRAINING_DIR = "./training/"
    train_datagen = ImageDataGenerator( rescale = 1.0/255.)
    train_generator = train_datagen.flow_from_directory(TRAINING_DIR,
                                                        batch_size=512,
                                                        class_mode='binary')
    
    # loading the validation dataset on tensorflow's ImageDataGenerator
    # validation directory should have respective images in folders of each category
    validation ="./validation/"
    val_datagen = ImageDataGenerator( rescale = 1.0/255.)
    val_generator = val_datagen.flow_from_directory(validation, batch_size=512,
                                                        class_mode='binary')
    
    # loading the testing dataset on tensorflows ImageDataGenerator
    # testing directory should have respective images in folders of each category
    TESTING_DIR = "./testing/"
    test_datagen = ImageDataGenerator( rescale = 1.0/255.)
    test_generator = test_datagen.flow_from_directory(TESTING_DIR,
                                                        class_mode='binary')
    # Training the CNN classifier model
    # Model uses a combination of Covolution layer,Max pooling layer,
    # BatchNormalization layer followed by Gloabal Avg pooling and Dense layers
    # Activation function used all layer except the final layers is Rectified Linear Unit, and 
    # Activation function used for final layer is sigmoid function
    
    CNN_model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(8,(5,5), activation = "relu",  input_shape=(235, 235, 3)),
        tf.keras.layers.MaxPool2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(8,(5,5), activation = "relu"),
        tf.keras.layers.MaxPool2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(16,(3,3), activation = "relu"),
        tf.keras.layers.MaxPool2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(16,(3,3), activation = "relu"),
        tf.keras.layers.MaxPool2D((3,3)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(32,(1,1), activation = "relu"),
        tf.keras.layers.MaxPool2D((3,3)),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')  
    ])
    
    ## Compiling the CNN_model
    
    # Optimizer used: Adam (Adaptive momentum optimizer)
    # loss: Binary cross entropy
    # metric to optimize: Accuracy
    CNN_model.compile(optimizer=Adam(),loss='binary_crossentropy', metrics=['acc'])
    
    # Callbacks to store weights while monitoring validation loss
    model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
                               filepath="/checkpoint_path/",
                               save_weights_only=True,
                               monitor='val_acc',
                               save_best_only= False)

    
    # Fitting the CNN model on training data and validating it on validation data
    history = CNN_model.fit_generator(train_generator,
                              epochs=25,validation_data=val_generator,
                              verbose=1, callbacks = [model_checkpoint_callback])
    
    # Saving the model
    CNN_model.save('model_CNN_classifier')
    

    
