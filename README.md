🛡 AI Zero-Day Cyber Attack Detection System

Real-time detection of suspicious network activity using Artificial Intelligence and Machine Learning.

This project captures live network packets, analyzes them using an AI model, and visualizes results on a real-time cybersecurity dashboard.

📌 Table of Contents

<a href="#overview">Overview</a>

<a href="#problem-statement">Problem Statement</a>

<a href="#system-architecture">System Architecture</a>

<a href="#dataset--data-source">Dataset / Data Source</a>

<a href="#tools--technologies">Tools & Technologies</a>

<a href="#project-structure">Project Structure</a>

<a href="#how-the-system-works">How the System Works</a>

<a href="#ai-model-development">AI Model Development</a>

<a href="#dashboard-features">Dashboard Features</a>

<a href="#results--output">Results / Output</a>

<a href="#how-to-run-this-project">How to Run This Project</a>

<a href="#future-improvements">Future Improvements</a>

<a href="#author--contact">Author & Contact</a>

<h2><a class="anchor" id="overview"></a>Overview</h2>

Cyber attacks are increasing rapidly, and traditional rule-based security systems struggle to detect unknown or zero-day attacks.

This project builds an AI-based intrusion detection system that:

• Captures live network traffic
• Extracts packet features
• Uses a machine learning model to detect anomalies
• Displays results in a real-time security dashboard

The system helps simulate how modern Security Operations Centers (SOC) monitor networks.

<h2><a class="anchor" id="problem-statement"></a>Problem Statement</h2>

Organizations face thousands of network events every second.

Key challenges include:

• Detecting unknown cyber attacks
• Monitoring real-time network traffic
• Identifying suspicious IP behavior
• Visualizing attacks for security analysts

Manual monitoring is inefficient.

This project automates detection using machine learning-based anomaly detection.

<h2><a class="anchor" id="system-architecture"></a>System Architecture</h2>

System workflow:

Network Traffic
      │
      ▼
Packet Capture (Scapy)
      │
      ▼
Feature Extraction
      │
      ▼
AI Detection Model
      │
      ▼
Attack Logs (CSV)
      │
      ▼
Real-Time Dashboard (Streamlit)

The system continuously analyzes incoming packets and updates the dashboard automatically.

<h2><a class="anchor" id="dataset--data-source"></a>Dataset / Data Source</h2>

Training Dataset:

CICIDS2017 Cybersecurity Dataset

Contains labeled network traffic including:

• Normal traffic
• DDoS attacks
• Port scanning
• Botnet traffic

Dataset used for training the machine learning model.

Dataset not uploaded due to large size.

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

Python

Core programming language

Pandas & NumPy

Data preprocessing and feature handling

Scapy

Real-time packet capture

Streamlit

Interactive dashboard

Scikit-learn

Machine learning model training

Matplotlib

Traffic visualization

Joblib

Model saving and loading

GitHub

Version control and project hosting

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>
AI-ZeroDay-Detection/
│
├── detection_engine.py
│
├── dashboard.py
│
├── train_model.py
│
├── packet_capture.py
│
├── cyber_attack_model.pkl
│
├── attack_logs.csv
│
├── dataset/
│   └── cicids_dataset.csv
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
<h2><a class="anchor" id="how-the-system-works"></a>How the System Works</h2>

1️⃣ Network packets are captured using Scapy

2️⃣ Important packet features are extracted such as:

• Packet length
• Protocol type
• Flow characteristics

3️⃣ Features are passed to the trained AI model

4️⃣ The model predicts:

Normal Traffic
Suspicious Traffic

5️⃣ Results are logged and visualized in the dashboard.

<h2><a class="anchor" id="ai-model-development"></a>AI Model Development</h2>

Problem Type:

Anomaly Detection / Classification

Machine Learning Model Used:

Random Forest Classifier

Feature Engineering:

• Packet length
• Protocol type
• Traffic statistics

Training Method:

Train-Test Split (80/20)

Model saved using:

Joblib

<h2><a class="anchor" id="dashboard-features"></a>Dashboard Features</h2>

The cybersecurity dashboard provides real-time monitoring.

Features include:

📊 Traffic statistics

• Total packets
• Normal traffic
• Suspicious traffic

📈 Traffic analytics

• Packet size trends
• Attack distribution

📄 Network logs

• Recent packet activity
• Suspicious IP detection

🌍 Global attack map

Shows geographical location of suspicious IP addresses.

🔄 Auto refresh every few seconds for real-time monitoring.

<h2><a class="anchor" id="results--output"></a>Results / Output</h2>

Example detection output:

⚠ Suspicious Traffic Detected
Source: 192.178.211.103 → Destination: 10.109.209.172

Dashboard shows:

• Live traffic monitoring
• Suspicious IP alerts
• Traffic graphs

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

Clone the repository:

git clone https://github.com/Nityanand-Khule-24/AI-ZeroDay-Detection.git

Navigate to project folder:

cd AI-ZeroDay-Detection

Install dependencies:

pip install -r requirements.txt

Run the detection engine:

python detection_engine.py

Start the dashboard:

streamlit run dashboard.py

Open browser:

http://localhost:8501
<h2><a class="anchor" id="future-improvements"></a>Future Improvements</h2>

Possible improvements:

• Deep learning based intrusion detection
• Attack type classification (DDoS / Botnet / Port Scan)
• Automatic attacker IP blocking
• Integration with SIEM systems
• Advanced real-time analytics
• 3D cyber attack visualization dashboard

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

Nityanand Khule

Artificial Intelligence & Machine Learning Student
Savitribai Phule Pune University

📧 nityanandkhule24@gmail.com

🔗 LinkedIn
https://www.linkedin.com/in/nityanand-khule/