from datetime import datetime  # Importa a classe datetime para pegar a data e hora atual

def iniciar_jarvis():
    # Loop infinito que mantém o Jarvis rodando até receber o comando "encerrar"
    while True:
        # Solicita que o usuário digite um comando
        comando = input("Comando: ")

        # Envia o comando para a função interpretar_comando e recebe a resposta correspondente
        retorno = interpretar_comando(comando)

        # Exibe a resposta do Jarvis na tela
        print(retorno)

        # Se a resposta for exatamente "Encerrando o programa ...", interrompe o loop
        if retorno == "Encerrando o programa ...":
            break


def interpretar_comando(comando):
    """
    Interpreta o comando digitado pelo usuário e decide qual ação executar.
    Retorna uma mensagem de acordo com o comando reconhecido.
    """

    # Se o comando tiver a palavra "mostrar_horas", chama a função que retorna a hora atual
    if "mostrar_horas" in comando:
        return mostrar_horas()

    # Se o comando tiver a palavra "abrir_navegador", retorna uma resposta informando
    # que essa função ainda não foi implementada
    elif "abrir_navegador" in comando:
        return "Ainda não sei abrir o navegador."

    # Se o comando tiver a palavra "pesquisar", retorna uma mensagem informando
    # que a função ainda não existe
    elif "pesquisar" in comando:
        return "Ainda não sei pesquisar nada."

    # Se o comando tiver a palavra "encerrar", retorna a mensagem que fará o programa parar
    elif "encerrar" in comando:
        return "Encerrando o programa ..."

    # Caso o comando não combine com nada acima, retorna mensagem de erro
    else:
        return "Não entendi esse comando."


def mostrar_horas():
    """
    Retorna a hora atual em formato de texto.
    """
    agora = datetime.now()  # Obtém a data e a hora atuais do sistema
    return "Hora atual: " + str(agora)  # Converte o valor para texto e retorna
