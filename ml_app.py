import pickle
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv("Final_Project.csv")
    return df

df = load_data()

# Load regression model
with open('regression_model.pkl', 'rb') as file:
    reg = pickle.load(file)

def predict_price(Location, Area_SqFt, Floor_No, Bathroom, Bedroom, Property_Age):
    # Create feature array with proper encoding
    x = np.zeros(7)  # Adjust size based on actual model features
    
    # Numerical features
    x[0] = Area_SqFt
    x[1] = Floor_No
    x[2] = Bedroom
    x[3] = Bathroom
    
    # Property Age encoding (example - adjust based on your data)
    if Property_Age == 'New':
        x[4] = 1
    
    # Location encoding (example - adjust based on your data)
    if Location == 'Downtown':
        x[5] = 1
    elif Location == 'Suburb':
        x[6] = 1
    
    return reg.predict([x])[0]

def run_ml_app():
    st.subheader('Property Price Calculator')
    
    # User inputs
    col1, col2 = st.columns(2)
    with col1:
        Location = st.selectbox('Location', df['Region'].unique())
        Area_SqFt = st.number_input('Area (SqFt)', min_value=500, max_value=10000, step=100)
        Floor_No = st.selectbox('Floor Number', sorted(df['Floor_No'].unique()))
    with col2:
        Bedroom = st.selectbox('Bedrooms', sorted(df['Bedroom'].unique()))
        Bathroom = st.selectbox('Bathrooms', sorted(df['Bathroom'].unique()))
        Property_Age = st.selectbox('Property Age', df['Property_Age'].unique())
    
    # Prediction and visualization
    if st.button('Estimate Price'):
        # Calculate prediction
        price = predict_price(Location, Area_SqFt, Floor_No, Bathroom, Bedroom, Property_Age)
        st.success(f'Estimated Price: ₹{price:.2f} Lakhs')
        
        # Actual vs Predicted Plot
        st.subheader("Actual vs Predicted Prices Comparison")
        
        # Sample data for visualization
        sample = df.sample(100)
        predictions = sample.apply(lambda row: predict_price(
            row['Region'], row['Area_SqFt'], row['Floor_No'],
            row['Bathroom'], row['Bedroom'], row['Property_Age']
        ), axis=1)
        
        # Create plot
        fig, ax = plt.subplots(figsize=(8, 6))
       
        ax.scatter(sample['Price_Lakh'], predictions, alpha=0.6, label='Properties')

        ax.plot([sample['Price_Lakh'].min(), sample['Price_Lakh'].max()], 
                [sample['Price_Lakh'].min(), sample['Price_Lakh'].max()], 
                'r--', label='Perfect Prediction')
        ax.set_xlabel('Actual Price (Lakhs)')
        ax.set_ylabel('Predicted Price (Lakhs)')
        ax.set_title('Model Performance: Actual vs Predicted Prices')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

if __name__ == '__main__':
    run_ml_app()