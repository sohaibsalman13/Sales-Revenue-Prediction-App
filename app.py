import streamlit as st
import pandas as pd
import numpy as np
#import pickle
import joblib
import plotly.express as px

st.set_page_config(page_title="Revenue Forecasting", layout="wide")

# Loading models
@st.cache_resource
def load_models():
    return {
        "Revenue per Order Predictor": joblib.load("rf_reg_compressed.pkl"),
        "Revenue per Day Predictor": joblib.load("rf_reg2_compressed.pkl"),
        "Late Delivery Predictor": joblib.load("rf_cl_compressed.pkl")
    }

models = load_models()

#------------------------------------------------------------------------------------#
# App Configuration 

#st.title("📈 E-commerce Forecasting App")
st.markdown("<h1 style='text-align: center;'>📈 E-commerce Forecasting App</h1>", unsafe_allow_html=True)

st.header("Choose Model & Input Features")
model_choice = st.selectbox("Select Model", list(models.keys()))

col1, col2, col3 = st.columns(3)
col4, col5, col6, col7 = st.columns(4)

#------------------------------------------------------------------------------------#
# Input features for model 2
if model_choice == "Revenue per Day Predictor": 
    with col1:
        num_of_items2 = st.number_input("Number of Items per Day", min_value=75, key="num_items2")
    with col2:
        avg_price_per_item2 = st.number_input("Total Average Price per Item per Day", min_value=4000.0, key="avg_price2")
    with col3:
        freight_value2 = np.clip(np.random.normal(loc=2367, scale=500), 1000, 3000)
    with col4:
        purchase_day2 = st.number_input("Purchase Day of the Month", min_value=1, max_value=31, key="day2")
    with col5:
        purchase_month2 = st.number_input("Purchase Month (1=Jan)", min_value=1, max_value=12, key="month2")
    with col6:
        purchase_year2 = st.number_input("Purchase Year", min_value=2016, key="year2")

    input_features = np.array([[
        num_of_items2,
        avg_price_per_item2,
        freight_value2,
        purchase_day2,
        purchase_month2,
        purchase_year2,
        
    ]])


# Input features for model 1
else:
    with col1:
        num_of_items = st.number_input("Number of Items", min_value=1, key="num_items")
    with col2:
        avg_price_per_item = st.number_input("Average Price per Item", min_value=1.0, key="avg_price")
    with col3:
        freight_value = np.clip(np.random.normal(loc=20, scale=15.4), 8, 15)
    with col4:
        purchase_day = st.number_input("Purchase Day of the Month", min_value=1, max_value=31, key="day")
    with col5:
        purchase_month = st.number_input("Purchase Month (1=Jan)", min_value=1, max_value=12, key="month")
    with col6:
        purchase_year = st.number_input("Purchase Year", min_value=2016, key="year")
    with col7:
        is_weekend = st.selectbox("Is it a Weekend?", [0, 1], key="weekend")

    input_features = np.array([[
        num_of_items,
        avg_price_per_item,
        freight_value,
        purchase_day,
        purchase_month,
        purchase_year,
        is_weekend,  
    ]])


#------------------------------------------------------------------------------------#
# Predict 
button_text = {
    "Revenue per Order Predictor": "Revenue per Order Predictor",
    "Revenue per Day Predictor": "Revenue per Day Predictor",
    "Late Delivery Predictor": "Predict Late Delivery"
}


if st.button(button_text[model_choice]):
    model = models[model_choice]
    prediction = model.predict(input_features)[0]

    if model_choice == "Late Delivery Predictor":
        label = "Yes" if prediction == 1 else "No"
        st.metric("Will the order be delivered late?", label)
    else:
        st.metric("Prediction", f"${prediction:,.2f}")



#------------------------------------------------------------------------------------#
# History Graph

st.subheader("📊 Historical Revenue per Day Trend")

df = pd.read_csv("order_df_agg.csv")  
df["purchase_date"] = pd.to_datetime(df["purchase_date"])

# Extract Year-Month format for grouping
df["Month"] = df["purchase_date"].dt.to_period("M").astype(str)

# Group by Month and sum sales
monthly_sales = df.groupby("Month")["final_price_per_order"].sum().reset_index()
monthly_sales.columns = ["Month", "Sales"]

# Sort by Month for proper x-axis
monthly_sales["Month"] = pd.to_datetime(monthly_sales["Month"])
monthly_sales = monthly_sales.sort_values("Month")
monthly_sales["Month_str"] = monthly_sales["Month"].dt.strftime('%b %Y')

# Plot
fig = px.line(monthly_sales, x="Month_str", y="Sales")
fig.update_layout(width=1000, height=400)
st.plotly_chart(fig, use_container_width=False)



st.subheader("📊 Historical Revenue per Order Trend")

df = pd.read_csv("order_df.csv")  
df["purchase_date"] = pd.to_datetime(df["purchase_date"])

# Extract Year-Month format for grouping
df["Month"] = df["purchase_date"].dt.to_period("M").astype(str)

# Group by Month and sum sales
monthly_sales = df.groupby("Month")["final_price_per_order"].sum().reset_index()
monthly_sales.columns = ["Month", "Sales"]

# Sort by Month for proper x-axis
monthly_sales["Month"] = pd.to_datetime(monthly_sales["Month"])
monthly_sales = monthly_sales.sort_values("Month")
monthly_sales["Month_str"] = monthly_sales["Month"].dt.strftime('%b %Y')

# Plot
fig = px.line(monthly_sales, x="Month_str", y="Sales")
fig.update_layout(width=1000, height=400)
st.plotly_chart(fig, use_container_width=False)

#------------------------------------------------------------------------------------#
# Footer 
st.sidebar.subheader('About')
st.sidebar.caption(
    "This app is built on Random Forest Regression and Classification models. " \
    "There are 3 models that predict 'Revenue per single Order', " \
    "'Total Revenue per Day' and 'Late delivery' respectively using a set of input features. " \
    "The models are trained on the real world supermarket data from Brazil (2016-2018). " \
    "Hence the model makes the prediciton using that data with an accuracy of 92%.")
st.sidebar.subheader('Steps:')
st.sidebar.caption("""
1. Choose the model that you want the prediction from.  
2. Input all the required features with relative accuracy.  
3. Use the predict button to get the prediction.
""")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")

st.sidebar.caption("""
                   Built by Sohaib Salman
                   sohaibsalman684@gmail.com""")