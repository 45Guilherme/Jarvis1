from datetime import datetime  # Importa a classe datetime para pegar a data e hora atual

def iniciar_jarvis():
    # Loop infinito que mantém o Jarvis rodando até receber o comando "encerrar"
    while True:
        # Solicita que o usuário digite um comando
        comando = input("Comando: ")

        # Envia o comando para a função interpretar_comando e recebe uma resposta
        retorno = interpretar_comando(comando)

        # Exibe a resposta do Jarvis
        print(retorno)

        # Se a resposta indicar encerramento, sai do loop e finaliza o programa
        if retorno == "Encerrando o programa ...":
            break


def interpretar_comando(comando):
    """
    Interpreta o comando digitado pelo usuário e decide qual ação tomar.
    Retorna uma mensagem correspondente à ação.
    """

    # Verifica se o usuário pediu para mostrar horas
    if "mostrar_horas" in comando:
        return "Agora não posso mostrar horas ainda."

    # Verifica se o usuário pediu para abrir o navegador
    elif "abrir_navegador" in comando:
        return "Ainda não sei abrir o navegador."

    # Verifica se o usuário pediu para pesquisar algo
    elif "pesquisar" in comando:
        return "Ainda não sei pesquisar nada."

    # Verifica se o usuário pediu para encerrar o programa
    elif "encerrar" in comando:
        return "Encerrando o programa ..."


def mostrar_horas():
    """
    Retorna a hora atual em formato de texto.
    """
    agora = datetime.now()  # Obtém a data e hora atuais do sistema
    return "Hora atual: " + str(agora)  # Converte a data/hora para texto e retorna
