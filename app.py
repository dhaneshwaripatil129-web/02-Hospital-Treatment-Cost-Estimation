import streamlit as st
import numpy as np
import pandas as pd
import pickle

import streamlit as st
import pandas as pd
import pickle


st.header("🏥 Hospital Treatment Cost Estimation")
#st.subheader("Hello Dhaneshwari 👋")

pipe = pickle.load(open("pipe.pkl","rb"))

st.sidebar.header("Enter Patient Details")

region = st.sidebar.selectbox("Region",["northeast","northwest","southeast","southwest"])
age = st.sidebar.number_input("Age",18,100)
gender = st.sidebar.selectbox("Gender",["Female","Male"])
bmi = st.sidebar.number_input("BMI",10.0,60.0)
children = st.sidebar.number_input("Children",0,10)
smoker = st.sidebar.selectbox("Smoker",["No","Yes"])

# Encoding
gender = 1 if gender=="Male" else 0
smoker = 1 if smoker=="Yes" else 0

region_northeast = 1 if region=="northeast" else 0
region_northwest = 1 if region=="northwest" else 0
region_southeast = 1 if region=="southeast" else 0
region_southwest = 1 if region=="southwest" else 0

if st.sidebar.button("Predict Cost"):
    st.subheader("📋 Patient Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**👤 Age:** {age}")
        st.write(f"**⚧ Gender:** {gender}")
        st.write(f"**⚖️ BMI:** {bmi}")

    with col2:
        st.write(f"**🌍 Region:** {region}")
        st.write(f"**👨‍👩‍👧 Children:** {children}")
        st.write(f"**🚬 Smoker:** {smoker}")

    st.markdown("---")
    myinput = [[
        region_northeast,
        region_northwest,
        region_southeast,
        region_southwest,
        age,
        gender,
        bmi,
        children,
        smoker
    ]]

    columns = [
        'region_northeast',
        'region_northwest',
        'region_southeast',
        'region_southwest',
        'age',
        'gender',
        'bmi',
        'children',
        'smoker'
    ]


    myinput = pd.DataFrame(myinput, columns=columns)

    result = pipe.predict(myinput)

    
    st.success(f"💰 Estimated Treatment Cost: ₹ {round(result[0], 2)}")
   