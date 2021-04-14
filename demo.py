import streamlit as st
import pandas as pd 
import numpy as np

st.title("THIS IS A TITLE")

st.header("THIS IS A HEADER")

st.subheader("THIS IS A SUBHEADER")

st.write("THIS IS SIMPLE PLAIN TEXT")


'''
# MARKDOWN H1
### MAKDOWN H3
1. Test
2. Test 2
'''

st.subheader("you can define dictonaires & lists:")
some_dict = {
    'key1' : 'value',
    'key2' : 'value2'
}
some_list = [1,2,3]
st.write(some_dict)
st.write(some_list)

# Adding a sidebar
st.sidebar.write('Write this to the sidebar')

# Adding selection to sidebar
dash_select = st.sidebar.selectionbox('Which Dashboard?' , ('twitter' , 'wallstreetbets' , 'stockwits' , 'chart' , 'pattern'))
st.sidebar.write('you selected:' , dash_select)

# Displaying a dataframe
st.subheader('Displaying a dataframe:')
df = pd.DataFrame(np.random.randn(50, 20),colums=('col %d' % i for i in range(20)))
st.dataframe(df)

# Display an image (URL or Path)
st.subheader('Displaying a Image (via URL:')
st.image('https://hatrabbits.com/wp-content/uploads/2017/01,random.jpg')


st.write('$123'.isalpha())
st.write('$AMG'.isalpha())
st.write('Joe'.isalpha())
st.write(1+1)
