from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from model_def import create_model

train_dir = 'data/train'
val_dir = 'data/test'

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir, target_size=(48, 48), color_mode="grayscale",
    batch_size=64, class_mode='categorical'
)
val_generator = val_datagen.flow_from_directory(
    val_dir, target_size=(48, 48), color_mode="grayscale",
    batch_size=64, class_mode='categorical'
)

model = create_model()
model.compile(loss='categorical_crossentropy', optimizer=Adam(1e-4), metrics=['accuracy'])

model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples//64,
    epochs=75,
    validation_data=val_generator,
    validation_steps=val_generator.samples//64
)

model.save_weights('model.h5')
