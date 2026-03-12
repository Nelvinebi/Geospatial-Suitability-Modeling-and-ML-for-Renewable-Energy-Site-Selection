# 🌍 Geospatial-Suitability-Modeling-and-ML-for-Renewable-Energy-Site-Selection

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://svj9ip3wkvv5qbgh6vksa2.streamlit.app)

🔗 **Live Dashboard:** https://svj9ip3wkvv5qbgh6vksa2.streamlit.app

![confusion matrix](https://github.com/Nelvinebi/Geospatial-Suitability-Modeling-and-ML-for-Renewable-Energy-Site-Selection/blob/416378c9e8d89859cab02c72fefee8e6ebece864/Confusion%20Matrix.png)

This project applies geospatial analysis and machine learning to identify suitable locations for renewable energy (solar and wind) installations in the Port Harcourt – Yenagoa region. A Random Forest classifier is trained on geographic and environmental features to predict site suitability classes (High, Moderate, Low).

## Table of Contents
- [Live Demo](#live-demo)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Visualizations](#visualizations)
- [Machine Learning Model](#machine-learning-model)
- [Model Evaluation](#model-evaluation)
- [Feature Importance](#feature-importance)
- [Spatial Visualization](#spatial-visualization)
- [Conclusion](#conclusion)

---

## 🚀 Live Demo

Try the interactive dashboard here: **https://svj9ip3wkvv5qbgh6vksa2.streamlit.app**

### Dashboard Features:
- 🗺️ **Interactive Map** – Explore renewable energy sites geographically
- ⚡ **Real-time Filtering** – Filter by wind speed, solar irradiance, and suitability class
- 🤖 **ML Predictions** – Input environmental variables and get instant suitability predictions
- 📊 **Scenario Simulation** – Test different wind/solar combinations
- 📈 **Data Visualizations** – Distribution charts and analytics

---

## Dataset
The dataset (data.xlsx) contains 400 samples with the following attributes:

| Column | Description |
|--------|-------------|
| latitude | Geographic latitude |
| longitude | Geographic longitude |
| solar_irradiance | Solar energy potential (kWh/m²/day) |
| wind_speed | Wind speed (m/s) |
| land_slope | Terrain slope (degrees) |
| elevation_m | Elevation (meters) |
| distance_to_road_km | Distance to nearest road (km) |
| distance_to_grid_km | Distance to power grid (km) |
| land_use_type | Land use category (barren, forest, urban, etc.) |
| suitability_score | Continuous suitability score (0–1) |
| suitability_class | Target class: High, Moderate, Low |

**Target variable:** `suitability_class` – a categorical rating of site appropriateness for renewable energy development.

---

## Project Workflow
1. **Data Loading & Exploration** – Inspect structure, summary statistics, and class distribution.
2. **Visualization** – Understand relationships between features and suitability.
3. **Data Preprocessing** – Encode categorical `land_use_type` using one-hot encoding.
4. **Train/Test Split** – 80% training, 20% testing (random state 42).
5. **Random Forest Classifier** – Train with 200 estimators.
6. **Model Evaluation** – Accuracy, classification report, confusion matrix.
7. **Feature Importance** – Identify key drivers of suitability.
8. **Spatial Visualization** – Map sites with suitability classes.
9. **Dashboard Deployment** – Interactive Streamlit app for end-users.

---

## Exploratory Data Analysis
Basic statistics reveal:

- **solar_irradiance:** mean 5.26 kWh/m²/day, range 3.04–7.31
- **wind_speed:** mean 5.58 m/s, range 2.02–8.60
- **land_use_type:** categories include barren, forest, urban, agricultural, wetland.
- **suitability_score:** mean 0.516, min 0.265, max 0.833.
- **suitability_class:** distribution is imbalanced – Moderate (40%), Low (37%), High (23%).

---

## Visualizations

### 1. Suitability Class Distribution
![Suitability Distribution](https://github.com/Nelvinebi/Geospatial-Suitability-Modeling-and-ML-for-Renewable-Energy-Site-Selection/blob/30f59027a9c37ef01d287d2be7d8968ff4e9bc10/Suitability%20Distribution.png)

Shows the number of locations per suitability class. Moderate and Low classes dominate; High suitability sites are scarce, which may affect model performance for the minority class.

### 2. Solar vs Wind Energy Potential
![Solar vs Wind](https://github.com/Nelvinebi/Geospatial-Suitability-Modeling-and-ML-for-Renewable-Energy-Site-Selection/blob/30f59027a9c37ef01d287d2be7d8968ff4e9bc10/Wind%20vs%20Solar.png)

Scatter plot of solar irradiance vs. wind speed, colored by suitability class. High suitability sites tend to cluster in regions with higher solar irradiance and moderate wind speeds.

### 3. Suitability Score by Land Use Type
![Suitability Score](https://github.com/Nelvinebi/Geospatial-Suitability-Modeling-and-ML-for-Renewable-Energy-Site-Selection/blob/57e2173de509a9df16b4458583e3a64376c6c612/Suitability%20score.png)

Box plots show the distribution of the continuous suitability score across land use categories. Barren land exhibits the highest median suitability.

### 4. Spatial Distribution of Sites
![Spatial Distribution](https://github.com/Nelvinebi/Geospatial-Suitability-Modeling-and-ML-for-Renewable-Energy-Site-Selection/blob/e17395780519151f55a315e092c666b0a37f9ca8/image_1.png)

Geographic coordinates plotted with color coding by suitability class. High suitability sites appear clustered, suggesting spatial autocorrelation.

---

## Machine Learning Model
- **Algorithm:** Random Forest Classifier (n_estimators=200, random_state=42)
- **Features:** All numeric columns plus one-hot encoded land use types
- **Target:** `suitability_class` (High, Moderate, Low)
- **Train/Test Split:** 320 train, 80 test samples

---

## Model Evaluation
**Accuracy:** 91.25% on the test set.

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| High | 1.00 | 0.33 | 0.50 | 3 |
| Low | 0.94 | 0.92 | 0.93 | 37 |
| Moderate | 0.88 | 0.95 | 0.92 | 40 |

The model performs very well for Low and Moderate classes. High class has low recall (0.33) due to the small number of samples.

---

## Feature Importance
Top features influencing suitability:

1. `distance_to_grid_km` – proximity to existing grid infrastructure
2. `elevation_m` – elevation affects wind patterns and construction costs
3. `solar_irradiance` – primary solar energy potential
4. `wind_speed` – primary wind energy potential
5. `land_slope` – terrain slope impacts feasibility

---

## Spatial Visualization
The final scatter plot of latitude vs. longitude, colored by suitability class, highlights geographic patterns. Potential high-suitability zones can be identified for further field investigation.

---

## Conclusion
This project demonstrates a complete pipeline for renewable energy site suitability modeling using geospatial data and machine learning. The Random Forest model achieves high accuracy (91%) and reveals that grid proximity, elevation, and solar/wind potential are the most influential factors.

### Limitations
The small number of high-suitability samples limits the model's ability to generalize for that class. Future work could incorporate more data or use techniques like SMOTE to balance classes.

---

## Requirements
```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl streamlit plotly joblib
Usage
Run the Analysis Notebook
bash
Copy
jupyter notebook
Run the Dashboard Locally
bash
Copy
streamlit run app.py
Author
AGBOZU EBINGIYE NELVIN
📅 Date: March 2025
🔗 LinkedIn: [https://www.linkedin.com/in/agbozu-ebi/]
💻 GitHub: https://github.com/Nelvinebi
📧 Email: [nelvinebingiye@gmail.com]
🌐 Live Demo: https://svj9ip3wkvv5qbgh6vksa2.streamlit.app
License: MIT
