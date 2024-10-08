# DATA PREPROCESSING
"""
import pandas as pd

# Read the data file (sourced from https://www.kaggle.com/datasets/abdmental01/heart-disease-dataset/data) into a DataFrame:
heart_disease_data = pd.read_csv("heart_disease_cleaned.csv")

# Remove irrelevant columns and keep only the ones needed for analysis:
heart_disease_data = heart_disease_data[['id', 'age', 'sex', 'dataset', 'cp', 'trestbps', #'chol', 'fbs',
       #'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 
       'num']].copy()

# Print the cleaned data to verify the changes
print(heart_disease_data)

# Rename the columns to more descriptive names
heart_disease_data = heart_disease_data.rename(columns={
    'id': 'patient_id',
    'dataset': 'place_of_study',
    'cp': 'chest_pain_type',
    'trestbps': 'resting_blood_pressure',
    'num': 'predicted_attribute'
})

# Replace numerical values in the 'predicted_attribute' column with descriptive labels:
heart_disease_data['predicted_attribute'] = heart_disease_data['predicted_attribute'].replace(
    {
        0: 'no heart disease',
        1: 'mild heart disease',
        2: 'moderate heart disease',
        3: 'severe heart disease',
        4: 'critical heart disease'
    }
)

# Ensure the 'predicted_attribute' column is of type string:
heart_disease_data['predicted_attribute'] = heart_disease_data['predicted_attribute'].astype(str)

# Save the modified DataFrame to a new CSV file
heart_disease_data.to_csv('heart_disease_data.csv', index=False)

"""

# DATA VISUALISATION
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Heart Disease Data Visualisation', layout='wide')

# Load the data
heart_disease_data = pd.read_csv('heart_disease_data.csv')

# Sidebar for user input
with st.sidebar:
    st.header('Options')
    st.write('Choose from the following areas for visualisation')
    study = st.multiselect('Which study data would you like to view?', heart_disease_data['place_of_study'].unique(), default=heart_disease_data['place_of_study'].unique())

# If no study area is selected, show the total study data
if not study:
    st.write("No specific study area selected. Showing total study data.")
    study_df = heart_disease_data
else:
    study_df = heart_disease_data.loc[heart_disease_data['place_of_study'].isin(study)]

# Scatter plot 
fig_scatter = px.scatter(study_df, x='age', y='resting_blood_pressure', color='sex', 
                         color_discrete_sequence=px.colors.qualitative.D3, 
                         title='Age vs Blood Pressure', 
                         hover_data=['chest_pain_type', 'place_of_study'])

# Pie chart 
heart_disease_data_pie = study_df['sex'].value_counts().reset_index()
heart_disease_data_pie.columns = ['sex', 'count']
fig_pie = px.pie(heart_disease_data_pie, values='count', names='sex', 
                 color='sex', color_discrete_sequence=px.colors.qualitative.Pastel,
                 title='Distribution of Sex')

# Histogram 
fig_histogram = px.histogram(study_df, x='age', color='sex', marginal='box', 
                             nbins=20, hover_data=['chest_pain_type', 'place_of_study'], 
                             title='Age distribution',
                             color_discrete_sequence=px.colors.qualitative.Set2)

# Function to generate heatmap 
def generate_heatmap(data, title_suffix):
    heart_disease_counts = data.groupby(['chest_pain_type', 'sex', 'predicted_attribute']).size().reset_index(name='count')
    heatmap_data = heart_disease_counts.pivot_table(index='chest_pain_type', columns='predicted_attribute', values='count', aggfunc='sum', fill_value=0)
    fig_heatmap = px.imshow(
        heatmap_data,
        labels=dict(x="Heart Disease Severity", y="Chest Pain Type", color="Count"),
        title=f"Distribution of Heart Disease Severity by Chest Pain Type {title_suffix}",
        color_continuous_scale=px.colors.sequential.Teal
    )
    st.plotly_chart(fig_heatmap)

# Display plots
with st.expander('Expand me to see the data'):
    st.dataframe(study_df, use_container_width=True)

st.plotly_chart(fig_histogram)
st.plotly_chart(fig_pie)
st.plotly_chart(fig_scatter)

# Generate heatmap for selected locations
if study:
    for location in study:
        generate_heatmap(study_df[study_df['place_of_study'] == location],f"at {location}")
else:
    generate_heatmap(study_df, "for All Locations")
