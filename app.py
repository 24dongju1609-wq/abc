import streamlit as st

# 제목
st.title('베이킹 하기')

# 음식 선택
food_type = st.selectbox('만들고 싶은 음식을 고르세요:', ['쿠키', '빵'])

# 재료 리스트 (쿠키와 빵 모두에 대한 재료 추가)
if food_type == '쿠키':
    st.subheader('쿠키 재료')
    ingredients = ['밀가루', '버터', '설탕', '계란', '바닐라 추출물', '토마토', '양배추']
    selected_ingredients = [st.checkbox(ingredient) for ingredient in ingredients]

    # 기본 재료가 모두 선택된 경우
    if all(selected_ingredients[:5]):  # 처음 5개 재료가 모두 선택된 경우
        # 추가 재료가 선택된 경우
        if any(selected_ingredients[5:]):  # 토마토나 양배추가 선택된 경우
            st.error('토마토나 양배추는 쿠키에 들어갈 수 없습니다! 쿠키를 만들 수 없습니다.')
        else:
            st.success('쿠키가 완성되었습니다! 맛있게 드세요!')
    else:
        st.warning('쿠키를 만들려면 밀가루, 버터, 설탕, 계란, 바닐라 추출물을 모두 선택해주세요.')

elif food_type == '빵':
    st.subheader('빵 재료')
    ingredients = ['밀가루', '효모', '설탕', '소금', '따뜻한 물', '토마토', '양배추']
    selected_ingredients = [st.checkbox(ingredient) for ingredient in ingredients]

    # 기본 재료가 모두 선택된 경우
    if all(selected_ingredients[:5]):  # 처음 5개 재료가 모두 선택된 경우
        # 추가 재료가 선택된 경우
        if any(selected_ingredients[5:]):  # 토마토나 양배추가 선택된 경우
            st.error('토마토나 양배추는 빵에 들어갈 수 없습니다! 빵을 만들 수 없습니다.')
        else:
            st.success('빵이 완성되었습니다! 맛있게 드세요!')
    else:
        st.warning('빵을 만들려면 밀가루, 효모, 설탕, 소금, 따뜻한 물을 모두 선택해주세요.')

# 사용자가 선택한 재료 리스트 출력
st.write("선택한 재료:")
for ingredient, selected in zip(ingredients, selected_ingredients):
    if selected:
        st.write(f"- {ingredient}")


