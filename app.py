import asyncio
import gradio as gr
import re

from langchain_core.messages import AnyMessage, HumanMessage, AIMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

URL = "http://localhost:8000/sse"

client = MultiServerMCPClient(
    {
        "math": {
            "transport": "sse",
            "url": URL
        },
    } # type: ignore
)

async def main():
    tools = await client.get_tools()
    agent = create_react_agent(
        model="ollama:qwen3:8b", # or we can specify the llm instance above
        tools=tools
    )

    async def chat_fn(message, history):
        session_id = "session-123"
        # Create a new session if it doesn't exist
        roled_message = {
            "role": "user",
            "content": message
        }    

        result = await agent.ainvoke(
            {"messages": history + [roled_message]},
            config={"configurable": {"thread_id": session_id}}
        )
        # gradio will accumulate the history automatically by taking the message parameter as human message
        # and the return values as AI messages. It'll also fill metadata and option
        return re.sub(r'<think>.*?</think>', '', result['messages'][-1].content, flags=re.DOTALL) 

    with gr.Blocks() as app:
        gr.Markdown("### Gradio Chat with LangGraph and MCP")
        chatbot = gr.ChatInterface(fn=chat_fn, type="messages")

    app.launch()

if __name__ == "__main__":
    asyncio.run(main())