# 🔍 Log Analysis: Traditional Python vs ML-Based Anomaly Detection

A two-phase project that demonstrates log file analysis using a **traditional Python scripting approach** and an **AI/ML-based approach** using the Isolation Forest algorithm — both aimed at identifying anomalies and patterns in application log data.

---

## 📌 Project Overview

Log monitoring is critical in any production system. This project compares two methodologies for parsing and analyzing log files:

- **Phase 1** — Rule-based log parsing using Python and Pandas
- **Phase 2** — Intelligent anomaly detection using Scikit-learn's Isolation Forest algorithm

Both phases operate on a sample log file containing `INFO`, `WARNING`, `ERROR`, and `CRITICAL` level entries.

---

## 🚀 Phase 1 — Traditional Log Analysis (Python + Pandas)

A straightforward script-based approach to read, parse, and summarize log files.

### Steps

**1. Set Up a Virtual Environment**

Isolate project dependencies by creating and activating a Python virtual environment.

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows CMD)
.\venv\Scripts\activate

# Activate (Git Bash / Linux)
source venv/Scripts/activate
```

**2. Install Dependencies**

```bash
pip install pandas
```

**3. Run the Script**

```bash
simple_log_analysis.py
```

### ✅ Output

- Parsed log entries displayed in a structured format
- Anomalies (e.g., ERROR/WARNING entries) listed and flagged for review

---
<img width="568" height="239" alt="simple-log" src="https://github.com/user-attachments/assets/7652107d-a26f-4768-a6d2-b28bf87b21a9" />


## 🤖 Phase 2 — ML-Based Log Analysis (Isolation Forest)

An AI-powered approach that assigns numeric severity levels to log entries and uses unsupervised machine learning to detect anomalies automatically.

### Algorithm Used: **Isolation Forest**

> Isolation Forest is an unsupervised anomaly detection algorithm that isolates observations by randomly selecting a feature and a split value — anomalies are isolated faster and thus have shorter paths in the tree.

### Log Severity Mapping

| Log Level | Numeric Value |
|-----------|--------------|
| INFO      | 1            |
| WARNING   | 2            |
| ERROR     | 3            |
| CRITICAL  | 4            |

### Steps

**1. Install Dependencies**

```bash
pip install scikit-learn
```

**2. Run the Script**

```bash
aiops_log_analysis.py
```

### ✅ Output

- Log entries parsed and encoded with severity levels
- Anomalies detected and listed with their corresponding log levels
- ML model flags unusual patterns beyond simple rule-matching

---
<img width="890" height="196" alt="ai-logs" src="https://github.com/user-attachments/assets/050e70f1-3f33-4a81-86e6-572f88af8e99" />


## 🗂️ Project Structure

```
├── venv/                    # Python virtual environment
├── sample_logs.log          # Input log file (INFO, WARN, ERROR, CRITICAL)
├── simple_log_analysis.py   # Phase 1: Traditional analysis script
├── ai_log_analysis.py       # Phase 2: ML-based analysis script
└── README.md
```

---

## 🛠️ Requirements

- Python 3.x
- pandas
- scikit-learn

---

## 💡 Key Takeaways

| Feature                  | Phase 1 (Traditional) | Phase 2 (ML-Based)        |
|--------------------------|----------------------|---------------------------|
| Approach                 | Rule-based filtering | Unsupervised ML (Isolation Forest) |
| Anomaly Detection        | Keyword/level match  | Pattern-based, data-driven |
| Flexibility              | Limited              | Adapts to data patterns   |
| Setup Complexity         | Simple               | Moderate                  |

