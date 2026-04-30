# 🤖 AIOps Projects — Overview

A collection of hands-on **AIOps (Artificial Intelligence for IT Operations)** mini projects exploring how AI and ML can be applied to real-world DevOps and operations challenges — from intelligent log monitoring to automated infrastructure generation.

---

## 📂 Projects at a Glance

| # | Project | Key Tech |
|---|---------|----------|
| 1 | Log Analysis: Traditional vs ML-Based | Python, Pandas, Scikit-learn (Isolation Forest) |
| 2 | AI-Powered Dockerfile Generator | Ollama (LLaMA 3.2), Google Gemini API |

---

## 📁 AIOps-1 — Log Analysis: Traditional Python vs ML-Based Anomaly Detection

### 📌 Description

Log files are the heartbeat of any running system — but manually scanning them for issues is inefficient and unscalable. This project tackles that problem by implementing and comparing **two log analysis approaches** on a sample log file containing `INFO`, `WARNING`, `ERROR`, and `CRITICAL` level entries.

**Phase 1** uses a straightforward rule-based Python script with **Pandas** to parse logs, filter by severity, and surface anomalies based on predefined conditions.

**Phase 2** elevates this by applying an unsupervised ML algorithm — **Isolation Forest** (via Scikit-learn) — which encodes log severity as numeric values and automatically detects anomalous patterns in the data, going beyond simple keyword matching.

### 🔗 [View Project →](https://github.com/Saahiti-Korlam/AIOps-projects/tree/main/AIOps-1)

### ✅ Conclusion

This project demonstrates a clear evolution from static, rule-driven log monitoring to dynamic, data-driven anomaly detection. While the traditional approach is simple and interpretable, the ML-based approach adapts to patterns in data and catches anomalies that rigid rules might miss — making it far more suitable for production-grade AIOps pipelines.

---

## 📁 AIOps-2 — AI-Powered Dockerfile Generator (Local LLM & Hosted LLM)

### 📌 Description

Writing optimized Dockerfiles for different tech stacks requires expertise and is often repetitive. This project uses **Large Language Models (LLMs)** to automate Dockerfile generation — you provide a programming language, and the AI produces a production-ready, multi-stage Dockerfile following best practices.

Two LLM integration strategies are explored side by side:

**Phase 1** runs a **local LLM** using [Ollama](https://ollama.com/) with the **LLaMA 3.2** model — fully offline, no API key, no data leaving your machine. Ideal for privacy-conscious or air-gapped environments.

**Phase 2** integrates a **hosted LLM** — **Google Gemini** (`gemini-flash`) via Google AI Studio — delivering higher output quality with minimal setup using a simple API key.

### 🔗 [View Project →](https://github.com/Saahiti-Korlam/AIOps-projects/tree/main/AIOps-2)

### ✅ Conclusion

This project highlights how LLMs — whether running locally or in the cloud — can be seamlessly embedded into developer workflows to automate infrastructure tasks. The dual-approach design makes it a practical reference for anyone evaluating the trade-offs between local and hosted AI: privacy and control vs. convenience and quality.

---

## 💡 Overall Takeaway

These projects together reflect a core AIOps principle — **replacing manual, reactive operations with intelligent, proactive automation**. Whether it's detecting log anomalies before they escalate or generating container configurations on demand, AI brings both speed and adaptability to modern IT operations.

---

> 🛠️ Built with Python · Pandas · Scikit-learn · Ollama · LLaMA 3.2 · Google Gemini API
