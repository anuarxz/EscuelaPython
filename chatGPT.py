import openai
import typer
from rich import print
from rich.table import Table

"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/
"""

def main():
    openai.api_key = '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'

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table('Comando', 'Descripción')
    table.add_row('exit', 'Salir de la aplicación')
    table.add_row('new', 'Crear nueva aplicación')

    print(table)

    # Contexto del asistente
    context = {'role':'system', 'context':'Eres un asistente que me ayudará en mis tareas diarias. Contesta a todo lo que te pregunte en español'}
    messages = [context]

    while True:
        context = __prompt()

        if context == 'new':
            print('Nueva conversación creada')
            messages = [context]
            content = __prompt()

        messages.append({'role':'user', 'context': content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        
        response_content = response.choices[0].message.content
        messages.append({'role':'assistant', 'context': response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt('\n¿Sobre qué quieres hablar?')

    if prompt == 'exit':
        exit = typer.confirm('¿Estás seguro?')
        if exit:
            print('Hasta luego!')
            raise typer.Abort()

        return __prompt()
    
    return prompt

if __name__ == '__main__':
    typer.run(main)