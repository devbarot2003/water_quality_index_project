import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib
import plotly.express as px

# Load the trained model
model = joblib.load('svm_model.pkl')
df = pd.read_csv("water_potability.csv")

# Streamlit app
def main():
    # st.title('Water Quality Index Project')
    selected_option = st.sidebar.selectbox(
        "Select Option",
        ("Select Option", "About the Project", "Prediction", "Analysis Figures")
    )

    if selected_option == "Select Option":
        st.error("No option selected. Select an option to get started.")
    # Display content based on selected option
    elif selected_option == "About the Project":
        st.title("About the Project")
        st.subheader("About the Dataset")
        st.write("The water_potability.csv file contains water quality metrics for 3276 different water bodies.")
        
        st.subheader("1. pH value")
        st.write("PH is an important parameter in evaluating the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5. The current investigation ranges were 6.52–7.83 which are in the range of WHO standards.")
        
        st.subheader("2. Hardness")
        st.write("Hardness is mainly caused by calcium and magnesium salts. These salts are dissolved from geologic deposits through which water travels. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium.")
        
        st.subheader("3. Solids (Total dissolved solids - TDS)")
        st.write("Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and diluted color in appearance of water. This is the important parameter for the use of water. The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 1500 mg/l and maximum limit is 3000 mg/l which prescribed for drinking purpose.")
        
        st.subheader("4. Chloramines")
        st.write("Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.")
        
        st.subheader("5. Sulfate")
        st.write("Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. The principal commercial use of sulfate is in the chemical industry. Sulfate concentration in seawater is about 2,700 milligrams per liter (mg/L). It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.")
        
        st.subheader("6. Conductivity")
        st.write("Pure water is not a good conductor of electric current rather’s a good insulator. Increase in ions concentration enhances the electrical conductivity of water. Generally, the amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.")
        
        st.subheader("7. Organic_carbon")
        st.write("Total Organic Carbon (TOC) in source waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment.")
        
        st.subheader("8. Trihalomethanes")
        st.write("THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water that is being treated. THM levels around 80 ppm is considered safe in drinking water.")
        
        st.subheader("9. Turbidity")
        st.write("The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.")
        
        st.subheader("10. Potability")
        st.write("Indicates if water is safe for human consumption where 1 means Potable and 0 means Not potable.")
    
    elif selected_option == "Prediction":
        st.title('Water Quality Prediction')
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
    
    elif selected_option == "Analysis Figures":
        st.title("Analysis of Dataset")

        st.markdown("<h4 style='text-align: center;'>1. Heatmap of Null Values in dataset</h4>", unsafe_allow_html=True)
        st.image("images/Null_values_heatmap.png")

        st.markdown("<h4 style='text-align: center;'>2. Heatmap of dataset</h4>", unsafe_allow_html=True)
        st.image("images/Normal_heatmap.png")

        st.markdown("<h4 style='text-align: center;'>3. Countplot of Potability</h4>", unsafe_allow_html=True)
        st.image("images/countplot_potability.png")

        st.markdown("<h4 style='text-align: center;'>4. Violin plot of pH-level</h4>", unsafe_allow_html=True)
        st.image("images/Violin_plot_ph_level.png")

        st.markdown("<h4 style='text-align: center;'>5. Boxplot of all columns in dataset</h4>", unsafe_allow_html=True)
        st.image("images/boxplots.png")

        st.markdown("<h4 style='text-align: center;'>6. Histogram of all columns in dataset</h4>", unsafe_allow_html=True)
        st.image("images/histograms.png")

        st.markdown("<h4 style='text-align: center;'>7. Pairplot of dataset</h4>", unsafe_allow_html=True)
        st.image("images/pairplot.png")

        st.markdown("<h4 style='text-align: center;'>8. Potability V/S pH in barplot</h4>", unsafe_allow_html=True)
        st.image("images/ potability_ph_comparison_bar.png")

        st.markdown("<h4 style='text-align: center;'>9. Potability V/S Hardness via barplot</h4>", unsafe_allow_html=True)
        st.image("images/ potability_hardness_comparison_bar.png")

        st.markdown("<h4 style='text-align: center;'>10. Potability V/S Sulfate via histogram</h4>", unsafe_allow_html=True)
        st.image("images/potability_sulfate_comparison_hist.png")

        st.markdown("<h4 style='text-align: center;'>11. Potability V/S Trihalomethane via histogram</h4>", unsafe_allow_html=True)
        st.image("images/potability_methane_comparison_hist.png")

        st.markdown("<h4 style='text-align: center;'>12. Pie chart of Potability</h4>", unsafe_allow_html=True)
        st.image("images/potability_pie.png")

        st.markdown("<h4 style='text-align: center;'>13. Potability V/S Sulfate via Scatterplot</h4>", unsafe_allow_html=True)
        st.image("images/potability_sulfate_comparison_scatter.png")

        st.markdown("<h4 style='text-align: center;'>14. Potability V/S Organic Carbon via Scatterplot</h4>", unsafe_allow_html=True)
        st.image("images/potability_carbon_comparison_scatter.png")

        st.markdown("<h4 style='text-align: center;'>15. Model accuracy comparison</h4>", unsafe_allow_html=True)
        st.image("images/model_comaprison_bar.png")
        
if __name__ == '__main__':
    main()
