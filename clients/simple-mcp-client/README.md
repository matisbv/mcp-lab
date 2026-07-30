# MCP client: `simple-mcp-client`

## Summary

This is a simple MCP client that can integrate with any MCP servers. It was copied from the Model Context Protocol's [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client) tutorial. 

## Instructions for use

1. Ensure that you have both `Python 3.10` (or higher) and `uv` installed.

2. In this folder (`clients/mcp-client`), create a `.env` file with the following content:
```
ANTHROPIC_API_KEY=[your Anthropic API key]
```

3. Open your terminal and navigate to this folder (`clients/mcp-client`).

4. In your terminal, run:
> uv run client.py [link to MCP server Python file]

For example:
> uv run client.py ../../servers/weather/weather.py

You terminal will turn into a simple chat application that allows you to call tools from your chosen MCP server. For example, with the weather MCP, you can try asking:
> What are the current weather alerts in California?
See the desired MCP's documentation to determine the tools and methods that can be called.