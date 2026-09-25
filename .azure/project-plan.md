# Project Plan

**Status**: Approved
**Created**: 2026-09-25
**Mode**: NEW

---

## 1. Project Overview

**Goal**: Build a Python NLP text categorization project that reads labeled text samples, preprocesses them with NLTK, trains a classifier, and predicts the category of new text in a repeatable, PyCharm-friendly workflow. The project is designed so that every module is independently testable.

**App Type**: Background worker

**API Login**: No

**Mode**: NEW

**Deployment Plan**: No deployment plan found

---

## 2. NLP Text Categorizer — worker

| Component | Technology |
|-----------|-----------|
| **Language** | Python |
| **Runtime** | CPython |
| **Package Manager** | pip |
| **Test Runner** | pytest |
| **Mocking Library** | unittest.mock |
| **Test Command** | pytest |
| **Orchestration** | docker-compose |

> **Language vs Runtime**: `Language` is the source language the user picked in this service's `language` question. `Runtime` is the execution runtime — default `Node` for TypeScript/JavaScript, `CPython` for Python, `.NET` for C#. Only deviate from the default (e.g. `Bun`, `Deno`, `PyPy`) when the user explicitly asks. **Package Manager and Test Runner are language-dependent** — match them to this service's Language (e.g. C# → `dotnet (NuGet)` + `xUnit`/`NUnit`/`MSTest`). The `Orchestration` row is recorded for the scaffold step but hidden in the plan UI — always keep it set to `docker-compose`.

---

## 3. Services Required

| Azure Service | Role in App | Environment Variable | Default Value (Local) | Classification |
|---------------|------------|---------------------|----------------------|----------------|
| Azure Functions | Optional future cloud execution target for the categorizer if the workflow is later deployed outside PyCharm | AZURE_FUNCTIONS_ENVIRONMENT | local | Optional |

---

## 4. Prerequisites

Identify the required tools, then inventory them by following [prerequisites.md](../shared-references/prerequisites.md). Always produce **both** groups — `### Run` and `### Debug` — as two sub-tables under this section. The plan webview shows the Run group always and the Debug group only when the user turns on the Autopilot toggle, so do not omit either group yourself.

### Run

| Tool | Service(s) | Installed | Version |
|------|------------|-----------|---------|
| Python | NLP Text Categorizer | ✅ | 3.14.5 |
| pip | NLP Text Categorizer | ✅ | 26.2.1 |
| NLTK | NLP Text Categorizer | ✅ | 3.10.3 |
| scikit-learn | NLP Text Categorizer | ✅ | 1.9.1 |
| pytest | NLP Text Categorizer | ❓ | not confirmed |

### Debug

| Tool | Service(s) | Installed | Version |
|------|------------|-----------|---------|
| Docker Compose | NLP Text Categorizer | ✅ | docker CLI 29.1.3 |
| VS Code Python extension | NLP Text Categorizer | ✅ | installed |
| Python Debugger (debugpy) | NLP Text Categorizer | ✅ | installed |
| Pylance | NLP Text Categorizer | ✅ | installed |

---

## 5. Project Structure

```
folder_gol/
├─ .azure/
│  └─ project-plan.md
├─ data/
│  ├─ samples/
│  └─ labels/
├─ src/
│  ├─ __init__.py
│  ├─ preprocess.py
│  ├─ features.py
│  ├─ train.py
│  ├─ predict.py
│  └─ evaluate.py
├─ tests/
│  ├─ test_preprocess.py
│  ├─ test_features.py
│  └─ test_model.py
├─ main.py
├─ requirements.txt
├─ README.md
└─ .gitignore
```

---

## 6. Route Definitions

| # | Method | Path | Description | Request Body | Response Body | Status Codes |
|---|--------|------|-------------|-------------|--------------|-------------|
| 1 | GET | `/api/health` | Health check for the NLP worker | — | `{ status, services }` | 200, 503 |
| 2 | POST | `/api/classify` | Classify a text sample into a known category | `{ text, labels? }` | `{ category, confidence, model_version }` | 200, 400, 500 |

---

## 7. Next Steps

1. Run **azure-project-scaffold** to execute this plan
2. Run **azure-project-integrate** to wire the frontend to live data, smoke-test the backend, and create the migrations
3. Run **azure-debug-plan** → **azure-debug-generate** for Docker emulators and VS Code debugging
4. Run the **azure-deploy** agent when ready; it uses **azure-app-onboard** for architecture, cost estimation, IaC generation, provisioning, and health verification
