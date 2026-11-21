
import os
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

# --------------------------------------------------
# 1. PATHS & CONFIGURATION
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent
ENV_FILE = ROOT_DIR / ".env"

load_dotenv(ENV_FILE)

AI_NAME = os.getenv("AI_NAME", "Architecture AI")
LANGUAGE = os.getenv("LANGUAGE", "Persian")
PROJECT_ROOT = os.getenv("PROJECT_ROOT", str(ROOT_DIR))

console = Console()


# --------------------------------------------------
# 2. AI CORE
# --------------------------------------------------

class ArchitectureAI:

    def __init__(self):
        self.name = AI_NAME
        self.language = LANGUAGE
        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.client = None

        self.roles = {
            "architect": "Architect and Design Specialist",
            "critic": "Architecture Professor and Design Critic",
            "researcher": "Architectural Researcher",
            "project_manager": "Project Manager",
            "presentation": "Presentation Specialist",
        }

        self.memory = []

    def initialize(self):
        console.print(
            Panel(
                f"[bold cyan]{self.name}[/bold cyan]\n"
                "Architecture AI Core",
                title="AI SYSTEM",
                border_style="cyan",
            )
        )

        console.print(f"Language: {self.language}")
        console.print(f"Project root: {PROJECT_ROOT}")
        console.print(f"Available roles: {len(self.roles)}")

        if self.api_key:
            console.print("[green]API key detected.[/green]")
        else:
            console.print(
                "[yellow]API key not configured yet.[/yellow]"
            )

        console.print("[green]Core initialized successfully.[/green]")

    def show_roles(self):
        console.print("\n[bold]AI Specialist Roles[/bold]")

        for role, description in self.roles.items():
            console.print(f"- {role}: {description}")

    def run(self):
        self.initialize()
        self.show_roles()

        console.print(
            "\n[bold cyan]System is ready for the next development stage.[/bold cyan]"
        )


# --------------------------------------------------
# 3. START SYSTEM
# --------------------------------------------------

if __name__ == "__main__":
    agent = ArchitectureAI()
    agent.run()
