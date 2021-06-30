import re
import string
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

filepath = ''
link = ''
def st_func():
    with open(filepath, 'r') as f:
        speech = f.read()
        #Regular expression to find words in blog post.
        words = [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in speech.split()]
        speech_words = [word if word.isupper() else word.casefold() for word in words]
        speech_words = ' '.join(speech_words)
        fig, ax = plt.subplots()
        wordcloud = WordCloud().generate(speech_words)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.header(f'Wordcloud of President {option}\'s inaugural speech, {date}')
        st.write(f'[SOURCE]({link})')
        st.pyplot(fig)

st.title('Wordcloud of the first term inaugural speech of every elected Nigerian \
president since 1999')

option = st.sidebar.selectbox('Select President',
             ('Olusegun Obasanjo', 'Umaru Yaradua', 'Goodluck Jonathan', 'Muhammadu Buhari'))
if option == 'Olusegun Obasanjo':
    filepath = 'speech_obasanjo.txt'
    date = '29th May, 1999.'
    link = 'http://news.bbc.co.uk/2/hi/world/monitoring/356065.stm'
    st_func()
elif option == 'Umaru Yaradua':
    filepath = 'speech_yaradua.txt'
    date = '29th May, 2007.'
    link = 'https://nairametrics.com/wp-content/uploads/2012/01/Inaugural-Address-of-Umaru-Musa-Yar.pdf'
    st_func()
elif option == 'Goodluck Jonathan':
    filepath = 'speech_goodluck.txt'
    date = '29th May, 2011.'
    link = 'https://www.vanguardngr.com/2011/05/over-40-heads-of-state-witness-jonathans-inauguration-amid-tight-security/'
    st_func()
elif option == 'Muhammadu Buhari':
    filepath = 'speech_buhari.txt'
    date = '29th May, 2015.'
    link = 'https://guardian.ng/features/president-muhammadu-buharis-inaugural-speech/'
    st_func()
