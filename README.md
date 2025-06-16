## Hello World MCP
This is a simple example of a [MCP](https://gofastmcp.com/) server that contains a tool for managing Tasks/Todo business logic and a simple web interface to interact with it. There's also a jupyter notebook that demonstrates how to consume the server with various clients.

## Features
- A local ollama hosted `qwen3:8b` model is used in the examples.
- **MCP Server**: A basic server that implements the MCP protocol.
  - `task.py`: Contains task entity definition and business logic.
  - `server.py`: The main server file that sets up the MCP server and defines the tools and resources.

- **MCP Clients**: A Jupyter notebook `main.ipynb` that demonstrates how to interact with the MCP server using various clients.
  - Native MCP client
  - LangChain
    - within native MCP client
    - with MultiServerMCPClient
  - LLM-interaction
    - with chat model
    - with agent

- **Web Interface**: A simple web interface `app.py` to interact with the MCP server using `gradio` through a react agent.
 
## Installation
- **Prerequisites**:
  - Ensure you have Python 3.8+ installed on your machine.
  - Ollama should be running with a model supporting tool calling, such as `qwen3`.
  - `uv` must be installed globally (`pip install uv`).

- Clone the repository:
  ```bash
  git clone https://github.com/aliakyurek/mcp-hello-world.git 
  cd mcp-hello-world
  ```

- Install the dependencies within a virtual environment:
  ```bash
  uv sync --no-dev
  ```

## Quickstart
**Running the server**
```bash
python server.py
```
or (fastmcp run ignores the `if __name__ == "__main__":` block, so you need to specify the transport type):
```bash
fastmcp run server.py --transport sse
```
Open your web browser and navigate to `http://localhost:8000/sse` to see some events and pings

**MCP Inspector**

To inspect the MCP server and see the offered tools, resources, and other components, you can use the MCP Inspector. This tool provides a user-friendly interface to explore the capabilities of your MCP server. Run it with the following command.
```bash
fastmcp dev server.py
```
**MCP Clients**

You can run the Jupyter notebook `main.ipynb` to see how to interact with the MCP server using various clients.

**Web Interface**

To run the web interface, execute the following command:
```bash
python app.py
```

## Demo



## References
* https://www.youtube.com/watch?v=aiH79Q-LGjY
* https://github.com/jlowin/fastmcp
* https://gofastmcp.com/getting-started/welcome
* https://github.com/langchain-ai/langchain-mcp-adapters/
* https://langchain-ai.github.io/langgraph/agents/mcp
