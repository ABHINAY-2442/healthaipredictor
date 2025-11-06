# 🏥 AI Health Predictor

## Early Disease Detection Using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/sklearn-1.3.0-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive machine learning-based web application that predicts the risk of three major diseases: **Diabetes**, **Heart Disease**, and **Parkinson's Disease**.

![AI Health Predictor Banner](https://via.placeholder.com/800x200/1f77b4/ffffff?text=AI+Health+Predictor)

## 🌟 Features

- 🩺 **Diabetes Prediction** - SVM model with 78-81% accuracy
- ❤️ **Heart Disease Prediction** - Logistic Regression with 85% accuracy
- 🧠 **Parkinson's Disease Prediction** - SVM model with 87-95% accuracy
- 🎨 **User-Friendly Interface** - Built with Streamlit
- ⚡ **Real-Time Predictions** - Instant risk assessment
- 📊 **Comprehensive Results** - Detailed recommendations for each prediction
- 🔒 **Privacy-Focused** - No data storage, all processing in real-time
- 📱 **Responsive Design** - Works on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-health-predictor.git
cd ai-health-predictor
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\\Scripts\\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the app**
Open your browser and navigate to `http://localhost:8501`

## 📁 Project Structure

```
ai-health-predictor/
│
├── app.py                      # Main Streamlit application
├── train_models.py             # Model training script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── models/                     # Trained ML models
│   ├── diabetes_model.pkl
│   ├── heart_model.pkl
│   └── parkinsons_model.pkl
│
├── scalers/                    # Feature scalers
│   ├── scaler_diabetes.pkl
│   ├── scaler_heart.pkl
│   └── scaler_parkinsons.pkl
│
└── data/                       # Training datasets
    ├── diabetes.csv
    ├── heart.csv
    └── parkinsons.csv
```

## 💻 Technology Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.8+ |
| **Web Framework** | Streamlit |
| **ML Library** | scikit-learn |
| **Data Processing** | pandas, numpy |
| **Serialization** | pickle |
| **Deployment** | Streamlit Cloud, Heroku |

## 🤖 Machine Learning Models

### 1. Diabetes Prediction
- **Algorithm**: Support Vector Machine (SVM)
- **Accuracy**: 78-81%
- **Input Features**: 8 clinical parameters
- **Dataset**: PIMA Indians Diabetes Database

### 2. Heart Disease Prediction
- **Algorithm**: Logistic Regression
- **Accuracy**: 85%
- **Input Features**: 11 cardiovascular parameters
- **Dataset**: UCI Heart Disease Dataset

### 3. Parkinson's Disease Prediction
- **Algorithm**: Support Vector Machine (SVM)
- **Accuracy**: 87-95%
- **Input Features**: 13 vocal measurement parameters
- **Dataset**: UCI Parkinson's Dataset

## 📊 Model Performance

| Disease | Algorithm | Accuracy | Precision | Recall | F1-Score |
|---------|-----------|----------|-----------|--------|----------|
| Diabetes | SVM | 78-81% | 76.8-81.0% | 75.9-80.2% | 76.1-81.2% |
| Heart Disease | Logistic Regression | 85% | 84.5% | 83.7% | 84.1% |
| Parkinson's | SVM | 87-95% | 82.0-95.0% | 81.5-94.5% | 81.5-94.7% |

## 📖 Usage Guide

### Diabetes Prediction
1. Navigate to "Diabetes Prediction" from the sidebar
2. Enter the following parameters:
   - Number of Pregnancies
   - Glucose Level (mg/dL)
   - Blood Pressure (mm Hg)
   - Skin Thickness (mm)
   - Insulin Level (mu U/ml)
   - BMI
   - Diabetes Pedigree Function
   - Age
3. Click "Predict Diabetes"
4. Review the results and recommendations

### Heart Disease Prediction
1. Navigate to "Heart Disease Prediction"
2. Enter cardiovascular parameters:
   - Age, Sex, Chest Pain Type
   - Resting BP, Cholesterol
   - Fasting Blood Sugar
   - Resting ECG, Max Heart Rate
   - Exercise Angina, Oldpeak, ST Slope
3. Click "Predict Heart Disease"
4. Review the risk assessment

### Parkinson's Prediction
1. Navigate to "Parkinson's Prediction"
2. Enter vocal measurement parameters:
   - MDVP frequencies (Fo, Fhi, Flo)
   - Jitter, Shimmer
   - NHR, HNR
   - RPDE, DFA
   - Spread measures, D2, PPE
3. Click "Predict Parkinson's"
4. Review the analysis

## 🌐 Deployment

### Deploy on Streamlit Cloud (Recommended)

1. **Push code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io/)
   - Connect your GitHub account
   - Select repository and branch
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Access your app**
   - Your app will be available at: `https://yourapp.streamlit.app/`

