from model import model_lead
import control 

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")   
    company = input("Empresa: ")
    step = input("Etapa de vendas: ")

    # validar entradas do usuário
    # após validação... modelar dados

    print(model_lead(name, email, company, step))
    
    # depois de modelado, vamos enviar o dict (leads) para o leads.json
    # para adicionar, vamos usar o módulo control
    control.create_lead(model_lead(name, email, company, step))

    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    if not leads:
        print("Nenhum lead encontrado")
        return

    print(leads) # pegar esses leads, percorrer e passar uma tabela no terminal com ID (0, 1 , 2), etc

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        option = input("Escolha uma opção: ")

        if option == "1":
            add_lead()

        elif option == "2":
            list_leads()

        elif option == "0":
            print("Até mais...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
