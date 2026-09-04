# MCP client: `http-mcp-client`

## Summary

This is a simple MCP client that can integrate with remotely hosted MCP servers via streamable HTTP. It was created as an extension of the Model Context Protocol's [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client) tutorial.

The client can connect to MCP servers with the following authorization schemes:
- No-auth.
- Static API key / Bearer tokens.

OAuth protocol is not yet supported.


## Instructions for use

1. Ensure that you have both `Python 3.10` (or higher) and `uv` installed.

2. In this folder (`clients/mcp-client`), create a `.env` file with the following content:
```
ANTHROPIC_API_KEY=[your Anthropic API key]
```

If connecting to a MCP server with static API key / Bearer token authorization, add to the `.env` file:
```
MCP_API_KEY=[your MCP API key]
```

3. Open your terminal and navigate to this folder (`clients/mcp-client`).

4. In your terminal, run:
> uv run client.py [URL to remote MCP server]

Example 1 (no-auth): [DeepWiki](https://docs.devin.ai/work-with-devin/deepwiki-mcp)
> uv run client.py https://mcp.deepwiki.com/mcp

Example 2 (static API key): [Github](https://github.com/github/github-mcp-server) (requires a personal access token)
> uv run client.py https://api.githubcopilot.com/mcp/

You terminal will turn into a simple chat application that allows you to call tools from your chosen MCP server. For example, with the DeepWiki MCP, you can try asking:
> What tokenizer does karpathy use in the nanochat repo?

See the desired MCP's documentation to determine the tools and methods that can be called.