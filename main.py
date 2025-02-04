import streamlit as st
import pickle
from PIL import Image
pickle_in=open("D:\\project1_tv\\banknoteauthentication\\Banknote_Authentication\\classifier.pkl","rb")
classifier=pickle.load(pickle_in)
def predict_note_authentication(variance,skewness,kurtosis,entropy):
    prediction=classifier.predict([[variance,skewness,kurtosis,entropy]])
    print ( prediction)
    return prediction
def main():
    st.title("bank_authentication")
    html_temp="""
    <div style="background_color:tomato;padding:10 px">
    <h2 style="color:white;text-align:centre;">streamlit bank authenticator ML APP</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input(" variance","type_here")
    skewness = st.text_input("skewness", "type_here")
    kurtosis = st.text_input(" kurtosis", "type_here")
    entropy = st.text_input(" entropy", "type_here")
    result="   "
    if st.button("predict"):
        result=predict_note_authentication(variance,skewness,kurtosis,entropy)
        st.success("op".format(result))
    if st.button("about"):
        st.text("lets learn")
if __name__ == '__main__':
    main()