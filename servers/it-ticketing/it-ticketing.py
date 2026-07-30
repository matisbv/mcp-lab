from mcp.server.fastmcp import FastMCP
from datetime import datetime
import random, io
from urllib.error import HTTPError

# Initialize FastMCP server
mcp = FastMCP("it-ticketing")

# Constants
API_FAILURE_MOCK_PROB = 0.3

# Helper functions
def format_ticket(ticket: dict) -> str:
    """Format a ticket into a readable string."""
    return f"""    Ticket ID: {ticket.get("id", "Unknown")}
    Subject: {ticket.get("subject", "Unknown")}
    Status: {ticket.get("status", "Unknown")}
    Opened at: {ticket.get("opened_at", "Unknown")}
    Escalation reason: {ticket.get("escalation_reason", "Unknown")}
    Resolution note: {ticket.get("resolution_note", "Unknown")}
"""

def format_ticket_list(ticket_list: list) -> str:
    """Format a list of tickets into a readable string."""
    if len(ticket_list) == 0:
        return ''
    else:
        formatted_ticket_list = ''
        for ticket_number in range(len(ticket_list)):
            formatted_ticket_list += f"""Ticket {ticket_number+1}: \n{format_ticket(ticket_list[ticket_number])}"""
    return formatted_ticket_list

# Data model
tickets = {
    1: {'id': 1, 'subject': 'Forgot my password', 'status': 'resolved', 'opened_at': datetime(2026, 4, 20), 'escalation_reason': None, 'resolution_note': 'New password assigned to user'},
    2: {'id': 2, 'subject': 'Computer does not turn on anymore', 'status': 'resolved', 'opened_at': datetime(2026, 6, 1), 'escalation_reason': None, 'resolution_note': 'Computer replaced'},
    3: {'id': 3, 'subject': 'Cannot access ChatGPT', 'status': 'escalated', 'opened_at': datetime(2026, 7, 15), 'escalation_reason': 'User did not get response from IT in 2 days', 'resolution_note': None},
    4: {'id': 4, 'subject': 'Lost my work phone', 'status': 'open', 'opened_at': datetime(2026, 7, 23), 'escalation_reason': None, 'resolution_note': None},
    5: {'id': 5, 'subject': 'Cannot access Outlook', 'status': 'open', 'opened_at': datetime(2026, 7, 25), 'escalation_reason': None, 'resolution_note': None},
}

# Helper functions
def list_open_tickets() -> str:
    """Return all tickets currently open."""        
    open_tickets = []
    for ticket in tickets.values():
        if ticket.get('status') == 'open':
            open_tickets.append(ticket)
    return f"There are currently {len(open_tickets)} open tickets: \n---\n" + format_ticket_list(open_tickets)

# Resources
@mcp.resource("tickets://open")
def list_open_tickets_resource() -> str:
    """Return all tickets currently open."""        
    return list_open_tickets()

# Tools
@mcp.tool()
def get_ticket(ticket_id: int) -> str:
    """Return full details for one ticket."""
    ticket = tickets.get(ticket_id, "Not found")
    formatted_ticket = format_ticket(ticket) if isinstance(ticket, dict) else f"Error: ticket {ticket_id} not found in database"
    return(formatted_ticket)

@mcp.tool()
def list_all_tickets() -> str:
    """Return all tickets."""
    # Artificial flakiness
    api_failure = random.random() < API_FAILURE_MOCK_PROB
    if api_failure:
        dummy_fp = io.BytesIO(b"Internal Server Error Payload")
        raise HTTPError(
            url="https://example.com",
            code=500,
            msg="Couldn't connect to database",
            hdrs={"Content-Type": "application/json"},
            fp=dummy_fp
        )
        
    tickets_list = [ticket for ticket in tickets.values()]

    return f"There are currently {len(tickets_list)} tickets: \n---\n" + format_ticket_list(tickets_list)

@mcp.tool()
def list_open_tickets_tool() -> str:
    """Return all tickets currently open."""
    return list_open_tickets()

@mcp.tool()
def escalate_ticket(ticket_id: int, reason: str):
    """Escalate a ticket."""
    if reason == '' or reason is None:
        return('Escalation reason is empty or missing. Please provide valid reason for escalation.')
    tickets[ticket_id]['status'] = 'escalated'
    tickets[ticket_id]['escalation_reason'] = reason
    return(f'Ticket {ticket_id} successfully escalated.')

@mcp.tool()
def resolve_ticket(ticket_id: int, resolution_note: str):
    """Resolve a ticket."""
    tickets[ticket_id]['status'] = 'resolved'
    tickets[ticket_id]['resolution_note'] = resolution_note
    return(f'Ticket {ticket_id} successfully resolved.')

# Running the server
def main():
    # Initialize and run the server
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
