from fastmcp import FastMCP

mcp = FastMCP.as_proxy("https://rv-expense-tracker-mcp.fastmcp.app/mcp",
					   name = "Expense tracker proxy")


if __name__ =="__main__":
	mcp.run()