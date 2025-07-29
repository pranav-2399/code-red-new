import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def run_gemini_generation(route_json_path):
    def read_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def read_json(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    route_json = read_json(route_json_path)

    full_prompt = (
        f"ROUTE DATA:\n{route_json}\n"
        f"\nProvide 5 distinct routes between the source and destination."
        f" Describe each route with details about bus stops, metro stations, legs, cost-effectiveness, and shortest/fastest options."
        f" For each leg, include both the start and end locations' names along with their respective latitude and longitude coordinates."
        f" Also include lat/lon for the overall source and destination fields in the route."
        f"\nHere is a sample output. Use this to generate a large paragraph with all details regarding the output." 
    )

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    print("⚡ Querying Gemini...")
    try:
        output = ""
        for chunk in llm.stream(full_prompt):
            output += chunk.content
            print(chunk.content, end="", flush=True)
        return output
    except Exception as e:
        print("Streaming error:", e)

