#!/usr/bin/env python3
"""
Wrapper for FileSystemMCP server to make it discoverable by SuperMCP.

This wrapper allows SuperMCP to find and launch the FileSystemMCP server
which is located in the file-system-mcp-server subdirectory.
"""

import sys
import os
from pathlib import Path

# Add the file-system-mcp-server directory to the path
server_dir = Path(__file__).parent / "file-system-mcp-server"
sys.path.insert(0, str(server_dir))

# Change to the server directory so relative imports work
os.chdir(server_dir)

# Import and run the actual fs_server
if __name__ == "__main__":
    import fs_server
    # The fs_server.py has its own if __name__ == "__main__" block that runs mcp.run()
    # But since we imported it as a module, we need to manually call run()
    fs_server.mcp.run()

