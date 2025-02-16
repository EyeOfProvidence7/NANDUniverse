from helpers import generate_combinations
import nand_components as nc
import shutil

def binary_string_to_list(binary_str: str) -> list[int]:
    return [int(bit) for bit in binary_str]

def print_help(component_name: str = None):
    if component_name:
        print(f"\n--- Help: Using '{component_name}' Component ---")
        print("Commands:")
        print("  back   - Return to component selection")
        print("  help   - Show this help message")
        print("  <binary string> - Enter a valid binary input to compute the output\n")
    else:
        print("\n--- Help: Main Menu ---")
        print("Commands:")
        print("  exit   - Quit the program")
        print("  help   - Show this help message")
        print("  <component name> - Select a component to start computing (e.g., 'not', 'and', 'or')\n")

def main():
    components = {
        "not": nc.Not(),
        "and": nc.And(),
        "or": nc.Or()
    }

    print("Welcome to the NAND-based Component Simulator!")
    print(f"Available components: {', '.join(components.keys())}")

    while True:
        try:
            component_name = input("\nEnter the component (or 'exit' to quit): ").strip().lower()
            if component_name == "exit":
                print("Goodbye!")
                break

            if component_name not in components:
                print(f"Invalid component. Choose from: {', '.join(components.keys())}")
                continue

            component = components[component_name]
            print(f"\nYou selected the '{component_name}' component. Type 'back' to choose another component.\n")

            while True:
                input_str = input(f"{component_name}: ").strip()

                if input_str.lower() == "back":
                    print("\nReturning to component selection...")
                    break

                if input_str.lower() == "help":
                    print_help(component_name)
                    continue

                if input_str.lower() == "exit":
                    print("Goodbye!")
                    return

                if len(input_str) != component.num_inputs or not set(input_str).issubset({"0", "1"}):
                    print(f"Invalid input. You must enter a {component.num_inputs}-bit binary string.")
                    continue

                inputs = binary_string_to_list(input_str)
                output = component.compute(inputs)
                output_str = "".join(map(str, output))

                terminal_width = shutil.get_terminal_size().columns
                message = f"Output: {output_str}"
                nand_info = f"(NAND gates used: {nc.nand_count})"
                padding = max(terminal_width - len(message) - len(nand_info) - 2, 1)
                print(message + " " * padding + nand_info)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()