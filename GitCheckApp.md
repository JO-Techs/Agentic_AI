#  Auto Code Reviewer – AI-Powered GitHub PR Review Bot

## 🔹 Project Overview
This AI-powered GitHub bot **automatically reviews pull requests**, analyzes code changes, and suggests improvements based on best practices, security vulnerabilities, and coding standards.

##  Features
- 🔹 **Automatic PR Review**: Fetches pull requests and analyzes code changes.
- 🔹 **AI-Powered Suggestions**: Uses GPT-4 to provide code quality insights.
- 🔹 **Security & Best Practices Check**: Identifies vulnerabilities and optimizations.
- 🔹 **GitHub Integration**: Posts comments directly on PRs using GitHub API.

---

##  Tech Stack
| Component       | Technology |
|----------------|------------|
| **Backend**    | Python (Flask/FastAPI) |
| **AI Model**   | GPT-4 (OpenAI API) / Code Llama |
| **GitHub API** | REST API / GraphQL |
| **Automation** | LangChain, Webhooks |

---

## 📍 Roadmap

### **1️⃣ Project Setup**
- [ ] Create a **GitHub App** and get API credentials.
- [ ] Enable **Pull Request Read & Write permissions**.
- [ ] Install dependencies:  
  ```bash
  pip install flask github openai langchain
