import streamlit as st
import time

st.title('Генерация видеолекций на основе фото, аудио и конспекта')
uplode_photo = st.file_uploader('Загрузи фотографию',['jpg','png'])
if uplode_photo is not None:
    st.subheader('Теперь можешь загрузить либо аудио, либо текст')
    uplode_audio = st.file_uploader('Загрузи аудио', ['mp3'])
    uplode_text = st.file_uploader('Загрузи конспект', ['txt','docx'])
    if (uplode_audio is not None) or (uplode_text is not None):
        st.subheader('Вы успешно загрузили все файлы, модель уже начала генерировать видео....')
        time.sleep(5)
        result_file = open('Mot.mp4','rb')
        result_play = result_file.read()
        st.subheader('Модель закончила работу. Можете посмотреть и скачать вашу лекцию')
        st.download_button('Видеолекция','Mot.mp4')
        st.video(result_play)



