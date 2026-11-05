# Algerian Forest Fire Prediction

A Machine Learning web application that predicts the Fire Weather Index (FWI) using weather and environmental parameters.

The application is built using Python, Flask, and Ridge Regression, with a simple and responsive user interface.

## Features

- Predicts the Fire Weather Index (FWI)
- Displays a fire status based on an FWI threshold
- Flask-based web application
- User-friendly HTML form
- Custom CSS styling

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS

## Machine Learning Model

The project uses Ridge Regression to predict the numerical FWI value.

The displayed Yes/No fire status is determined using a threshold applied to the predicted FWI. It is not a direct fire-occurrence classification model.

## Project Structure

├── application.py
├── requirements.txt
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
├── templates/
│   └── home.html
└── static/
    └── style.css

How to Run Locally

1. Clone this repository.
2. Install the required dependencies:
pip install -r requirements.txt

3. Run the Flask application:
python application.py

4. Open your browser and visit:
text
http://127.0.0.1:5000


Machine Learning Project — Algerian Forest Fire Prediction
