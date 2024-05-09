import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from streamlit_option_menu import option_menu
import joblib
import plotly.express as px

# Load the trained model
model = joblib.load('svm_model.pkl')
df = pd.read_csv("water_potability.csv")

# Streamlit app
def main():
    # st.title('Water Quality Index Project')
    
    selected_option = option_menu(
        menu_title=None,  # required
        options=["About the Project", "📊 Prediction", "❓ Myth v/s Fact", "📚 Basic Knowledge"],  # required
        icons=["info", "📊", "❓", "📚"],  # optional
        #menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#ffffff"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#74ccf4"},
        },
    )

    if selected_option == "Select Option":
        st.error("No option selected. Select an option to get started.")
    # Display content based on selected option


#---------------------------------------------------------------------------------------------------------------------------------------------------------------


    elif selected_option == "About the Project":
        st.title("About the Project")
        st.subheader("About the Dataset")
        st.write("The water_potability.csv file contains water quality metrics for 3276 different water bodies.")
        
        st.subheader("1. pH value")
        st.write("PH is an important parameter in evaluating the acid–base balance of water. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5.")
        
        st.subheader("2. Hardness")
        st.write("Hardness is mainly caused by calcium and magnesium salts. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium.")
        
        st.subheader("3. Solids (Total dissolved solids - TDS)")
        st.write("The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 1500 mg/l and maximum limit is 3000 mg/l which prescribed for drinking purpose.")
        
        st.subheader("4. Chloramines")
        st.write("Chlorine and chloramine are the major disinfectants used in public water systems. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.")
        
        st.subheader("5. Sulfate")
        st.write("Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. It ranges from 200 to 600 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.")
        
        st.subheader("6. Conductivity")
        st.write("The amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.")
        
        st.subheader("7. Organic_carbon")
        st.write("Organic Carbon is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 20 mg/L as TOC in treated  drinking water, and < 40 mg/Lit in source water which is use for treatment.")
        
        st.subheader("8. Trihalomethanes")
        st.write("The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water. THM levels around 80 ppm is considered safe in drinking water.")
        
        st.subheader("9. Turbidity")
        st.write("The turbidity of water depends on the quantity of solid matter present in the suspended state. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.")
        
        st.subheader("10. Potability")
        st.write("Indicates if water is safe for human consumption where 1 means Potable and 0 means Not potable.")


#---------------------------------------------------------------------------------------------------------------------------------------------------------------


    elif selected_option == "📊 Prediction":
        st.write("<h1 style='text-align: center;'>Water Quality Prediction</h1>",unsafe_allow_html=True)
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

    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------


    elif selected_option == "❓ Myth v/s Fact":
        st.write("<h1 style='text-align: center;'>Some myths regarding water purification</h1>",unsafe_allow_html=True)
        st.subheader("1. Boiling Water:")
        st.write("<b>Universal Myth:</b> Drinking, boiled water is completely safe.", unsafe_allow_html=True)
        st.write("<b>Fact:</b> It requires 20 minutes of effective boiling to kill viruses and bacteria. It is still not safe if the water is contaminated with pesticides, heavy metals and arsenic.", unsafe_allow_html=True)
        st.image("images/boiled_water.jpg")

        st.subheader("2. Water Filtration Systems:")
        st.write("<b>Universal Myth:</b> Filtration Removes All Minerals, Making Water Unhealthy.", unsafe_allow_html=True)
        st.write("<b>Fact:</b> Water filtration indeed removes minerals, but the percentage of calcium, iron, etc., in water is almost negligible. Drinking water with some mineral content is beneficial for health.", unsafe_allow_html=True)
        st.image("images/water_filter.jpg")

        st.subheader("3. Water Filters:")
        st.write("<b>Universal Myth:</b> Water filters are all you need to ensure safe drinking water.", unsafe_allow_html=True)
        st.write("<b>Fact:</b> Different types of filters target specific contaminants, so it's essential to choose the right filter for your water quality concerns.", unsafe_allow_html=True)
        st.image("images/filters.jpg")

        st.subheader("4. Bottled Water:")
        st.write("<b>Universal Myth:</b> Bottled water is always safer and cleaner than tap water.", unsafe_allow_html=True)
        st.write("<b>Fact:</b> Both bottled water and tap water are regulated by government agencies to ensure safety. In many cases, tap water is subject to more stringent testing and regulations than bottled water.", unsafe_allow_html=True)
        st.image("images/bottle.jpg")
        
        st.subheader("5. Drinking contaminated water:")
        st.write("<b>Universal Myth:</b> All waterborne illnesses come from drinking contaminated water.", unsafe_allow_html=True)
        st.write("<b>Fact:</b> Waterborne illnesses can also be contracted through other means such as swimming or bathing in contaminated water, or consuming contaminated food. ", unsafe_allow_html=True)
        st.image("images/dirty_water.jpg")


#---------------------------------------------------------------------------------------------------------------------------------------------------------------


    elif selected_option == "📚 Basic Knowledge":
        st.write("<h1 style='text-align: center;'>Basics to Identify Water Quality</h1>",unsafe_allow_html=True)
        st.write("As a normal person concerned about water quality, there are several measures or parameters you can take into account if the water quality results in poor conditions:")
        st.subheader("1. Appearance and Odor:")
        st.write("Water that appears discolored or has a foul smell may indicate contamination.")
        st.image("images/water1.jpg")

        st.subheader("2. pH level:")
        st.write("Test the pH level of the water using a <b><i>simple pH testing kit</i></b>. A pH value outside the normal range (typically between 6.5 and 8.5 for drinking water) can indicate acidity or alkalinity issues.", unsafe_allow_html=True)
        st.markdown("[Click Here to buy pH Test Kit. ↗️](https://www.amazon.in/AQUASOL-Aquasol-PH-Test-Kit/dp/B016QEQT80)")
        st.image("images/ph_level.jpg")

        st.subheader("3. Turbidity:")
        st.write("Assess the clarity of the water by observing how easily visible objects are when submerged.")
        st.image("images/turbidity.jpg")

        st.subheader("4. Comparative Analysis:")
        st.write("Comparing the taste, odor, and appearance of tap water to that of bottled or filtered water can sometimes reveal differences in quality. However, it's essential to remember that appearance alone does not necessarily indicate water safety.")
        st.image("images/versus.jpg")

        st.subheader("5. Community Monitoring Programs:")
        st.write("These programs often provide training and support to volunteers interested in monitoring local water sources. One of the popular water monitoring program:")
        st.markdown("[Click Here to know more. ↗️](https://www.nwtwaterstewardship.ca/en/nwt-wide-community-based-water-quality-program)")
        st.image("images/monitor.jpg")

if __name__ == '__main__':
    main()
