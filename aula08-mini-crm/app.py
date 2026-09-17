from model import model_lead
import control 

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")   
    company = input("Empresa: ")
    step = input("Etapa de vendas: ")

    # validar entradas do usuário
    # após validação... modelar dados

    print(model_lead(name, email, company, step)) # Retorna um dic
    
    # depois de modelado, vamos enviar o dict (leads) para o leads.json
    # para adicionar, vamos usar o módulo control
    control.create_lead(model_lead(name, email, company, step))

    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    if not leads:
        print("Nenhum lead encontrado")
        return

    print(f"# / {"Nome":<10} / {"E-mail:":<10} / Empresa") 
    for i, lead in enumerate(leads):
        print(f"{i:02d} / {lead["name"]:<10} / {lead["email"]:<10} / {lead["company"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia")
        return

    # Enviar a query para o control realizar a busca no leads.json
    leads_finded = control.read_leads_search(query)

    print(f"# / {"Nome":<10} / {"E-mail:":<10} / Empresa")
    for i, lead in leads_finded:
        print(f"{i:02d} / {lead["name"]:<10} / {lead["email"]:<10} / {lead["company"]}")

def export_leads():
    
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar os leads.")

    else:
        print(f"Exportado para: {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail/empresa)")
        print("[4] Exportar CSV")
        print("[0] Sair do programa")

        option = input("Escolha uma opção: ")

        if option == "1":
            add_lead()

        elif option == "2":
            list_leads()

        elif option == "3":
            search_leads()

        elif option == "4":
            export_leads()

        elif option == "0":
            print("Até mais...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
