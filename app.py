import streamlit as st


st.title('안녕하세요')


st.write("여기에 오신 걸 환영합니다")


if st.button('클릭'):
    st.write("당신은 저에게 치킨을 사주셔야 합니다")
else:
    st.write("버튼을 클릭하세요.")
