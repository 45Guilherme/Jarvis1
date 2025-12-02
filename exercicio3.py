def iniciar_jarvis():
    # Loop infinito para manter o Jarvis funcionando até o usuário pedir para encerrar
    while True:
        # Lê o comando digitado pelo usuário
        comando = input("Comando: ")

        # Interpreta o comando e recebe uma resposta
        retorno = interpretar_comando(comando)

        # Exibe o resultado da interpretação
        print(retorno)


def interpretar_comando(comando):
    # Verifica se o comando pede para mostrar as horas
    if "mostrar_horas" in comando:
        return "Agora não posso mostrar horas ainda."

    # Verifica se o comando pede para abrir o navegador
    elif "abrir_navegador" in comando:
        return "Ainda não sei abrir o navegador."

    # Verifica se o comando pede para pesquisar algo
    elif "pesquisar" in comando:
        return "Ainda não sei pesquisar nada."

    # Verifica se o usuário pediu para encerrar o programa
    elif "encerrar" in comando:
        return "Encerrando o programa ..."

    # Caso o comando não seja reconhecido
    else:
        return "Não entendi esse comando."

    
    

