# Financial Market Anomaly Detection and Investment Strategy Chatbot

This project focuses on detecting anomalies in financial markets using the **XGBoost** model and implementing a robust investment strategy based on the detected anomalies. Additionally, a **chatbot interface** has been developed to provide real-time insights and assist users in making informed investment decisions.

---

## Features

### 1. **Anomaly Detection**
- Utilizes historical financial market data.
- Employs the XGBoost model to detect anomalies that may signal potential market crashes or irregularities.
- Key indicators such as moving averages, price ratios, and volatility are calculated to enhance feature engineering.

### 2. **Investment Strategy**
- Implements a trading strategy that generates **Buy**, **Sell**, or **Hold** recommendations.
- Leverages market indicators like price, moving averages, and anomaly detection results.
- Strategy performance is evaluated using backtesting on historical data.

### 3. **Chatbot Interface**
- Interactive chatbot built using **Flask** to provide real-time insights.
- Responds to user queries about the current strategy, anomalies, and market conditions.
- User-friendly interface with features such as avatars, message formatting, and auto-scrolling.

---

## Project Workflow

### **Step 1: Data Preparation**
- Process raw financial data (e.g., market indices, volatility).
- Compute indicators:
  - Moving averages (e.g., 7-day VIX moving average).
  - Price differences and ratios.
- Clean and prepare the dataset for anomaly detection.

### **Step 2: Model Training**
- Train the XGBoost model to detect anomalies based on market patterns.
- Address class imbalance using weighted loss functions.
- Evaluate model performance using metrics like precision, recall, and F1-score.

### **Step 3: Investment Strategy Implementation**
- Develop a strategy that:
  - Buys when anomalies and favorable conditions are detected.
  - Sells when profit thresholds or risk conditions are met.
  - Holds during periods of uncertainty or weekends.
- Simulate strategy performance using backtesting.

### **Step 4: Chatbot Development**
- Build a chatbot interface using **Flask** to interact with users.
- Features:
  - Query market conditions and strategies.
  - Display anomalies and provide actionable insights.
  - Modern, responsive UI with Bootstrap styling.

---


