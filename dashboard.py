import streamlit as st 
import stocktwits_dash 

# Adding a sidebar
st.sidebar.title('options')

# Adding selection to sidebar
dash_select = st.sidebar.selectionbox('Which Dashboard?' , ('twitter' , 'wallstreetbets' , 'stockwits' , 'chart' , 'reddit' , 'stock portfolio' , 'stock prediction'), 2)

 st.markdown(f"<h1 style='text-align: centre;'>{dash_select.upper()}</h1>", unsafe_allow_html=True)

if dash_select == 'stocktwits':
    st.markdown(f"<h4 style='text-align: centre;'>(Stocktwits is like twitter for tradrers & investors)</h4>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: centre;'>Pulls the feed that mentions a particular stock</h2>", unsafe_allow_html=True)
    stocktwits_dash.load_stocktwits_dash()
