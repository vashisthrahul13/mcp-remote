from fastmcp import FastMCP
import random
import json

#create the FastMCP server instance
mcp = FastMCP(name='Simple Calculator Server')

#add tools
#Tool: add two numbers
@mcp.tool
def add(a : int, b: int) -> int:
    """Add two numbers
    
    Args :
    a: First number
    b: Second Number
    
    Returns:
    The sum of a and b"""
    return (a + b)

@mcp.tool
def random_number(min_val: int = 1 , max_val: int = 100) -> int:
    """Generate random number in a give range
    
    Args:
    min_val : Minimum value(default = 1)
    max_val : Maximim value(default = 100)
    
    Returns:
    A random number between min_val and max_val"""
    
    return random.randint(min_val,max_val)

#resources : Server information
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server"""
    info = {
        'name': "Simple Calculator Server",
        "version": '1.0.0',
        "tools":["add","random_number"],
        "auth": {
    "type": "none"
  }
    }

    return json.dumps(info,indent=2)

#Start the server
if __name__ == "__main__":
    mcp.run(transport='http',host = '0.0.0.0',port = 8000)