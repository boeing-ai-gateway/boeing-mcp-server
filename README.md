# Boeing MCP Server

MCP server for Boeing that provides tools for discovering, searching, and connecting to MCP servers.

## Tools

- **`boeing_list_mcp_servers`** - List available MCP servers with optional runtime filtering
- **`boeing_list_connected_mcp_servers`** - List connected/configured MCP servers for the current user
- **`boeing_search_mcp_servers`** - Search servers by keyword (matches name and description)
- **`boeing_connect_to_mcp_server`** - Connect to a server by ID, handling configuration, OAuth, and launch

## Quick Start

```bash
uv sync
BOEING_URL=<url> uv run python main.py
```

The server listens on port 8080 and path `/mcp` using streamable-http transport.

## Docker

Pre-built images are available from GitHub Container Registry:

```bash
docker pull ghcr.io/boeing-ai-gateway/boeing-mcp-server:latest
docker run -e BOEING_URL=<url> -p 8080:8080 ghcr.io/boeing-ai-gateway/boeing-mcp-server:latest
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `BOEING_URL` | Boeing API base URL | `http://localhost:8080` |

Authentication is forwarded from the incoming request's `Authorization` header to the Boeing API.

## Testing

```bash
uv run pytest test_server.py -v
```
