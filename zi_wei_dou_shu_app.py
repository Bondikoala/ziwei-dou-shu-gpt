
import streamlit as st
import pandas as pd
import numpy as np

# Define the Zi Wei Dou Shu 12 Palaces
palaces = [
    "Life Palace (命宫)", "Siblings Palace (兄弟宫)", "Spouse Palace (夫妻宫)", "Children Palace (子女宫)",
    "Wealth Palace (财帛宫)", "Health Palace (疾厄宫)", "Travel Palace (迁移宫)", "Friends Palace (交友宫)",
    "Career Palace (事业宫)", "Property Palace (田宅宫)", "Fortune Palace (福德宫)", "Parents Palace (父母宫)"
]

# Define major stars in Zi Wei Dou Shu
major_stars = ["Zi Wei (紫微)", "Tian Ji (天机)", "Tai Yang (太阳)", "Wu Qu (武曲)",
               "Tian Tong (天同)", "Lian Zhen (廉贞)", "Tian Fu (天府)", "Tai Yin (太阴)",
               "Tan Lang (贪狼)", "Ju Men (巨门)", "Tian Xiang (天相)", "Tian Liang (天梁)"]

# Interpretations for each star
interpretations = {
    "Zi Wei (紫微)": "You possess strong leadership qualities and are destined for significant influence.",
    "Tian Ji (天机)": "Your intelligence and strategic thinking set you apart.",
    "Tai Yang (太阳)": "You are energetic and charismatic, often finding success in public-facing roles.",
    "Wu Qu (武曲)": "Wealth is a major theme in your life. With determination and discipline, you can build financial stability.",
    "Tian Tong (天同)": "You enjoy comfort and stability, often favoring a life of harmony.",
    "Lian Zhen (廉贞)": "Your personality is complex, excelling in negotiation and diplomacy.",
    "Tian Fu (天府)": "You have strong financial acumen, leading to wealth accumulation.",
    "Tai Yin (太阴)": "A deep thinker with strong intuition, you thrive in artistic or philosophical pursuits.",
    "Tan Lang (贪狼)": "Charismatic and versatile, you excel in business or entertainment.",
    "Ju Men (巨门)": "Your communication skills make you successful in law, media, or education.",
    "Tian Xiang (天相)": "You are an excellent strategist and planner.",
    "Tian Liang (天梁)": "Strong protective energy, excelling in healthcare or humanitarian efforts."
}

# Function to generate Zi Wei Dou Shu Chart
def generate_zwds_chart(birth_year, birth_month, birth_day, birth_hour):
    np.random.seed(birth_year + birth_month + birth_day + birth_hour)
    star_assignments = np.random.choice(major_stars, size=12, replace=False)
    zwds_chart_df = pd.DataFrame({"Palace": palaces, "Major Star": star_assignments})
    zwds_chart_df["Interpretation"] = zwds_chart_df["Major Star"].map(interpretations)
    return zwds_chart_df

# Function to calculate Ten-Year Luck Cycle
def calculate_ten_year_cycles(life_palace_position):
    return [f"{(i * 10) + 1}-{(i * 10) + 10} years: {palaces[(life_palace_position + i) % 12]}" for i in range(12)]

# Function to calculate Yearly Fortune
def calculate_yearly_fortune(current_year, birth_year, life_palace_position):
    year_diff = current_year - birth_year
    yearly_palace = (life_palace_position + year_diff) % 12
    return f"{current_year}: Influenced by {palaces[yearly_palace]}"

# Streamlit UI
st.title("Zi Wei Dou Shu Fortune Analysis")

birth_year = st.number_input("Enter Birth Year", min_value=1900, max_value=2100, step=1, value=1983)
birth_month = st.number_input("Enter Birth Month", min_value=1, max_value=12, step=1, value=4)
birth_day = st.number_input("Enter Birth Day", min_value=1, max_value=31, step=1, value=10)
birth_hour = st.number_input("Enter Birth Hour", min_value=0, max_value=23, step=1, value=15)

if st.button("Generate Analysis"):
    zwds_chart_df = generate_zwds_chart(birth_year, birth_month, birth_day, birth_hour)
    st.subheader("Zi Wei Dou Shu Natal Chart")
    st.dataframe(zwds_chart_df)

    life_palace_position = 0  # Placeholder, can be dynamically determined later
    ten_year_df = pd.DataFrame({"Ten-Year Cycle": calculate_ten_year_cycles(life_palace_position)})
    st.subheader("Ten-Year Luck Cycle (大限)")
    st.dataframe(ten_year_df)

    current_year = 2025  # Example for current year
    yearly_fortune_df = pd.DataFrame({"Year": [current_year], "Fortune Analysis": [calculate_yearly_fortune(current_year, birth_year, life_palace_position)]})
    st.subheader("Yearly Fortune (流年)")
    st.dataframe(yearly_fortune_df)
