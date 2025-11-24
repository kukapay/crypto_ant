import rich
from rich.panel import Panel
from rich.text import Text

def print_intro():
    """Display the welcome screen with ASCII art."""
    # ANSI color codes
    #LIGHT_BLUE = "\033[94m"
    #RESET = "\033[0m"
    #BOLD = "\033[1m"
    
  
    # ASCII art for CryptoAnt in block letters (financial terminal style) #elite, pagga, ansi compact
    logo = r"""
    
    
░█▀▀░█▀▄░█░█░█▀█░▀█▀░█▀█░█▀█░█▀█░▀█▀
░█░░░█▀▄░░█░░█▀▀░░█░░█░█░█▀█░█░█░░█░
░▀▀▀░▀░▀░░▀░░▀░░░░▀░░▀▀▀░▀░▀░▀░▀░░▀░


"""
    #ascii_art = f"""{BOLD}{LIGHT_BLUE}{logo}{RESET}"""
    
    rich.print(
      Panel(
        Text(logo, justify="center"), 
        title="Welcome to CryptoAnt", 
        subtitle="Your Rentless AI Agent for Crypto Trading & Investment",
        border_style="bright_blue",
        style="bright_blue on black"
      )
    )
    print()
    print("Ask me any questions. Type 'exit' or 'quit' to end.")
    print()

