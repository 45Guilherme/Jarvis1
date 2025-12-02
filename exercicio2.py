def interpretar_comando(comando):
    # Verifica se o usuário pediu para saber as horas
    if "Que horas são" in comando:
        return "mostrar_horas"

    # Verifica se o usuário pediu para abrir o navegador
    elif "abrir o navegador" in comando:
        return "abrir_navegador"

    # Verifica se o usuário pediu para fazer uma pesquisa
    elif "pesquise" in comando:
        return "pesquisar"

    # Verifica se o usuário pediu para encerrar o Jarvis
    elif "sair" in comando:
        return "encerrar"

    # Caso o comando não se encaixe em nenhuma opção conhecida
    else:
        return "desconhecido"




        
