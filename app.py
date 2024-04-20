import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

# Load the trained model
model = joblib.load('svm_model.pkl')

# Streamlit app
def main():
    st.title('Water Quality Prediction')

    # Sidebar inputs
    st.sidebar.header('Input Variables:')
    ph = st.sidebar.slider('pH level', min_value=0.0, max_value=14.0, step=0.1)
    hardness = st.sidebar.slider('Hardness', min_value=0.0, max_value=500.0, step=1.0)
    solids = st.sidebar.slider('Solids', min_value=0.0, max_value=5000.0, step=1.0)
    chloramines = st.sidebar.slider('Chloramines', min_value=0.0, max_value=20.0, step=0.1)
    sulfate = st.sidebar.slider('Sulfate', min_value=0.0, max_value=500.0, step=1.0)
    conductivity = st.sidebar.slider('Conductivity', min_value=0.0, max_value=1000.0, step=1.0)
    organic_carbon = st.sidebar.slider('Organic Carbon', min_value=0.0, max_value=50.0, step=0.1)
    trihalomethanes = st.sidebar.slider('Trihalomethanes', min_value=0.0, max_value=200.0, step=0.1)
    turbidity = st.sidebar.slider('Turbidity', min_value=0.0, max_value=10.0, step=0.1)

    # Predict button
    if st.sidebar.button('Predict'):
        # Prepare input data
        input_data = pd.DataFrame({
            'ph': [ph],
            'Hardness': [hardness],
            'Solids': [solids],
            'Chloramines': [chloramines],
            'Sulfate': [sulfate],
            'Conductivity': [conductivity],
            'Organic_carbon': [organic_carbon],
            'Trihalomethanes': [trihalomethanes],
            'Turbidity': [turbidity]
        })

        # Load scaler for standardization
        scaler = joblib.load('scaler.pkl')
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)
      

        # Display prediction result
        st.write("")
        st.write("")
        st.write("")
        if prediction[0] == 0:
            st.write("<span style='color:green; font-size:35px'><b>Water Quality is good.</b></span>", unsafe_allow_html=True)
            st.markdown("![Water Is Drinkable GIF](https://img.laitimes.com/img/__Qf2AjLwojIjJCLyojI0JCLiMGc902byZ2PkJmYmRmYhVGZ1IjZ5QDZ4QWYjRTYhlDO2EjZkJmZ4EzLcBza5QTcsJja2FXLp1ibj1ycvR3Lc5Wanlmcv9CXt92YucWbp9WYpRXdvRnLzA3Lc9CX6MHc0RHaiojIsJye.webp)")
        else:
            st.write("<span style='color:red; font-size:35px'><b>Water Quality is bad.</b></span>", unsafe_allow_html=True)
            st.markdown("![Water Is Not Drinkable GIF](https://cdn.dribbble.com/users/742615/screenshots/3293621/media/b6ea130ac9bab9d0acefae88e9ab7ce5.gif)")
        

if __name__ == '__main__':
    main()
