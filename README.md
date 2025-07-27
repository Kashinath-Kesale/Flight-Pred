# ✈️ Flight Price Prediction  

**SkyFlights** is a **Machine Learning-powered web application** that predicts flight ticket prices based on factors like airline, source, destination, class, departure/arrival times, and more.  
The model is trained on **300,000+ real-world flight records** and achieves **state-of-the-art accuracy** using advanced ensemble methods.  

---

## 🔧 **Tech Stack**  

- **Backend & Model**: Python, Flask  
- **Libraries**: Pandas, NumPy, Scikit-learn  
- **Visualization**: Matplotlib, Seaborn  
- **Algorithm**: Random Forest Regressor (**R² = 0.985**)  
- **Frontend**: HTML, CSS (Responsive UI)  
- **Dataset**: `Flight_Booking.csv` (from Kaggle)  

---

## 🚀 **Features**  
- 🎯 **Accurate Price Prediction** based on user-selected flight parameters.  
- 🔍 **Data Preprocessing** – handles missing values, label encoding, and feature engineering.  
- 📊 **Model Comparison** with multiple ML algorithms.  
- 🎨 **Interactive Web App** – simple, modern UI for quick predictions.  
- 📈 **Data Insights & Visualizations** from 300k+ flight records.  

---

## 📊 **Model Performance**  

| Model                | R² Score   |  
|---------------------|------------|  
| Linear Regression    | 0.9052     |  
| Decision Tree        | 0.9768     |  
| Bagging Regressor    | 0.9844     |  
| 🌟 Random Forest      | **0.9854** |  

---

## 🖼 **Screenshots**  


---

## ⚡ **How to Run Locally**  
```bash
# Clone the repository
git clone https://github.com/<your-username>/Flight-Pred.git
cd Flight-Pred

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py


# MIT License

Copyright (c) 2025 Kashinath Kesale

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



