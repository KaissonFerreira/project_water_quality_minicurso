import joblib
import os
import pathlib




# Diretórios
PACKAGE_ROOT = pathlib.Path('.').resolve()
MODEL_DIR = os.path.join(PACKAGE_ROOT, 'model')
FILE_MODEL = os.path.join(MODEL_DIR,'clf_randomforest.joblib')


# Carregando o modelo
model = joblib.load(FILE_MODEL)
print(model.classes_)