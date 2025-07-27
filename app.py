from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load('flight_price_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

categorical_cols = ['airline', 'flight', 'source_city', 'departure_time', 'arrival_time', 'destination_city', 'class']
numerical_cols = ['duration', 'days_left', 'stops']
expected_features = categorical_cols + numerical_cols
stops_mapping = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'two_or_more': 2}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/predictor')
def predictor_form():
    dropdown_data = {col: list(le.classes_) for col, le in label_encoders.items() if col in categorical_cols}
    stops_options = list(stops_mapping.keys())
    return render_template('index.html', dropdown_data=dropdown_data, stops_options=stops_options)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form.to_dict()
        new_df = pd.DataFrame([form_data])

        new_df['duration'] = new_df['duration'].astype(float)
        new_df['days_left'] = new_df['days_left'].astype(int)
        new_df['stops'] = new_df['stops'].map(stops_mapping).astype(int)

        for col in categorical_cols:
            if col in label_encoders:
                if new_df[col][0] not in label_encoders[col].classes_:
                    label_encoders[col].classes_ = np.append(label_encoders[col].classes_, new_df[col][0])
                new_df[col] = label_encoders[col].transform(new_df[col])
            else:
                return "Missing encoder for " + col

        X = new_df[expected_features].astype(float)
        predicted_price = model.predict(X)[0]

        dropdown_data = {col: list(le.classes_) for col, le in label_encoders.items() if col in categorical_cols}
        stops_options = list(stops_mapping.keys())

        return render_template('index.html', prediction=f"₹{predicted_price:.2f}", form_data=form_data,
                               dropdown_data=dropdown_data, stops_options=stops_options)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
