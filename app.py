import streamlit as st

# 제목
st.title('나의 첫 번째 Streamlit 앱')

# 텍스트
st.write("Streamlit을 사용하여 간단한 웹 앱을 만들었습니다!")

# 버튼을 추가해서 클릭 시 텍스트 변화
if st.button('클릭'):
    st.write("버튼이 클릭되었습니다!")
else:
    st.write("버튼을 클릭하세요.")
