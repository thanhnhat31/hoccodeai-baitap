import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import yfinance as yf
from pprint import pprint
import inspect
from pydantic import TypeAdapter
import json
import requests

def get_symbol (company: str) -> str:
    """
    Retrieve the stock symbol for a specified company using the Yahoo Finance API.
    :param company: The name of the company for which to retrieve the stock symbol, e.g., 'Nvidia'.
    :output: The stock symbol for the specified company.
    """
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": company, "country": "United States"}
    user_agents = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    res = requests.get(url, params, headers=user_agents)

    data = res.json()
    symbol = data["quotes"][0]["symbol"]
    return symbol


def get_stock_price (symbol: str):
    """
    Retrieve the most recent stock price data for a specified company using the Yahoo Finance API via the yfinance Python library.
    :param symbol: The stock symbol for which to retrieve data, e.g., 'NVDA' for Nvidia.
    :output: A dictionary containing the most recent stock price data.
    """
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d", interval="1m")
    latest = hist.iloc[-1]
    return {
        "timestamp": str(latest.name),
        "open": latest["Open"],
        "high": latest["High"],
        "low": latest["Low"],
        "close": latest["Close"],
        "volume": latest["Volume"]
    }

def view_website(url: str) -> str:
    """
    Fetchs website content from a specified URL
    :param url: The URL of website to fetch content from.
    :output: The content of the website.
    """
    load_dotenv()
    JINA_KEY = os.getenv("JINA_KEY")

    base_url="https://r.jina.ai/"
    prefetch_url = base_url + url
    headers = {
        "Authorization": "Bearer " + JINA_KEY
    }
    response = requests.get(prefetch_url, headers=headers)

    print(response.text)

    return response.text


# nvidia_symbol = get_symbol("Nvidia")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_symbol",
            "description": inspect.getdoc(get_symbol),
            "parameters": TypeAdapter(get_symbol).json_schema(),
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": inspect.getdoc(get_stock_price),
            "parameters": TypeAdapter(get_stock_price).json_schema(),
        },
    },
    {
        "type": "function",
        "function": {
            "name": "view_website",
            "description": inspect.getdoc(view_website),
            "parameters": TypeAdapter(view_website).json_schema(),
        },
    }
]


def get_completion(messages, client: OpenAI, model: str):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        temperature=0
        )
    return response

# Đưa câu hỏi về giá cổ phiếu
#question = "Giá cổ phiếu hiện tại của Vinfast là bao nhiêu?"

#question = "Hãy tóm tắt nội dung của trang web này: https://vnexpress.net/thu-tuong-yeu-cau-som-ket-luan-thanh-tra-ve-kinh-doanh-vang-4885630.html"

def get_answer(question: str, client: OpenAI, model: str):
    messages = [
        {"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."},
        {"role": "user", "content": question}
    ]

    response = get_completion(messages, client=client, model=model)
    first_choice = response.choices[0]
    print(first_choice)

    finish_reason = first_choice.finish_reason
    print(finish_reason)

    FUNCTION_MAP = {
        "get_symbol": get_symbol,
        "get_stock_price": get_stock_price,
        "view_website": view_website,
    }

    while finish_reason != "stop":
        tool_call = first_choice.message.tool_calls[0]

        tool_call_function = tool_call.function
        tool_call_arguments = json.loads(tool_call_function.arguments)

        tool_function = FUNCTION_MAP[tool_call_function.name]
        result = tool_function(**tool_call_arguments)

        print(f"Call {tool_call_function.name} with params {tool_call_function.arguments}. Result: {result}.")

        messages.append(first_choice.message)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call_function.name,
            "content": json.dumps({"result": result})
        })

        print(f"Message: {messages}")

        # Chờ kết quả từ LLM
        response = get_completion(messages, client=client, model=model)
        first_choice = response.choices[0]
        pprint(first_choice)

        finish_reason = first_choice.finish_reason
        pprint(finish_reason)

    # In ra kết quả sau khi đã thoát khỏi vòng lặp
    print(f"BOT RESULT: {first_choice.message.content}")

# Xử lý chính
def main():
    # Load environment variables from .env file
    load_dotenv()
    BASE_URL = os.getenv("BASE_URL")
    #API_KEY = os.getenv("API_KEY")
    API_KEY = os.getenv("TOGETHER_API_KEY")
    MODEL = os.getenv("MODEL")

    if not BASE_URL or not API_KEY or not MODEL:
        raise ValueError("LLM parameters are not set. Please check your enviroment.")

    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY,
    )

    if client is None:
        raise ValueError("Client is not initialized. Please check your API key and base URL.")

    while True:
        # Get input from userpy 
        question = input("Bạn có câu hỏi gì không? ")
        if question.lower() in ['quit', 'close', 'exit']:
            break

        get_answer(question=question, client=client, model=MODEL)

if __name__ == "__main__":
    main()
    



