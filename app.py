import streamlit as st
import math

st.set_page_config(page_title="폐의약품 처리 안내", layout="centered")

# -----------------------
# 1. 약물 DB
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

# -----------------------
# 2. 처리 방법
# -----------------------
disposal = {
    "정제": "포장(PTP) 제거 후 밀봉 → 폐의약품 수거함 배출",
    "액체": "휴지 등에 흡수 → 밀봉 후 배출",
    "연고": "용기 그대로 밀봉 → 수거함 배출"
}

# -----------------------
# 3. 서산시 수거 기관 DB
# -----------------------
bins = [
    {"name": "서산시 보건소", "type": "보건소", "lat": 36.7833, "lon": 126.4522},
    {"name": "석남동 행정복지센터", "type": "행정센터", "lat": 36.7845, "lon": 126.4555},
    {"name": "동문1동 행정복지센터", "type": "행정센터", "lat": 36.7801, "lon": 126.4540},
    {"name": "중앙약국", "type": "약국", "lat": 36.7820, "lon": 126.4530},
    {"name": "서산약국", "type": "약국", "lat": 36.7810, "lon": 126.4520}
]

# -----------------------
# 4. 거리 계산
# -----------------------
def distance(a, b, c, d):
    return ((a-c)**2 + (b-d)**2)**0.5

def sort_bins(user_lat, user_lon):
    return sorted(bins, key=lambda x: distance(user_lat, user_lon, x["lat"], x["lon"]))

# -----------------------
# 5. UI
# -----------------------
st.title("폐의약품 처리 안내")

drug = st.text_input("약 이름 입력")

user_lat = st.number_input("위도", value=36.7833)
user_lon = st.number_input("경도", value=126.4522)

# -----------------------
# 6. 결과
# -----------------------
if drug:
    st.divider()

    if drug in drug_db:
        category = drug_db[drug]
        st.subheader("처리 방법")
        st.write(f"분류: {category}")
        st.write(disposal[category])
    else:
        st.warning("DB에 없는 약입니다. (직접 추가 가능)")

    st.subheader("서산시 폐의약품 수거 기관")

    sorted_list = sort_bins(user_lat, user_lon)

    for b in sorted_list:
        dist = distance(user_lat, user_lon, b["lat"], b["lon"])
        st.write(f"{b['name']} ({b['type']}) - 거리: {round(dist,3)}")
