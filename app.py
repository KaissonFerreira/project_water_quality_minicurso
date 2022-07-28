import joblib
import os
import pathlib
import streamlit as st



# Diretórios
PACKAGE_ROOT = pathlib.Path('.').resolve()
MODEL_DIR = os.path.join(PACKAGE_ROOT, 'model')
FILE_MODEL_RF = os.path.join(MODEL_DIR,'clf_randomforest.joblib')
FILE_MODEL_LR = os.path.join(MODEL_DIR,'clf_logisticregression.joblib')


# Carregando o modelo
model_rf = joblib.load(FILE_MODEL_RF)
model_lr = joblib.load(FILE_MODEL_LR)


st.set_page_config(
    page_title="Kaisson Ferreira", page_icon=":round_pushpin:", initial_sidebar_state="expanded"
                )

st.title('APP - Modelo de classificação')


st.write("""
# :bar_chart: Projeto de Data Science

Predição da qualidade da água

""")

