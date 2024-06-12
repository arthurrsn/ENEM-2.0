import google.generativeai as genai
from flask import Flask, render_template, request
import random

genai.configure(api_key='YOUR_API_KEY')

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name='gemini-1.0-pro',
    generation_config=generation_config
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        modelo_escolhido = request.form.get("modelo", "Reformulação Direta")
        tecnica_escolhida = request.form.get("tecnica")

        prompt_reformulado = gerar_prompt(pergunta, modelo_escolhido, tecnica_escolhida)

        response = model.generate_content(prompt_reformulado)
        resposta = response.text
        return render_template("index.html", pergunta=pergunta, resposta=resposta, prompt_usado=prompt_reformulado)
    else:
        return render_template("index.html")

  def gerar_prompt(pergunta, modelo, tecnica):
    if modelo == "Reformulação Direta":
        return reformular_direta(pergunta, tecnica)
    elif modelo == "Criação de Cenário":
        return criar_cenario(pergunta, tecnica)
    elif modelo == "Abordagem Pragmática":
        return abordagem_pragmatica(pergunta, tecnica)
    else:
        return pergunta  # Caso padrão

def reformular_direta(pergunta, tecnica):
    if tecnica == "Sinônimos":
        return f"Reescreva a pergunta '{pergunta}' utilizando sinônimos."
    elif tecnica == "Reestruturação":
        return f"Reestruture a pergunta '{pergunta}' sem alterar o significado."
    elif tecnica == "Expansão":
        return f"Adicione contexto à pergunta '{pergunta}' para torná-la mais completa."
    else:
        return pergunta

  def criar_cenario(pergunta, tecnica):
    if tecnica == "História Fictícia":
        return f"Crie uma história curta que incorpore a pergunta '{pergunta}'."
    elif tecnica == "Analogia":
        return f"Crie uma analogia para explicar a pergunta '{pergunta}'."
    elif tecnica == "Personificação":
        return f"Personifique os elementos da pergunta '{pergunta}' em um diálogo."
    else:
        return pergunta

def abordagem_pragmatica(pergunta, tecnica):
    if tecnica == "Decomposição":
        return f"Divida a pergunta '{pergunta}' em partes menores e mais específicas."
    elif tecnica == "Reformulação em Etapas":
        return f"Crie uma série de perguntas que levem à resposta da pergunta '{pergunta}'."
    elif tecnica == "Solicitação de Justificativa":
        return f"Responda à pergunta '{pergunta}' e explique o raciocínio por trás da resposta."
    else:
        return pergunta

if __name__ == "__main__":
    app.run(debug=True)
