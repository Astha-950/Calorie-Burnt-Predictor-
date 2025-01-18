
# Calorie-Burnt-Predictor-

A machine learning-powered web application that predicts the number of calories burnt during exercise based on user inputs like duration, gender, weight, height, body temperature, and heart rate. This project demonstrates end-to-end machine learning workflow, including data cleaning, exploratory data analysis (EDA), model training, and deployment using a user-friendly web interface.
# Features

- **User Input Form:**:  
  Enter personal details (duration, gender, weight, height, body temperature, and heart rate) to predict calories burnt.

- **Machine Learning Model:**:  
  A trained regression model to provide accurate calorie predictions.

- **Data Cleaning and Preprocessing:**:  
  Handled missing values, outliers, and other irregularities to ensure robust model training.

- **EDA (Exploratory Data Analysis):**:  
  Gained insights into the relationships between variables using visualizations like scatter plots, heatmaps, and histograms.

- **Interactive Web Application:**:  
  Built with a clean UI to make predictions easy and accessible for u## How It Works

1. **Data Collection**:  
   Two datasets, *Exercise* and *Calorie*, were combined and processed to create a clean and integrated dataset.

2. **Data Preprocessing**:  
   - Handled missing or inconsistent values.
   - Normalized and scaled the features for better model performance.

3. **EDA**:  
   - Analyzed correlations between features like duration, heart rate, and calories burnt.  
   - Visualized patterns and trends to identify the most important predictors.

4. **Model Creation**:  
   - Used regression algorithms to predict calories burnt.  
   - Evaluated performance using metrics like MSE (Mean Squared Error) and R² Score.

5. **Web Application**:  
   - A simple form allows users to input details.  
   - The app processes the inputs and returns a prediction for calories burnt in real time.

---

## Technologies Used

### Backend:
- **Python**: Core programming language for data processing and model training.
- **Pandas & NumPy**: For data manipulation and preprocessing.
- **Scikit-learn**: For training the regression model.
- **Matplotlib & Seaborn**: For visualizing data trends during EDA.

### Frontend:
- **Streamlit**: For creating an interactive and user-friendly web app interface.

### Deployment:
- **Local Deployment**: Run the app directly on your machine using Streamlit.

---
# Run Locally

Clone the project

```bash
  git clone https://github.com/Astha-950/Calorie-Burnt-Predictor-.git
```

Go to the project directory

```bash
  cd Organic
```

  Install dependencies

```bash
 pip install -r requirements.txt
```

Start the Application

```bash
  streamlit run app.py
```
