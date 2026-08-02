# MCP client: `http-mcp-client`

## Summary

This is a simple MCP client that can integrate with any remote MCP servers via streamable HTTP. It was adapted from the Model Context Protocol's [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client) tutorial - changing the config from stdio/stdout local servers to remote streamable HTTP ones.

## Instructions for use

1. Ensure that you have both `Python 3.10` (or higher) and `uv` installed.

2. In this folder (`clients/mcp-client`), create a `.env` file with the following content:
```
ANTHROPIC_API_KEY=[your Anthropic API key]
```

3. Open your terminal and navigate to this folder (`clients/mcp-client`).

4. In your terminal, run:
> uv run client.py [URL to remote MCP server]

For example:
> uv run client.py https://mcp.deepwiki.com/mcp

You terminal will turn into a simple chat application that allows you to call tools from your chosen MCP server. For example, with the DeepWiki MCP, you can try asking:
> What tokenizer does karpathy use in the nanochat repo?

See the desired MCP's documentation to determine the tools and methods that can be called.