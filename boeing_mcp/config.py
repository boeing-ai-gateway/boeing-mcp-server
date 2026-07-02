"""Configuration for Boeing MCP Server."""

import os


class Config:
    """Configuration settings for the Boeing MCP server."""

    def __init__(self):
        self.boeing_server_url = os.getenv("BOEING_URL", "http://localhost:8080")

        # Ensure URL doesn't end with slash
        if self.boeing_server_url.endswith("/"):
            self.boeing_server_url = self.boeing_server_url[:-1]


# Global config instance
config = Config()
