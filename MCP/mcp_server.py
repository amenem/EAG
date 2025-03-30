from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

mcp = FastMCP("string reverser")

@mcp.tool()
async def reverse_string(text: str)-> dict:
    return {
        'content':TextContent(
            type='text',
            text=text[::-1]
        )
    }
if __name__=='__main__':
    print("Starting MCP String Reverser server...")
    mcp.run()