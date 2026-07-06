import streamlit as st
import pandas as pd
import pickle

# ---------------------- PAGE ----------------------
st.set_page_config(
    page_title="Hospital Cost Estimation",
    page_icon="🏥",
    layout="wide"
)

# ---------------------- LOAD MODEL ----------------------
pipe = pickle.load(open("pipe.pkl","rb"))

# ---------------------- CSS ----------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg, #E0F7FA, #BBDEFB, #E8F5E9);
}

.main-title{
font-size:42px;
font-weight:bold;
text-align:center;
color:#0b7285;
}

.sub{
text-align:center;
color:gray;
font-size:18px;
margin-bottom:25px;
}

[data-testid="stMetric"]{
background:white;
padding:15px;
border-radius:15px;
box-shadow:0px 5px 10px rgba(0,0,0,.12);
}

.stButton>button{
width:100%;
background:#009688;
color:white;
font-size:20px;
border-radius:10px;
height:55px;
border:none;
}

.stButton>button:hover{
background:#00695c;
color:white;
}

.result{
padding:20px;
border-radius:15px;
font-size:24px;
font-weight:bold;
text-align:center;
}

.good{
background:#2ecc71;
color:white;
}

.bad{
background:#e74c3c;
color:white;
}

</style>
""",unsafe_allow_html=True)


# ---------------------- TITLE ----------------------
st.markdown("<div class='main-title'>🏥 Hospital Treatment Cost Estimation</div>",unsafe_allow_html=True)
st.markdown("<div class='sub'>AI Powered Medical Expense Predictor</div>",unsafe_allow_html=True)

# ---------------------- METRICS ----------------------
m1,m2,m3,m4=st.columns(4)
with m1: st.metric("Model","Linear Regression")
with m2: st.metric("Inputs","6")
with m3: st.metric("Prediction","Cost (₹)")
with m4: st.metric("Status","Ready")

st.divider()

# ---------------------- INPUTS ----------------------
left,right=st.columns(2)

with left:
    st.subheader("👤 Patient Information")
    age = st.number_input("Age",18,100)
    gender = st.selectbox("Gender",["Female","Male"])
    children = st.number_input("Children",0,10)

with right:
    st.subheader("🧪 Medical Information")
    bmi = st.number_input("BMI",10.0,60.0)
    smoker = st.selectbox("Smoker",["No","Yes"])
    region = st.selectbox("Region",["northeast","northwest","southeast","southwest"])

st.divider()

# ---------------------- BUTTON ----------------------
if st.button("🔍 Estimate Cost"):

    gender_val = 1 if gender=="Male" else 0
    smoker_val = 1 if smoker=="Yes" else 0
    region_northeast = 1 if region=="northeast" else 0
    region_northwest = 1 if region=="northwest" else 0
    region_southeast = 1 if region=="southeast" else 0
    region_southwest = 1 if region=="southwest" else 0

    myinput = pd.DataFrame([[
        region_northeast,region_northwest,region_southeast,region_southwest,
        age,gender_val,bmi,children,smoker_val
    ]],columns=[
        'region_northeast','region_northwest','region_southeast','region_southwest',
        'age','gender','bmi','children','smoker'
    ])

    result = pipe.predict(myinput)

    st.markdown(f"<div class='result good'>💰 Estimated Treatment Cost: ₹ {round(result[0],2)}</div>", unsafe_allow_html=True)
    st.success("✅ Prediction generated successfully!")
    st.progress(80)

st.divider()
st.caption("Developed with ❤️ Streamlit + Machine Learning")
