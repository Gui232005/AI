import ollama
import time

class LocalLLM:
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = ollama.Ollama(model_name)

    def generate(self, prompt, max_tokens=100):
        response = self.model.generate(prompt, max_tokens=max_tokens)
        return response.text