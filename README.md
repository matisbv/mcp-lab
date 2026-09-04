# mcp-lab

A playground for experimenting with the **Model Context Protocol (MCP)**.

This repository contains personal experiments with building and running MCP clients and servers.

## Repository structure

```
mcp-lab/
├── clients/
│   └── MCP clients
│
├── servers/
│   └── MCP servers
│
└── README.md
```

## What's in here

**Clients**
- `http-client` — a Streamable HTTP client that connects to remote MCP servers over the network. Supports no-auth servers and static API-key/bearer-token auth (OAuth not yet supported).
- `stdio-client` — connects to local MCP servers by spawning them as subprocesses.

**Servers**
- `weather` — fetches live weather data from the National Weather Service (weather.gov) API.
- `it-ticketing` — a toy IT ticketing system backed by dummy data.

Each server's capabilities (tools, methods and prompts) are documented in their relevant folder- for example [see documentation for the weather MCP server](servers/weather/README.md).

## Getting started

Ensure that you have both `Python 3.10` (or higher) and `uv` installed.

Each client or server has its own setup instructions. Check the relevant folder for details - for example [see instructions for the weather MCP server](servers/weather/README.md).

## Resources

* Model Context Protocol documentation: https://modelcontextprotocol.io/
* MCP Python SDF documentation: https://py.sdk.modelcontextprotocol.io/
