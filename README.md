# JARVIS AI - The Ultimate Multi-Agent System

## 🚀 System Overview
JARVIS is a production-ready multi-agent AI system that combines local LLM power (Llama 3.1 8B) with cloud-based agility. It controls your PC, generates 3D assets in Blender, manages your files, and learns from the web autonomously.

## 🛠 Tech Stack
- **Brain**: Ollama (Llama 3.1 8B)
- **Orchestration**: LangGraph
- **Memory**: Supabase (pgvector)
- **Voice**: Groq Whisper (STT) + Edge TTS (TTS) + Porcupine (Wake Word)
- **Frontend**: React + Three.js + TailwindCSS
- **Backend**: FastAPI + WebSockets + Ngrok

## 📦 Setup Instructions

### 1. Prerequisites
- Install [Ollama](https://ollama.ai/) and run `ollama run llama3.1:8b`.
- Install [Blender](https://www.blender.org/).
- Create a [Supabase](https://supabase.com/) project.
- Get API keys for [Groq](https://groq.com/) and [Picovoice](https://picovoice.ai/).

### 2. Configuration
1. Copy `.env.example` to `.env`.
2. Fill in all API keys and paths (especially `BLENDER_PATH`).
3. Run the SQL script in `JARVIS/memory/supabase_setup.sql` inside your Supabase SQL Editor.

### 3. Installation
```bash
pip install -r requirements.txt
```

### 4. Running the System
1. **Start Backend**:
   ```bash
   python JARVIS/ui/backend/main.py
   ```
2. **Start Frontend**:
   ```bash
   cd JARVIS/ui/frontend
   npm install
   npm start
   ```

## 🤖 Agent Capabilities
- **Manager**: Routes tasks to specialized agents.
- **Web**: Searches web, GitHub, and scrapes content.
- **PC**: Controls windows, volume, and executes system commands.
- **Blender**: Generates AAA 3D models and PBR materials.
- **Code**: Writes, tests, and integrates new features into itself.
- **File**: Searches and analyzes PDFs, Excel, and Word files.
- **Voice**: "Hey JARVIS" wake-word activation.
- **Self-Improvement**: Autonomously adds tools and features.
