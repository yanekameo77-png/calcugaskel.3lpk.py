import streamlit as st
import numpy as np
import pandas as pd

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Gas Ideal",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Kalkulator Gas Ideal")
st.caption("Hukum Gas + Studi Kasus + Regresi Linear (Full Streamlit)")

st.markdown("---")

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.selectbox(
    "📌 Pilih Menu",
    ["Home", "Studi Kasus", "Hukum Boyle", "Hukum Charles", "Hukum Gay-Lussac", "Gas Ideal", "Regresi Linear"]
)

# =========================
# HOME
# =========================
if menu == "Home":

    st.subheader("👋 Selamat Datang")

    st.success("Aplikasi ini dibuat full Streamlit tanpa library error 🚀")

    st.markdown("""
    ### 🔬 Fitur:
    - Hukum Boyle
    - Hukum Charles
    - Hukum Gay-Lussac
    - Gas Ideal (PV = nRT)
    - 📈 Regresi Linear (LINE CHART)
    """)

    st.balloons()

# =========================
# STUDI KASUS
# =========================
elif menu == "Studi Kasus":

    st.subheader("🧪 Studi Kasus Gas Ideal")

    P = st.number_input("Tekanan (atm)", value=1.0)
    V = st.number_input("Volume (L)", value=10.0)
    n = st.number_input("Mol gas", value=1.0)
    T = st.number_input("Suhu (K)", value=300.0)

    R = 0.0821

    if st.button("Analisis"):

        PV = P * V
        nRT = n * R * T

        st.write(f"PV = {PV:.3f}")
        st.write(f"nRT = {nRT:.3f}")

        if abs(PV - nRT) < 1:
            st.success("Sistem sesuai Gas Ideal ✅")
        else:
            st.warning("Ada deviasi dari gas ideal ⚠️")

# =========================
# BOYLE
# =========================
elif menu == "Hukum Boyle":

    st.subheader("📘 Hukum Boyle")

    st.latex(r"P_1V_1=P_2V_2")

    P1 = st.number_input("P1", value=1.0)
    V1 = st.number_input("V1", value=1.0)
    P2 = st.number_input("P2", value=2.0)

    if st.button("Hitung V2"):
        if P2 != 0:
            V2 = (P1 * V1) / P2
            st.success(f"V2 = {V2:.3f} L")

# =========================
# CHARLES
# =========================
elif menu == "Hukum Charles":

    st.subheader("📘 Hukum Charles")

    st.latex(r"\frac{V_1}{T_1}=\frac{V_2}{T_2}")

    V1 = st.number_input("V1", value=1.0)
    T1 = st.number_input("T1 (K)", value=273.0)
    T2 = st.number_input("T2 (K)", value=300.0)

    if st.button("Hitung V2"):
        V2 = (V1 * T2) / T1
        st.success(f"V2 = {V2:.3f} L")

# =========================
# GAY LUSSAC
# =========================
elif menu == "Hukum Gay-Lussac":

    st.subheader("📘 Hukum Gay-Lussac")

    st.latex(r"\frac{P_1}{T_1}=\frac{P_2}{T_2}")

    P1 = st.number_input("P1", value=1.0)
    T1 = st.number_input("T1 (K)", value=273.0)
    T2 = st.number_input("T2 (K)", value=300.0)

    if st.button("Hitung P2"):
        P2 = (P1 * T2) / T1
        st.success(f"P2 = {P2:.3f} atm")

# =========================
# GAS IDEAL
# =========================
elif menu == "Gas Ideal":

    st.subheader("📘 Persamaan Gas Ideal")

    st.latex(r"PV=nRT")

    P = st.number_input("P (atm)", value=1.0)
    V = st.number_input("V (L)", value=1.0)
    n = st.number_input("n (mol)", value=1.0)

    R = 0.0821

    if st.button("Hitung T"):
        T = (P * V) / (n * R)
        st.success(f"Suhu = {T:.2f} K")

# =========================
# REGRESI LINEAR (LINE CHART)
# =========================
elif menu == "Regresi Linear":

    st.subheader("📈 Regresi Linear (LINE CHART Streamlit)")

    x_input = st.text_input("Data P (pisahkan koma)", "1,2,3,4,5")
    y_input = st.text_input("Data V (pisahkan koma)", "10,8,6,4,2")

    if st.button("Hitung & Grafik"):

        # convert data
        x = np.array([float(i) for i in x_input.split(",")])
        y = np.array([float(i) for i in y_input.split(",")])

        # regresi linear
        m, b = np.polyfit(x, y, 1)
        y_pred = m * x + b

        st.success(f"Persamaan: V = {m:.3f}P + {b:.3f}")

        # =========================
        # DATAFRAME
        # =========================
        df = pd.DataFrame({
            "P": x,
            "V (data asli)": y,
            "V (regresi)": y_pred
        })

        # urutkan biar grafik rapi
        df = df.sort_values("P")

        # =========================
        # 📈 LINE CHART (STREAMLIT NATIF)
        # =========================
        st.line_chart(df.set_index("P"))

        st.dataframe(df)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("🚀 Full Streamlit Version | Tanpa Matplotlib | Aman dijalankan")
