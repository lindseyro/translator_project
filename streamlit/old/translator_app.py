import streamlit as st
import numpy as np
from PIL import Image
import tensorflow
import time
from tempfile import NamedTemporaryFile
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import MobileNetV2, VGG16, InceptionV3, Xception

#load model
# pt_model = tensorflow.keras.models.load_model('pre_trained.h5')
model = tensorflow.keras.models.load_model('model.h5')

pre_trained_model = Xception(
    include_top=False,
    weights='imagenet',
    input_shape=(150, 150, 3))

#App title
st.title("Translator")
st.text("Upload an image and see the translation to many different languages!")

#Get image from User
user_file = st.file_uploader(label = 'Image',
    type = ['jpg', 'jpeg', 'png'])



#display image and convert for model
if user_file != None:
    # st.text(f'File Type:{(user_file)}')
    st.text('Image')
    im = Image.open(user_file)
    st.image(im)
    # st.text(f'Image Type:{type(im)}')

    imar = image.img_to_array(im)/255.
    imar.resize(150, 150, 3)
    imar = np.expand_dims(imar, axis=0)
    # st.text(f'Shape:{imar.shape}')

#predict
try:
    pt_pred = pre_trained_model.predict(imar)
    pred = np.argmax(model.predict(pt_pred), axis = 1)
except:
    st.subheader("Waiting...")
    st.stop()

#return prediction
st.text(pred)
# st.subheader(f'Prediction: {pred}')
