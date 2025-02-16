from helpers import generate_combinations
import nand_components as nc
from prompt_toolkit import PromptSession
from rich.console import Console
from rich.panel import Panel

console = Console()
session = PromptSession()

def binary_string_to_list(binary_str: str) -> list[int]:
    return [int(bit) for bit in binary_str]

def print_help(component_name: str = None):
    if component_name:
        help_message = f"""
        [bold cyan]--- Help: Using '{component_name}' Component ---[/bold cyan]
        [green]Commands:[/green]
          • [yellow]back[/yellow]   - Return to component selection
          • [yellow]help[/yellow]   - Show this help message
          • [yellow]<binary string>[/yellow] - Enter a valid binary input to compute the output
        """
    else:
        help_message = """
        [bold cyan]--- Help: Main Menu ---[/bold cyan]
        [green]Commands:[/green]
          • [yellow]exit[/yellow]   - Quit the program
          • [yellow]help[/yellow]   - Show this help message
          • [yellow]<component name>[/yellow] - Select a component to start computing (e.g., 'not', 'and', 'or')
        """
    console.print(Panel(help_message, expand=False))

def main():
    components = {
        "not": nc.Not(),
        "and": nc.And(),
        "or": nc.Or()
    }

    console.print("[bold magenta]Welcome to the NAND-based Component Simulator![/bold magenta]")
    console.print(f"[cyan]Available components:[/cyan] {', '.join(components.keys())}\n")

    while True:
        try:
            component_name = session.prompt("> ").strip().lower()

            if component_name == "exit":
                console.print("[bold green]Goodbye![/bold green]")
                break

            if component_name not in components:
                console.print(f"[bold red]Invalid component.[/bold red] Choose from: {', '.join(components.keys())}")
                continue

            component = components[component_name]

            while True:
                input_str = session.prompt(f"{component_name} > ").strip()

                if input_str.lower() == "back":
                    console.print("\n[bold yellow]Returning to component selection...[/bold yellow]")
                    break

                if input_str.lower() == "help":
                    print_help(component_name)
                    continue

                if input_str.lower() == "exit":
                    console.print("[bold green]Goodbye![/bold green]")
                    return

                if len(input_str) != component.num_inputs or not set(input_str).issubset({"0", "1"}):
                    console.print(f"[bold red]Invalid input.[/bold red] You must enter a {component.num_inputs}-bit binary string.")
                    continue

                inputs = binary_string_to_list(input_str)
                output = component.compute(inputs)
                output_str = "".join(map(str, output))

                console.print(f"[bold green]Output: {output_str}[/bold green]")
                console.print(f"[bold cyan]NAND gates used: {nc.nand_count}[/bold cyan]\n")

                nc.nand_count = 0

        except KeyboardInterrupt:
            console.print("\n[bold red]Exiting...[/bold red]")
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
