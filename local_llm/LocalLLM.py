import ollama
import time

class LocalLLM:
    def __init__(self, model_name='llama3.2:3b'):
        self.model_name = model_name
        self.cache = {}

    def get_attractions(self, city_name):
        if city_name in self.cache:
            return self.cache[city_name]
        
        try:
            start_time = time.time()
            response = ollama.chat(
                model=self.model_name,
                messages=[{
                    'role': 'user',
                    'content': f"""Descreve as 3 principais atrações turísticas de {city_name} no páis Portugal (Europa).
                    Escreve em português de Portugal.
                    Sê conciso e informativo. Máximo 15 palavras por atração."""
                }]
            )
            elapsed_time = time.time() - start_time

            result = {
                'attractions': response['message']['content'],
                'time': elapsed_time
            }

            self.cache[city_name] = result
            return result
        
        except Exception as e:
            return {
                'attractions': f"Erro ao obter atrações: {str(e)}",
                'time': 0
            }
