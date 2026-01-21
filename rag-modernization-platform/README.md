# RAG‑Based QA Evaluation Framework for Legacy Codebases

A production‑grade **Retrieval‑Augmented Generation (RAG) + Question–Answering (QA) Evaluation Platform** designed to measure and improve AI assistant accuracy over large legacy codebases such as **ERPNext** and **Bahmni**.

This project enables developers to:

* Ask **natural‑language questions directly on a codebase** (VS Code Extension)
* Retrieve **high‑quality, structured context** from legacy systems
* **Objectively evaluate** AI answers using **RAGAs + custom modernization metrics**
* Track improvements with **MLflow experiments**
* Visualize results through a **Streamlit dashboard**

---

## Why This Project Exists

Modernization tools often fail silently: they *seem* useful but provide no proof of accuracy.

This framework answers the core question:

> **Does providing extracted code context actually improve AI answers about legacy systems?**

By combining **RAG evaluation**, **human‑in‑the‑loop scoring**, and **experiment tracking**, this project turns subjective AI quality into **measurable engineering metrics**.

---

## Key Features

* **VS Code Extension** – Ask questions like:

  * "What happens when a Sales Invoice is submitted?"
  * "Where is discount logic implemented?"

* **Hybrid RAG Retrieval**

  * Vector search (embeddings)
  * BM25 keyword search
  * Optional graph‑based reranking

* **Context‑Aware Answering**

  * File‑level, function‑level, and workflow context
  * ERPNext/Bahmni business‑logic aware

* **QA Evaluation with RAGAs**

  * Faithfulness
  * Answer relevancy
  * Context precision
  * Context recall

* **Custom Modernization Metrics**

  * Validation completeness
  * Workflow tracing success
  * Business logic findability
  * Relation accuracy

* **Experiment Tracking**

  * MLflow runs for embeddings, chunking, retrieval strategy
  * Compare baseline vs with‑context performance

* **Streamlit Dashboard**

  * QA chat
  * Experiment comparison
  * Metric visualization

---

## High‑Level Architecture

```
VS Code Extension / Streamlit UI
            │
            ▼
     FastAPI RAG Backend
            │
   ┌────────┼─────────┐
   ▼        ▼         ▼
Indexing  Retrieval  LLM Adapter
(AST)     (Hybrid)   (Claude/Gemini)
   │        │         │
   └────────▼─────────┘
        Context Builder
                │
                ▼
        RAGAs QA Evaluation
                │
                ▼
           MLflow Tracking
```

---

## Repository Structure

```
rag-modernization-platform/
│
├── backend/                 # Core RAG + QA system
│   ├── api/                 # FastAPI routes
│   ├── indexing/            # AST parsing, symbol extraction
│   ├── retriever/           # Vector + BM25 + hybrid retrieval
│   ├── rag/                 # Context building + LLM calls
│   ├── evaluation/          # RAGAs + modernization metrics
│   ├── experiments/         # MLflow logging
│   └── config/
│
├── vscode-extension/        # Developer-facing VS Code plugin
│
├── streamlit-app/           # QA & evaluation dashboard
│
├── data/                    # Codebases, embeddings, results
│
└── README.md
```

---

## Installation

### Prerequisites

* Python 3.9+
* Node.js 18+
* VS Code
* MLflow

---

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn api.main:app --reload
```

Backend runs at: `http://localhost:8000`

---

### Streamlit App

```bash
cd streamlit-app
streamlit run app.py
```

Dashboard runs at: `http://localhost:8501`

---

### VS Code Extension

```bash
cd vscode-extension
npm install
npm run build
```

Press `F5` to launch Extension Development Host.

---

## Usage

### 1. Index a Codebase

```bash
POST /index
{
  "path": "data/codebases/erpnext"
}
```

---

### 2. Ask a Question

From:

* VS Code command palette, or
* Streamlit UI

Example:

```
What happens when a Sales Invoice is submitted?
```

---

### 3. Run QA Evaluation

* Baseline (no context)
* With extracted context

Metrics computed:

* Faithfulness
* Answer relevancy
* Context precision
* Context recall

Results logged to **MLflow**.

---

## Experiment Design (Aligned with Research)

Each experiment follows:

1. Ask question without context
2. Ask same question with context
3. Score accuracy & completeness
4. Compute delta
5. Log results

Target success criteria:

* Average accuracy delta ≥ **+1.5**
* ≥ **70%** questions improved
* ≤ **5%** regressions

---

## Example Test Case (YAML)

```yaml
question: "How is discount calculated?"
expected_files:
  - DiscountController
  - PricingRule
expected_concepts:
  - item-level discount
  - invoice-level discount
```

---

## Intended Use Cases

* Legacy system modernization
* ERP / HIS migration planning
* AI‑assisted code understanding
* Internship / academic evaluation projects
* Enterprise RAG validation (IBM, consulting)

---

## Roadmap

* MCP server for Claude Code
* Graph‑aware retrieval (PageRank)
* CI gate for RAG quality regressions
* Migration readiness scoring
* Multi‑language support (Java, PHP, Python)

---

## Disclaimer

This project is designed for **engineering validation and research**. It does not replace human code reviews or architectural decisions.

---

## License

MIT License

---

## Author

Built for **AI‑driven legacy modernization and evaluation workflows**.
