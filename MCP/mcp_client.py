from mcp import  ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
from pdb import set_trace

async def main():
    #Create serverparameter for stdio connection
    server_params = StdioServerParameters(
        command='python',
        args=['mcp_server.py']
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Connected to MCP server")

            #Get input from user
            text = input("Enter text to reverse:")

            result = await session.call_tool(
                "reverse_string",
                arguments={'text':text}
            )

            reversed_string=result.content[0].text

            print (f"Reversed string- {reversed_string}")
            # print(dir(session))
            result= await session.list_tools()
            # print('\n\n\n', result.tools)

if __name__=='__main__':
    asyncio.run(main())


