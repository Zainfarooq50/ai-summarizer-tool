# AI Summarizer Tool with GPT-3.5

This Python tool provides quick, AI-generated summaries of any text using OpenAI's GPT-3.5 model. Ideal for summarizing long articles, reports, emails, or documents into concise, easy-to-understand outputs.

---

## ⚡ Features
✅ Accepts free-form text input  
✅ Generates clear, human-friendly summaries using AI  
✅ Automatically saves each summary with a timestamp  
✅ Simple and beginner-friendly  
✅ Great for business, academic, or personal use  

---

## 🛠️ Requirements
- Python 3.x  
- `requests` library  
- OpenAI API key stored in a `config.py` file like:  
  ```python
  api_key = "YOUR_OPENAI_API_KEY"
🚀 How to Use
Ensure your OpenAI API key is added to config.py

Run the script:

bash
Copy
Edit
python Summarize_tool.py
Paste or type your text input (press Enter twice to finish)

The AI will generate a summary and save it in the summaries folder

📁 Output Example
text
Copy
Edit
📝 Enter the text you'd like summarized (Press Enter twice to finish):

OpenAI is an AI research company developing advanced language models such as GPT-3. These models help automate content generation, summarization, and much more.

✅ Summary:
OpenAI develops AI language models like GPT-3 to automate content generation and summarization.

📁 Summary saved to 'summaries/Summary_20250702_145322.txt'