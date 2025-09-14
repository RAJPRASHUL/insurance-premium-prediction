Insurance Premium Prediction API
Overview
A FastAPI-based web service that predicts insurance premium categories based on various user inputs like age, BMI, lifestyle, city tier, income, and occupation.

🚀 Features
RESTful API endpoints for insurance premium predictions
Input validation using Pydantic models
CORS support for cross-origin requests
Health check monitoring
Automated API documentation
🛠️ Tech Stack
Python 3.11+
FastAPI
Scikit-learn
Pydantic
CORS middleware
📁 Project Structure
insurance-premium-prediction/
├── app.py                      # Main FastAPI application
├── requirements.txt            # Project dependencies
├── schema/
│   ├── user_input.py          # Input validation schemas
│   └── prediction_response.py  # Response schemas
└── model/
    ├── model.pkl              # Trained ML model
    └── predict.py             # Prediction logic



 Installation
Clone the repository
git clone https://github.com/yourusername/insurance-premium-prediction.git
cd insurance-premium-prediction
Create a virtual environment
python -m venv venv
.\venv\Scripts\activate
Install dependencies
pip install -r requirements.txt

🚀 Running the Application
Start the FastAPI server:
uvicorn app:app --reload

The API will be available at http://localhost:8000

📚 API Documentation
Endpoints
Home Endpoint

URL: /
Method: GET
Response: Welcome message
Health Check

URL: /health
Method: GET
Response: API status and model information
Prediction Endpoint

URL: /predict
Method: POST
Request Body:
{
    "bmi": float,
    "age_group": string,
    "lifestyle_risk": string,
    "city_tier": int,
    "income_lpa": float,
    "occupation": string
}

Response:
{
    "response": {
        "predicted_category": string,
        "confidence": float
    }
}

📖 Interactive API Documentation
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
🧪 Testing
To run tests:

🔒 Environment Variables
No environment variables are required for basic setup.

🤝 Contributing
Fork the repository
Create a new branch (git checkout -b feature/awesome-feature)
Commit your changes (git commit -m 'Add awesome feature')
Push to the branch (git push origin feature/awesome-feature)
Create a Pull Request

👥 Authors
Your Name (@RAJPRASHUL)
