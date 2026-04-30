# 🐳 AI-Powered Dockerfile Generator — Local LLM & Hosted LLM

A mini project that leverages the power of **Large Language Models (LLMs)** to automatically generate production-ready, best-practice Dockerfiles for any programming language — explored via two approaches: a **locally running LLM (Ollama + LLaMA 3.2)** and a **hosted LLM (Google Gemini via AI Studio)**.

---

## 📌 Project Overview

Writing Dockerfiles from scratch for different languages and frameworks can be repetitive and error-prone. This project automates that using AI — you simply provide a programming language, and the LLM generates an optimized, multi-stage Dockerfile following industry best practices.

Two distinct LLM integration strategies are demonstrated:

- **Phase 1** — Local LLM using [Ollama](https://ollama.com/) with the LLaMA 3.2 model (fully offline, no API key needed)
- **Phase 2** — Hosted LLM using Google Gemini (`gemini-flash`) via Google AI Studio API

---

## 🖥️ Phase 1 — Local LLM with Ollama + LLaMA 3.2

Run the LLM entirely on your local machine — no internet dependency, no API costs.

### 1. Install Ollama

**Windows (PowerShell):**
```powershell
irm https://ollama.com/install.ps1 | iex
```
Or download the installer directly from [ollama.com/download/windows](https://ollama.com/download/windows).

**Verify installation:**
```bash
ollama --version
```

**Start the Ollama service:**
```bash
ollama serve
```

### 2. Pull the LLaMA 3.2 Model

```bash
ollama pull llama3.2
```

This downloads the model locally. Once pulled, it runs fully offline.

---

### 3. Set Up the Python Environment

**Install Python 3.13** (or latest stable) and verify:
```bash
python --version
```

**Create and activate a virtual environment:**
```bash
# Create
python -m venv venv

# Activate (Windows CMD)
.\venv\Scripts\activate

# Activate (Git Bash / Linux)
source venv/Scripts/activate
```

### 4. Install Dependencies

The only dependency needed is the `ollama` Python package, which lets your script communicate with the locally running Ollama service.

```bash
pip3 install -r requirements.txt
```

`requirements.txt`:
```
ollama
```

### 5. Run the Script

```bash
python generate_dockerfile.py
```

You'll be prompted to enter a programming language (e.g., `python`, `groovy`, `ruby on rails`), and the LLM will generate a Dockerfile instantly.

### ✅ What the Generated Dockerfile Includes

- Official base image selection
- Dependency installation
- Working directory setup
- Source code inclusion
- Multi-stage Docker build
- Application run command
- Port exposure based on the language

### Outputs of some of the generated dockerfiles
<img width="487" height="256" alt="dockerfile-output" src="https://github.com/user-attachments/assets/2ade3ac1-dc01-4954-8a7b-60e630ec6759" />

<img width="520" height="397" alt="ollama-dockerfile-python" src="https://github.com/user-attachments/assets/e0e263ba-e7ec-4234-b3b1-8e40355be49b" />

<img width="911" height="302" alt="ruby-on-rails-dockerfile" src="https://github.com/user-attachments/assets/4e8391b5-74a7-47b1-9df8-9179a2205918" />

---

## ☁️ Phase 2 — Hosted LLM with Google Gemini (AI Studio)

Use Google's Gemini model via API for cloud-powered Dockerfile generation — useful when you want higher model capability without local hardware constraints.

### 1. Get a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Navigate to **Get API Key**
3. Copy the generated API key

### 2. Install the Gemini SDK

```bash
pip install google-generativeai
```

### 3. Configure the API Key

Set your API key in the script (or use environment variables for production):
```python
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"
```

### 4. Run the Script

```bash
python generate_dockerfile-gemini.py
```

Enter your target language when prompted. The Gemini model (`gemini-3-flash-preview`) returns a clean, ready-to-use Dockerfile.

### Output
<img width="665" height="451" alt="hosted-LLM-dockerfile" src="https://github.com/user-attachments/assets/218e1ca0-2ece-4058-be2a-dc8d660efca8" />


### ✅ What the Generated Dockerfile Includes

- Multi-stage build with clear separation of build and runtime stages
- Non-root user setup for container security
- Dependency caching using Docker layer ordering
- Environment variable configuration
- Port exposure and entry point definition

---

## 🗂️ Project Structure

```
├── venv/                          # Python virtual environment
├── requirements.txt               # Python dependencies
├── generate_dockerfile.py         # Phase 1: Ollama (local LLM) script
├── generate_dockerfile_gemini.py  # Phase 2: Gemini (hosted LLM) script
└── README.md
```

---

## ⚖️ Local LLM vs Hosted LLM — Comparison

| Feature              | Phase 1 — Ollama (Local)        | Phase 2 — Gemini (Hosted)         |
|----------------------|----------------------------------|-----------------------------------|
| Model                | LLaMA 3.2                        | gemini-3-flash-preview            |
| Internet Required    | ❌ No                            | ✅ Yes                            |
| API Key Required     | ❌ No                            | ✅ Yes                            |
| Cost                 | Free (uses local compute)        | Free tier / pay-as-you-go        |
| Setup Complexity     | Moderate (Ollama install)        | Simple (pip + API key)            |
| Output Quality       | Good                             | High                              |
| Privacy              | ✅ Fully local                   | Data sent to Google               |

---

## 💡 Key Takeaways

- **Local LLMs via Ollama** are ideal for privacy-sensitive or offline environments — no data leaves your machine.
- **Hosted LLMs via Google Gemini** offer higher quality output with minimal setup, leveraging Google's infrastructure.
- Both approaches demonstrate how LLMs can be integrated into developer tooling to automate repetitive infrastructure tasks like writing Dockerfiles.






