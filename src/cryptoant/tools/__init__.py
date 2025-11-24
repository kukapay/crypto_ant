# This file makes the directory a Python package from typing_extensions import Callable
import json
import asyncio
from pathlib import Path
from typing_extensions import Callable
from langchain_mcp_adapters.client import MultiServerMCPClient
from cryptoant.tools.search.google import search_google_news
  
def get_mcp_tools():
    def load_mcp_config():
        current_file = Path(__file__).resolve()
        project_root = current_file.parents[3]  
        config_path = project_root / "mcp.json"
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)  
        return config

    config = load_mcp_config()  
    client = MultiServerMCPClient(config["mcpServers"])                           

    return asyncio.run(client.get_tools())
  

TOOLS: list[Callable[..., any]] = [ search_google_news ] + get_mcp_tools()

