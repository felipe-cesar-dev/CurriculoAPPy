while True:
    try:
        valor = input('Digite a data de nascimento (DD/MM/AA): ')
        if not valor.strip():
            raise ValueError("N pode ser em branco")
        break
    except ValueError:
        print("N pode ser em branco")

