def iniciar_jarvis():
    # Loop infinito que mantém o Jarvis rodando até receber o comando de encerrar
    while True:
        # Lê o comando digitado pelo usuário
        comando = input("Comando: ")

        # Interpreta o comando e guarda o que deve ser retornado
        retorno = interpretar_comando(comando)

        # Exibe o resultado da interpretação
        print(retorno)

        # Se o Jarvis recebeu o comando de encerrar, ele sai do loop e termina o programa
        if retorno == "Encerrando o programa ...":
            break


def interpretar_comando(comando):
    # Se o comando contiver "mostrar_horas", retorna a resposta adequada
    if "mostrar_horas" in comando:
        return "Agora não posso mostrar horas ainda."

    # Se o comando contiver "abrir_navegador", retorna a resposta adequada
    elif "abrir_navegador" in comando:
        return "Ainda não sei abrir o navegador."

    # Se o comando contiver "pesquisar", retorna a resposta adequada
    elif "pesquisar" in comando:
        return "Ainda não sei pesquisar nada."

    # Se o comando contiver "encerrar", retorna a mensagem de encerramento
    elif "encerrar" in comando:
        return "Encerrando o programa ..."

