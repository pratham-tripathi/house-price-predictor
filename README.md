# house-price-predictor

## 🏠 Real Estate Intelligence Engine
### AI-Powered Property Valuation Tool
The Real Estate Intelligence Engine is a high-precision machine learning application designed to estimate residential property values. By leveraging historical data and a robust preprocessing pipeline, this tool provides instant market valuations based on key structural and contextual features.

## 🚀 Live Deployment
Experience the engine in action here:
👉 https://prathamt-house-price-predictor.hf.space

## 🛠️ Technical Architecture
This project implements an end-to-end Machine Learning lifecycle:
 * Data Preprocessing: Uses ColumnTransformer to apply OneHotEncoder on categorical variables (Location, Condition, Garage) while passing through numerical data.
 * Modeling: Implements a Linear Regression algorithm to identify correlations between house features and market prices.
 * Pipeline Integration: Encapsulates the entire workflow into a scikit-learn Pipeline to ensure data consistency between training and real-time inference.
 * Interface: A custom-styled Gradio web interface deployed on the cloud.

## 📂 Repository Structure
 * app.py: The core application script containing the UI layout and prediction logic.
 * house_model.pkl: The serialized (saved) trained model ready for production.
 * requirements.txt: List of Python dependencies required to run the engine.
 * README.md: Project documentation and overview.

## 📖 How to Use
 * Input Specs: Provide total area, number of rooms, and the year of construction.
 * Set Context: Choose the location type (Urban/Suburban/Rural) and the building's current condition.
 * Analyze: Click the "Calculate Valuation" button.
 * Result: The AI will display the estimated market value based on its learned patterns.

##👨‍💻 Submission Details
 * Developer: Pratham Tripathi
 * Course: Foundation of AI Technology
 * Batch: AT-01
