from PIL import Image
import joblib
import os
import pathlib
import streamlit as st
import numpy as np

# Diretórios
PACKAGE_ROOT = pathlib.Path('.').resolve()
MODEL_DIR = os.path.join(PACKAGE_ROOT, 'model')
FILE_MODEL_RF = os.path.join(MODEL_DIR,'clf_randomforest.joblib')
FILE_MODEL_LR = os.path.join(MODEL_DIR,'clf_logisticregression.joblib')

IMAGE_DIR = os.path.join(PACKAGE_ROOT,'image')
FILE_IMAGE_AGUA = os.path.join(IMAGE_DIR, 'tratamento-agua.jpg')




st.set_page_config(
    page_title="APP model", page_icon=":beginner:", initial_sidebar_state="expanded"
                )



st.title('APP - Modelo de classificação')


st.write("""
# :droplet: :chart_with_upwards_trend: Predição da qualidade da água

Projeto de Data Science para o minicurso da SEQ

""")

classifier_name = st.selectbox("Selecione o classificador:", ("Random Forest","Regressão Logística"))

# Atributos
ph = st.sidebar.slider("PH",0,14)
dureza = st.sidebar.number_input("Dureza:")
solidos = st.sidebar.number_input("TDS - Sólidos dissolvidos totais (mg/L):")
cloramina = st.sidebar.number_input("Cloro (mg/L):")
sulfatos = st.sidebar.number_input("sulfato (mg/L):")
condutividade = st.sidebar.number_input("Condutividade (micro-Siemens/cm):")
toc = st.sidebar.number_input("Carbono orgânico total (mg/L):")
trihalometano = st.sidebar.number_input("Trihalometano (mg/L):")
turbidez = st.sidebar.number_input("Turbidez (NTU):")

lista_atributos = np.array([[ph, dureza, solidos, cloramina, sulfatos, condutividade, toc, trihalometano, turbidez]])
st.button("Refresh")



def get_clf():
    if classifier_name == "Random Forest":
        model = joblib.load(FILE_MODEL_RF)
        predict = model.predict_proba(lista_atributos)
    else:
        model = joblib.load(FILE_MODEL_LR)
        predict = model.predict_proba(lista_atributos)
    return predict

response = get_clf()
text_response = st.write("""
## A probabilidade da água ser potável é de: **{:.2f}%**
""".format(response[0][1]*100))

image = Image.open('images/tratamento-agua.jpg')
st.image(image, caption='Estação de tratamento de água')