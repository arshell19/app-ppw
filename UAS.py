import pandas as pd
import numpy as np
import streamlit as st 
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime
import warnings
import nltk
import requests
import time
from generate_label import get_label 

import re 
import csv

nltk.download('stopwords')
nltk.download('punkt')
warnings.filterwarnings('ignore')

st.markdown("<h3 style='text-align: center;'>Aplikasi Klasifikasi Berita</h3>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Arshelia Romadhona | 200411100053</h6>", unsafe_allow_html=True)
dataset, preprocessing, modelling, implementasi = st.tabs(["Dataset", "Pre-processing", "Modelling", "Implementasi"])

with dataset:
    dataset = pd.read_csv("https://raw.githubusercontent.com/arshell19/app-ppw/main/Kompas.csv")
    st.dataframe(dataset)
    st.info(f"Banyak Dataset : {len(dataset)}")

with preprocessing:
    dataset = pd.read_csv("https://raw.githubusercontent.com/arshell19/app-ppw/main/HasilTokenizeSummary.csv")
    st.dataframe(dataset)
    st.info(f"Banyak Dataset : {len(dataset)}")

with modelling :
    csv_path = 'https://raw.githubusercontent.com/arshell19/app-ppw/main/hasil.csv'
    df = pd.read_csv(csv_path)
    df


with implementasi:
    news_text = st.text_area(
        "Masukkan Isi Berita", key="input_text", height=250)

    if st.button("Cari Kategori"):
        if news_text:
            text = get_label(news_text)
            with st.expander('Tampilkan Hasil'):
                st.write('Berita yang anda masukkan termasuk dalam kategori: ')
                if text == "Health":
                    st.info(text)
                    url = "https://health.kompas.com/"
                    st.write(
                        'Baca Selanjutnya(%s)'  %url)
                elif text == "Bola":
                    st.info(text)
                    url = "https://bola.kompas.com/"
                    st.write(
                        'Baca Selanjutnya(%s)'  %url)
                elif text == "Tekno":
                    st.info(text)
                    url = "https://tekno.kompas.com/"
                    st.write(
                        'Baca Selanjutnya(%s)'  %url)
               
        else:
            time.sleep(.5)
            st.toast('Masukkan teks terlebih dahulu')


    if __name__ == "__uas__":
        UAS() 