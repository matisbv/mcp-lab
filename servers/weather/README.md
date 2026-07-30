# MCP server: `weather`

## Summary

This is a simple MCP server that can fetch US-specific weather information from `https://api.weather.gov`. It was copied from the Model Context Protocol's [Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server) tutorial. 

## Capabilities

### Tools

#### get_alerts

Get weather alerts for a US state.

Args:
- state: Two-letter US state code (e.g. CA, NY)

#### get_forecast

Get weather forecast for a location.

Args:
- latitude: Latitude of the location
- longitude: Longitude of the location

### Methods

None. 

### Prompts

None.

## Instructions for use

### Local run for testing purposes

1. Ensure that you have both `Python 3.10` (or higher) and `uv` installed.
2. Open your terminal and navigate to this folder (`servers/weather`).
3. In your terminal, run:
> uv run weather.py

If there are no errors, it is a signal that the MCP server is running properly.

### Using the MCP server

To use the server, you must connect to it from a MCP client. Two simple options to do so:
- Use Claude Desktop as a MCP client - see [this step](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#testing-your-server-with-claude-for-desktop) from the official MCP tutorial.
- Use a local MCP client from this repo - see for example [`clients/simple-mcp-client/README.md`](../../clients/simple-mcp-client/README.md).

### Examples of use

- What are the current weather alerts in California?
- What is the weather forecast in Seattle?