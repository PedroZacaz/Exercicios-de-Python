import json

class Paciente:
    def __init__(self, nome, rg, cpf, cns, local_encontro, contato, unidade_saude,
                 problemas_saude, medicacoes, sinais_vitais, odontologia, conduta_odontologia,
                 medico, conduta_medica, outras_demandas):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.cns = cns
        self.local_encontro = local_encontro
        self.contato = contato
        self.unidade_saude = unidade_saude
        self.problemas_saude = problemas_saude
        self.medicacoes = medicacoes
        self.sinais_vitais = sinais_vitais
        self.odontologia = odontologia
        self.conduta_odontologia = conduta_odontologia
        self.medico = medico
        self.conduta_medica = conduta_medica
        self.outras_demandas = outras_demandas

    def to_dict(self):
        return self.__dict__

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")
        print(f"CNS: {self.cns}")
        print(f"Local de Encontro: {self.local_encontro}")
        print(f"Contato: {self.contato}")
        print(f"Unidade de Saúde: {self.unidade_saude}")
        print("Problemas de Saúde:", ", ".join(self.problemas_saude))
        print("Medicações em Uso:", ", ".join(self.medicacoes))
        print("Sinais Vitais:")
        for k, v in self.sinais_vitais.items():
            print(f"  {k}: {v}")
        print(f"Odontologia: {self.odontologia}")
        print(f"Conduta Odontologia: {self.conduta_odontologia}")
        print(f"Médico: {self.medico}")
        print(f"Conduta Médica: {self.conduta_medica}")
        print(f"Outras Demandas: {self.outras_demandas}")
        print("-" * 40)

# Funcionalidades simples
pacientes = []

def adicionar_paciente():
    print("=== Novo Paciente ===")
    nome = input("Nome: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    cns = input("CNS: ")
    local_encontro = input("Local de Encontro: ")
    contato = input("Contato: ")
    unidade_saude = input("Unidade de Saúde: ")
    problemas = input("Problemas de Saúde (separe por vírgula): ").split(",")
    medicacoes = input("Medicações em Uso (separe por vírgula): ").split(",")
    pa = input("PA: ")
    fc = input("FC: ")
    sat = input("SAT: ")
    dextro = input("Dextro: ")
    sinais = {"PA": pa, "FC": fc, "SAT": sat, "Dextro": dextro}
    odontologia = input("Odontologia: ")
    conduta_odo = input("Conduta Odontologia: ")
    medico = input("Médico: ")
    conduta_med = input("Conduta Médica: ")
    outras = input("Outras Demandas: ")

    p = Paciente(nome, rg, cpf, cns, local_encontro, contato, unidade_saude,
                 [s.strip() for s in problemas], [m.strip() for m in medicacoes],
                 sinais, odontologia, conduta_odo, medico, conduta_med, outras)
    pacientes.append(p)
    print("Paciente adicionado com sucesso!")

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        print("=== Lista de Pacientes ===")
        for p in pacientes:
            p.exibir()

def salvar_em_arquivo(caminho='pacientes.json'):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump([p.to_dict() for p in pacientes], f, ensure_ascii=False, indent=4)

def carregar_de_arquivo(caminho='pacientes.json'):
    global pacientes
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            pacientes = [Paciente(**d) for d in dados]
    except FileNotFoundError:
        pacientes = []

def menu():
    carregar_de_arquivo()
    while True:
        print("\n1. Adicionar Paciente")
        print("2. Listar Pacientes")
        print("3. Sair")
        opc = input("Escolha uma opção: ")
        if opc == "1":
            adicionar_paciente()
            salvar_em_arquivo()
        elif opc == "2":
            listar_pacientes()
        elif opc == "3":
            salvar_em_arquivo()
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
