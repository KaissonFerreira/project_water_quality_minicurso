FROM python

VOLUME [ "/data","imagens" ]

WORKDIR /water_quality

RUN ["stramlit run ./app.py"]
