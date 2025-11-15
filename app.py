import streamlit as st


st.title('나의 첫 번째 Streamlit 앱')


st.write("Streamlit을 사용하여 간단한 웹 앱을 만들었습니다!")


if st.button('클릭'):
    st.write("버튼이 클릭되었습니다!")
else:
    st.write("버튼을 클릭하세요.")
