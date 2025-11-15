import streamlit as st


st.title('맛있는 음식 만들기 시뮬레이션')

food_type = st.selectbox('만들고 싶은 음식을 고르세요:', ['쿠키', '빵'])

if food_type == '쿠키':
    st.subheader('쿠키 재료')
    ingredients = ['밀가루', '버터', '설탕', '계란', '바닐라 추출물']
    selected_ingredients = [st.checkbox(ingredient) for ingredient in ingredients]

    if all(selected_ingredients):
        st.success('쿠키가 완성되었습니다! 맛있게 드세요!')
    else:
        st.warning('쿠키를 만들려면 모든 재료를 선택해주세요.')

elif food_type == '빵':
    st.subheader('빵 재료')
    ingredients = ['밀가루', '효모', '설탕', '소금', '따뜻한 물']
    selected_ingredients = [st.checkbox(ingredient) for ingredient in ingredients]

    if all(selected_ingredients):
        st.success('빵이 완성되었습니다! 맛있게 드세요!')
    else:
        st.warning('빵을 만들려면 모든 재료를 선택해주세요.')

if food_type == '쿠키':
    st.write("선택한 재료:")
    for ingredient, selected in zip(ingredients, selected_ingredients):
        if selected:
            st.write(f"- {ingredient}")

elif food_type == '빵':
    st.write("선택한 재료:")
    for ingredient, selected in zip(ingredients, selected_ingredients):
        if selected:
            st.write(f"- {ingredient}")

st.title('안녕하세요')


st.write("여기에 오신 걸 환영합니다")


if st.button('클릭'):
    st.write("당신은 저에게 치킨을 사주셔야 합니다")
else:
    st.write("버튼을 클릭하세요.")
