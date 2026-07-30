# MCP server: `it-ticketing`

## Summary

This is a toy MCP server that simulates an IT ticketing system. It was implemented from scratch.

The MCP server is not connected to a real database - it uses a hardcoded, in-memory list of IT tickets:

| id | subject | status | opened_at | escalation_reason | resolution_note |
|----------|----------|----------|----------|----------|----------|
|1    |     Forgot my password     |    resolved      |   datetime(2026, 4, 20)       |   None       |   New password assigned to user       |
|2    |    Computer does not turn on anymore      |    resolved      |    datetime(2026, 6, 1)      |    None      |     Computer replaced     |
|3    |    Cannot access ChatGPT      |    escalated      |     datetime(2026, 7, 15)     |    User did not get response from IT in 2 days      |    None      |
|4    |    Lost my work phone      |    open      |     datetime(2026, 7, 23)     |   None       |     None     |
|5    |   Cannot access Outlook       |   open       |   datetime(2026, 7, 25)       |     None     |    None      |

## Capabilities

### Tools

#### get_ticket

Return full details for one ticket.

Args:
- ticket_id: Ticket id (int).

#### list_all_tickets

Return all tickets.

Args: none.

#### list_open_tickets_tool

Return all tickets currently open.

Args: none.

#### escalate_ticket

Escalate a ticket.

Args:
- ticket_id: Ticket id (int).
- reason: Reason for escalation (string).

#### resolve_ticket

Resolve a ticket.

Args:
- ticket_id: Ticket id (int).
- resolution_note: Note for resolution (string).


### Resources

#### list_open_tickets_resource

Return all tickets currently open.

Args: none.


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

- Find all tickets that are currently open and escalate them. The reason is that we need to close all tickets before the end of this week.
- Close ticket 5, the user has recovered access.