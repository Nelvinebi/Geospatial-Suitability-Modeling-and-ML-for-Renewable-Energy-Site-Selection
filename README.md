# Geospatial-Suitability-Modeling-and-ML-for-Renewable-Energy-Site-Selection
This project applies geospatial analysis and machine learning to identify suitable locations for renewable energy (solar and wind) installations in the Port Harcourt – Yenagoa region. A Random Forest classifier is trained on geographic and environmental features to predict site suitability classes (High, Moderate, Low).

Table of Contents
Dataset

Project Workflow

Exploratory Data Analysis

Visualizations

Machine Learning Model

Model Evaluation

Feature Importance

Spatial Visualization

Conclusion

## Dataset
The dataset (data.xlsx) contains 400 samples with the following attributes:

Column	Description
latitude	Geographic latitude
longitude	Geographic longitude
solar_irradiance	Solar energy potential (kWh/m²/day)
wind_speed	Wind speed (m/s)
land_slope	Terrain slope (degrees)
elevation_m	Elevation (meters)
distance_to_road_km	Distance to nearest road (km)
distance_to_grid_km	Distance to power grid (km)
land_use_type	Land use category (barren, forest, urban, etc.)
suitability_score	Continuous suitability score (0–1)
suitability_class	Target class: High, Moderate, Low
Target variable is suitability_class – a categorical rating of site appropriateness for renewable energy development.

## Project Workflow
Data Loading & Exploration – Inspect structure, summary statistics, and class distribution.

Visualization – Understand relationships between features and suitability.

Data Preprocessing – Encode categorical land_use_type using one-hot encoding.

Train/Test Split – 80% training, 20% testing (random state 42).

Random Forest Classifier – Train with 200 estimators.

Model Evaluation – Accuracy, classification report, confusion matrix.

Feature Importance – Identify key drivers of suitability.

Spatial Visualization – Map sites with suitability classes.

Exploratory Data Analysis
Basic statistics reveal:

solar_irradiance: mean 5.26 kWh/m²/day, range 3.04–7.31

wind_speed: mean 5.58 m/s, range 2.02–8.60

land_use_type: categories include barren, forest, urban, agricultural, wetland.

suitability_score: mean 0.516, min 0.265, max 0.833.

suitability_class: distribution is imbalanced – Moderate (40%), Low (37%), High (23%).

## Visualizations
1. Suitability Class Distribution

Shows the number of locations per suitability class.

Moderate and Low classes dominate; High suitability sites are scarce, which may affect model performance for the minority class.

2. Solar vs Wind Energy Potential

Scatter plot of solar irradiance vs. wind speed, colored by suitability class.

High suitability sites tend to cluster in regions with higher solar irradiance and moderate wind speeds.

Low suitability sites are scattered, often with lower solar or extreme wind values.

3. Suitability Score by Land Use Type

Box plots show the distribution of the continuous suitability score across land use categories.

Barren land exhibits the highest median suitability, followed by agricultural and urban.

Wetland and forest areas have the lowest suitability scores, likely due to environmental constraints.

4. Spatial Distribution of Sites

Geographic coordinates plotted with color coding by suitability class.

High suitability sites appear clustered, while Low and Moderate sites are more dispersed.

This suggests spatial autocorrelation – suitable areas may form contiguous zones.

## Machine Learning Model
Algorithm: Random Forest Classifier (n_estimators=200, random_state=42)

Features: All numeric columns plus one-hot encoded land use types.

Target: suitability_class (High, Moderate, Low).

Train/Test Split: 320 train, 80 test samples.

Model Evaluation
Accuracy: 91.25% on the test set.

Classification Report:

text
              precision    recall  f1-score   support

        High       1.00      0.33      0.50         3
         Low       0.94      0.92      0.93        37
    Moderate       0.88      0.95      0.92        40

    accuracy                           0.91        80
   macro avg       0.94      0.73      0.78        80
weighted avg       0.92      0.91      0.91        80
The model performs very well for Low and Moderate classes.

High class has low recall (0.33) due to the small number of samples (only 3 in test set).

Overall accuracy is strong, but the minority class is difficult to predict.

Confusion Matrix:


Shows correct and incorrect predictions per class.

Misclassifications mostly involve High being confused with Moderate.

Feature Importance

Top features influencing suitability:

distance_to_grid_km – proximity to existing grid infrastructure.

elevation_m – elevation affects wind patterns and construction costs.

solar_irradiance – primary solar energy potential.

wind_speed – primary wind energy potential.

land_slope – terrain slope impacts feasibility.

distance_to_road_km – accessibility for construction.

land_use_type (dummies) – certain land uses (e.g., barren) are more suitable.

The dominance of grid distance and elevation suggests that infrastructure and topography are critical constraints.

## Spatial Visualization
The final scatter plot of latitude vs. longitude, colored by suitability class, highlights geographic patterns. Potential high-suitability zones can be identified for further field investigation.

## Conclusion
This project demonstrates a complete pipeline for renewable energy site suitability modeling using geospatial data and machine learning. The Random Forest model achieves high accuracy (91%) and reveals that grid proximity, elevation, and solar/wind potential are the most influential factors. The visualizations provide intuitive insights into the data and support decision‑making for energy planning.

## Limitations: The small number of high‑suitability samples limits the model's ability to generalize for that class. Future work could incorporate more data or use techniques like SMOTE to balance classes.

Requirements
Python 3.x

pandas, numpy, matplotlib, seaborn

scikit-learn

openpyxl (for Excel reading)

Install dependencies with:

bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
Run the notebook sequentially to reproduce the analysis.

Author:
AGBOZU EBINGIYE NELVIN



Date: March 2025

License: MIT

