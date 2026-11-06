import asyncio
import os
# Fix Git error before importing agents
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

from core.manager_agent import jarvis_app
from core.config import config

from agents.web_agent import web_agent
from agents.pc_agent import pc_agent
from agents.file_agent import file_agent
from agents.code_agent import code_agent
from agents.blender_agent import blender_agent
from agents.voice_agent import voice_agent
from agents.self_improve_agent import self_improve_agent

# Colors for a better chat experience
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

async def main():
    # Clear screen for clean start
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{Colors.OKCYAN}{Colors.BOLD}" + "="*60)
    print("       🚀 JARVIS AI - TERMINAL INTERFACE v1.0 🚀")
    print("       Connected to: Rishabh | Brain: Llama 3.1 8B")
    print("="*60 + f"{Colors.ENDC}")
    print(f"{Colors.OKGREEN}System: Online | Memory: Active | Agents: Ready{Colors.ENDC}")
    print(f"{Colors.OKCYAN}Type 'exit' to shutdown or 'help' for commands.{Colors.ENDC}\n")

    chat_history = []

    while True:
        try:
            # Chat-style input
            user_input = input(f"{Colors.BOLD}👤 Rishabh{Colors.ENDC}: ")
            
            if not user_input.strip():
                continue

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"\n{Colors.OKBLUE}🤖 JARVIS: Shutting down systems. Goodbye, bhai!{Colors.ENDC}")
                break

            if user_input.lower() == 'help':
                print(f"\n{Colors.WARNING}Available Commands:{Colors.ENDC}")
                print("- 'clear': Clear the chat screen")
                print("- 'status': Check system health")
                print("- 'exit': Close JARVIS")
                continue

            if user_input.lower() == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Colors.OKCYAN}Screen cleared, bhai!{Colors.ENDC}")
                continue

            print(f"\n{Colors.OKCYAN}🤖 JARVIS{Colors.ENDC}: {Colors.BOLD}Thinking...{Colors.ENDC}", end="\r")
            
            # Process input through LangGraph
            inputs = {"input": user_input, "agent_results": []}
            result = await jarvis_app.ainvoke(inputs)
            final_response = result.get("final_response", "I couldn't process that, bhai.")

            # Chat-like output
            print(f"\n{Colors.OKCYAN}🤖 JARVIS{Colors.ENDC}: {final_response}")
            
            # Keep a simple history in memory
            chat_history.append({"user": user_input, "jarvis": final_response})

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n{Colors.FAIL}❌ System Error: {str(e)}{Colors.ENDC}")

if __name__ == "__main__":
    asyncio.run(main())
