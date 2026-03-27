import streamlit as st
import pandas as pd

st.set_page_config(page_title="폐의약품 처리 안내", layout="centered")

# -----------------------
# 스타일
# -----------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
h1 {
    text-align: center;
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)

st.title("💊 폐의약품 처리 안내 시스템")
st.caption("서산시 폐의약품 배출을 쉽게 안내합니다")

# -----------------------
# 약물 DB
# -----------------------
drug_db = {
    "타이레놀": "정제",
    "부루펜": "정제",
    "아세트아미노펜": "정제",
    "기침시럽": "액체",
    "시럽": "액체",
    "안연고": "연고",
    "피부연고": "연고"
}

disposal = {
    "정제": "포장 제거 후 밀봉하여 폐의약품 수거함 배출",
    "액체": "휴지 등에 흡수 후 밀봉하여 배출",
    "연고": "용기째 밀봉하여 배출"
}

# -----------------------
# 서산시 수거 기관
# -----------------------
bins = [
    {"name": "서산시 보건소", "type": "보건소", "lat": 36.7833, "lon": 126.4522},
    {"name": "석남동 행정복지센터", "type": "행정센터", "lat": 36.7845, "lon": 126.4555},
    {"name": "동문1동 행정복지센터", "type": "행정센터", "lat": 36.7801, "lon": 126.4540},
    {"name": "중앙약국", "type": "약국", "lat": 36.7820, "lon": 126.4530},
    {"name": "서산약국", "type": "약국", "lat": 36.7810, "lon": 126.4520}
]

# -----------------------
# 입력
# -----------------------
drug = st.text_input("💊 약 이름 입력")

# -----------------------
# 결과
# -----------------------
if drug:
    st.divider()

    if drug in drug_db:
        category = drug_db[drug]
        st.markdown("### 📌 처리 방법")
        st.info(f"**분류:** {category}\n\n**방법:** {disposal[category]}")
    else:
        st.warning("DB에 없는 약입니다")

    st.markdown("### 📍 수거 기관 위치")

    # DataFrame 변환 (지도용)
    df = pd.DataFrame(bins)

    # 지도 출력
    st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))

    # 리스트 출력
    st.markdown("### 📋 수거 기관 목록")
    for b in bins:
        st.success(f"{b['name']} ({b['type']})")
