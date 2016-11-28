import os, time
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Dropout
import inception_v3 as inception

recv_pipe = "/tmp/gtImageStream.pipe"
send_pipe = "/tmp/gtResultSteam.pipe"

send_port = os.open(send_pipe, os.O_SYNC | os.O_CREAT | os.O_RDWR)
recv_port = None


def predImg(model, file_path, IMSIZE):
    try:
        img = image.load_img(file_path, target_size=IMSIZE)
        ig = image.img_to_array(img)
        ig = np.expand_dims(ig, axis=0)
        ig = inception.preprocess_input(ig)
        preds = model.predict(ig)
        max_pred = preds[0][0]
        max_index = 0
        for i in [1, 2, 3]:
            if preds[0][i] > max_pred:
                max_pred = preds[0][i]
                max_index = i
        mapping = {
            0: 'cross',
            1: 'left',
            2: 'right',
            3: 'straight'
        }
        return mapping.get(max_index, "error")
    except BaseException as err:
        print(err)

if __name__ == '__main__':
    output_file_name = "l_inceptionV3"
    locked_base = True
    dense_count = 0

    print("Compile Model on: " + output_file_name)
    base_model = inception.InceptionV3(weights='imagenet')
    if locked_base:
        print("TrainModel::Lock_Base")
        for layer in base_model.layers:
            layer.trainable = False
    x = base_model.get_layer('flatten').output
    if dense_count > 0:
        print("TrainModel::Append_Layer")
        x = Dense(dense_count, activation='relu')(x)
        x = Dropout(0.5)(x)
    predictions = Dense(4, activation='softmax', name='predictions')(x)
    model = Model(input=base_model.input, output=predictions)
    print("TrainModel::Compile_Model")
    model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
    model.load_weights('road_prediction_' + output_file_name + '.h5')

    print("Model Completed.\n Waiting for inputs...")
    while True:
        if recv_port is None:
            recv_port = os.open(recv_pipe, os.O_RDONLY)
        s = os.read(recv_port, 1024)
        if len(s) == 0:
            time.sleep(0.5)
            continue
        print(s)
        result = result = predImg(model, '/Users/GreysTone/Desktop/Dev/Porus_Server/uploaded/target.jpg', (299, 299))
        os.write(send_port, bytes(result, 'utf-8'))