### Deploy on Heroku

```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.headless=true" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
heroku open
```

## 📚 Dataset Sources

1. **Diabetes Dataset**
   - Source: [Kaggle - PIMA Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
   - Instances: 768 patients
   - Features: 8 clinical measurements

2. **Heart Disease Dataset**
   - Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
   - Instances: 303 patients
   - Features: 13 cardiovascular parameters

3. **Parkinson's Dataset**
   - Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/parkinsons)
   - Instances: 195 voice recordings
   - Features: 22 vocal measurements

## ⚠️ Important Disclaimer

**This application is for educational purposes only and should NOT replace professional medical advice.**

- ❌ Not a medical diagnosis tool
- ❌ Not a substitute for doctor consultation
- ❌ Not validated for clinical use
- ✅ Educational demonstration of ML in healthcare
- ✅ Shows potential of AI in disease prediction

**Always consult qualified healthcare professionals for medical concerns.**

## 🛠️ Development

### Training Models

To train the models with your own datasets:

```bash
# Place datasets in data/ directory
# diabetes.csv, heart.csv, parkinsons.csv

# Run training script
python train_models.py
```

### Adding New Disease Models

1. Prepare dataset with features and target variable
2. Add preprocessing logic in `train_models.py`
3. Train model and save as pickle file
4. Update `app.py` with new prediction page
5. Add navigation menu item

### Customization

**Change Theme Colors:**
Edit the custom CSS in `app.py`:
```python
st.markdown("""
<style>
    .main-header {
        color: #your-color;
    }
</style>
""", unsafe_allow_html=True)
```

**Modify Prediction Logic:**
Update the risk assessment criteria in each prediction function.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/AmazingFeature
```
3. **Commit your changes**
```bash
git commit -m 'Add some AmazingFeature'
```
4. **Push to the branch**
```bash
git push origin feature/AmazingFeature
```
5. **Open a Pull Request**

### Areas for Contribution
- 🎨 UI/UX improvements
- 🤖 Additional disease models
- 📊 Better visualizations
- 📝 Documentation enhancements
- 🐛 Bug fixes
- ✨ New features

## 🐛 Troubleshooting

### Common Issues

**Issue: ModuleNotFoundError**
```bash
Solution: pip install -r requirements.txt
```

**Issue: Port already in use**
```bash
Solution: streamlit run app.py --server.port=8502
```

**Issue: Model files not found**
```bash
Solution: Run python train_models.py to generate models
```

**Issue: Streamlit won't start**
```bash
Solution: Check Python version (3.8+)
Reinstall: pip install --upgrade streamlit
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- UCI Machine Learning Repository for datasets
- scikit-learn team for the amazing ML library
- Streamlit team for the web framework
- Kaggle community for data science resources
- Medical research community for domain knowledge

## 📞 Support

Need help? Here are some resources:

- 📖 [Documentation](https://github.com/yourusername/ai-health-predictor/wiki)
- 🐛 [Report Issues](https://github.com/yourusername/ai-health-predictor/issues)
- 💬 [Discussions](https://github.com/yourusername/ai-health-predictor/discussions)
- 📧 Email: support@example.com

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] Add more disease predictions (Cancer, Kidney Disease)
- [ ] Implement deep learning models
- [ ] User authentication and history
- [ ] PDF report generation
- [ ] Mobile app development
- [ ] API for integration
- [ ] Multi-language support

### Version 3.0 (Future)
- [ ] Integration with wearable devices
- [ ] EHR system integration
- [ ] Real-time monitoring dashboard
- [ ] Telemedicine features
- [ ] AI chatbot for health queries

## 📈 Project Stats

![GitHub Stars](https://img.shields.io/github/stars/yourusername/ai-health-predictor?style=social)
![GitHub Forks](https://img.shields.io/github/forks/yourusername/ai-health-predictor?style=social)
![GitHub Issues](https://img.shields.io/github/issues/yourusername/ai-health-predictor)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/yourusername/ai-health-predictor)

---

**⭐ If you find this project helpful, please give it a star!**

**Made with ❤️ and Python**

© 2025 AI Health Predictor | Educational Machine Learning Project
# healthaipredictor
