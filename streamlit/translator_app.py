import streamlit as st
import numpy as np
from PIL import Image
import tensorflow
from tempfile import NamedTemporaryFile
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import Xception
from translator import *

#load model
# pt_model = tensorflow.keras.models.load_model('pre_trained.h5')
model = tensorflow.keras.models.load_model('model_612_30.h5')

pre_trained_model = Xception(
    include_top=False,
    weights='imagenet',
    input_shape=(150, 150, 3))

#App title
st.title("Translator")
st.text("Upload an image and see the translation to 107 different languages!")

col1, col2 = st.beta_columns(2)

language = col1.selectbox(
    'Select Your Language',
    ('Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 
    'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 
    'Chinese (simplified)', 'Chinese (traditional)', 'Corsican', 'Croatian', 'Czech', 
    'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 
    'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 
    'Haitian creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 
    'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 
    'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (kurmanji)', 'Kyrgyz', 'Lao', 
    'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay',
     'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (burmese)', 
     'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish', 'Portuguese', 
     'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots gaelic', 'Serbian', 'Sesotho', 
     'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 
     'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 
     'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu'))

#Get image from User
user_file = col2.file_uploader(label = 'Image',
    type = ['jpg', 'jpeg', 'png'])

#display image and convert for model
if user_file != None:
    # st.text(f'File Type:{(user_file)}')
    # st.text('Image')
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

#return translation
word = prediction(pred[0])

st.success(translate_word(word, language))
