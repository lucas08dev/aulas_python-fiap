from datetime import date

def model_lead(name, email, company, step = "novo"):
    """Estrutura um lead com dicionário"""
    return { 
        "name": name,
        "email": email,
        "company": company,
        "step": step,
        "created": date.today().isoformat()
    }