import streamlit as st
import pandas as pd
import joblib

#載入模型
model = joblib.load('plating_model.pkl')

# 顯示公司Logo和名稱
st.image('logo.png', width=200)
st.markdown("<h2 style='text-align: center; color: #1E90FF;'>謙集益企業股份有限公司</h2>", unsafe_allow_html=True)
st.title("光亮劑濃度預測與添加量計算")

# 輸入框
st.header("輸入數據")
gloss = st.number_input("檢驗數據", min_value=0.0, max_value=160.0, value=50.0)
target_concentration = st.number_input("目標濃度 (mL/L)", min_value=0.0, max_value=1.0, value=1.0)
tank_volume = st.number_input("槽體積 (L)", min_value=0.0, max_value=100000.0, value=18000.0)


# 預測與計算
if st.button("預測與計算"):
    # 預測當前濃度
    data = pd.DataFrame([[gloss]], columns=['檢驗數據'])
    current_concentration = model.predict(data)[0]
    st.success(f"當前光亮劑濃度: {current_concentration:.2f} mL/L")

    # 計算添加量
    if current_concentration < target_concentration:
        add_amount = (target_concentration - current_concentration) * tank_volume
        st.success(f"需添加光亮劑: {add_amount:.2f} mL")
    else:
        st.info("當前濃度已達或超過目標，無需添加！")

# 說明
st.write("檢驗數據（0-160）、目標濃度、槽體積，點擊預測。")
