# Heart Disease Data Analysis and Visualization

## Project Overview

This project focuses on analyzing heart disease data through Exploratory Data Analysis (EDA) and visualizing key insights using a web-based dashboard built with **Streamlit**.

The analysis aims to explore patterns, correlations, and significant factors associated with heart disease. After the analysis, a dashboard application is provided to visualize the results interactively.

### Files and Structure

- `EDA_Analysis.ipynb`: Jupyter Notebook containing the full exploratory data analysis (EDA) process, including data cleaning, feature analysis, and visualizations.
- `app.py`: A Streamlit application to visualize the key insights and visualizations from the EDA in a user-friendly web interface.
- `heart_disease_cleaned.csv`: The cleaned dataset used for analysis and visualization. The dataset contains various health and demographic attributes of individuals, along with an indicator of heart disease.

## Requirements

To run this project, the following libraries are required:

- `pandas`
- `numpy`
- `plotly`
- `streamlit`

You can install these dependencies using the following command:

```bash
pip install pandas numpy plotly streamlit
```

Alternatively, you can create a `requirements.txt` file with the following contents and install all dependencies at once:

```bash
pandas
numpy
plotly
streamlit
```

Then install the dependencies with:

```bash
pip install -r requirements.txt
```

## Dataset

The `heart_disease_cleaned.csv` dataset contains the following key features:

- **Age**: Age of the patient.
- **Sex**: Gender of the patient (Male or Female).
- **Chest Pain Type**: Type of chest pain experienced.
- **Resting Blood Pressure**: Resting blood pressure (in mm Hg).
- **Cholesterol**: Serum cholesterol in mg/dl.
- **Fasting Blood Sugar**: Whether fasting blood sugar is greater than 120 mg/dl.
- **Resting ECG**: Resting electrocardiographic results.
- **Max Heart Rate**: Maximum heart rate achieved.
- **Exercise-Induced Angina**: Whether the patient experienced angina as a result of exercise.
- **ST Depression**: Exercise-induced ST depression relative to rest.
- **Heart Disease**: Indicator of the presence or absence of heart disease.

## Key Features

- **EDA Insights**: Understand key patterns in the data, such as how different features correlate with heart disease.
- **Interactive Visualizations**: Use the Streamlit app to interact with the visualizations, including feature distributions, correlations, and more.
- **User-friendly Dashboard**: Visualize complex data insights through an easy-to-use web-based dashboard.

## Conclusion

This project provides an end-to-end analysis and visualization of heart disease data. By exploring the dataset through EDA and visualizing insights via the Streamlit app, it offers an accessible way to explore factors related to heart disease.

Feel free to fork this repository, explore the analysis, and modify it to suit your own needs!

---

Let me know if you'd like to make any further modifications!
