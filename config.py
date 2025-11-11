import os
from dotenv import load_dotenv

load_dotenv()

# DeepSeek API配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# DEEPSEEK_API_KEY = "sk-2dd01bce9aca4dfe89943bbaec98b31f"
# DEEPSEEK_API_BASE = "https://ark.cn-beijing.volces.com/api/v3/bots"
# DEEPSEEK_API_BASE = "https://ark.cn-beijing.volces.com/api/v3/bots/chat/completions"
# DEEPSEEK_API_BASE = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
DEEPSEEK_API_BASE = "https://api.deepseek.com"

# MCP服务器配置
MCP_HOST = "0.0.0.0"
MCP_PORT = 8000

# Streamlit配置
STREAMLIT_PORT = 8501 