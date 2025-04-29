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

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")
        print(f"CNS: {self.cns}")
        print(f"Local que se Encontra: {self.local_encontro}")
        print(f"Contato: {self.contato}")
        print(f"Unidade de Saúde que Frequenta: {self.unidade_saude}")
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

# Cadastro de um paciente:
print("=== Registro de Paciente ===")
nome = input("Nome: ")
rg = input("RG: ")
cpf = input("CPF: ")
cns = input("CNS: ")
local_encontro = input("Local que se Encontra: ")
contato = input("Contato: ")
unidade_saude = input("Unidade de Saúde que Frequenta: ")

problemas = input("Problemas de Saúde (separe por vírgula): ")
problemas = [p.strip() for p in problemas.split(",") if p.strip()]

medicacoes = input("Medicações em Uso (separe por vírgula): ")
medicacoes = [m.strip() for m in medicacoes.split(",") if m.strip()]

pa = input("PA: ")
fc = input("FC: ")
sat = input("SAT: ")
dextro = input("Dextro: ")
sinais_vitais = {"PA": pa, "FC": fc, "SAT": sat, "Dextro": dextro}

odontologia = input("Odontologia: ")
conduta_odontologia = input("Conduta Odontologia: ")

medico = input("Médico: ")
conduta_medica = input("Conduta Médica: ")

outras_demandas = input("Outras Demandas: ")

paciente = Paciente(
    nome, rg, cpf, cns, local_encontro, contato, unidade_saude,
    problemas, medicacoes, sinais_vitais, odontologia, conduta_odontologia,
    medico, conduta_medica, outras_demandas
)

print("\n=== Ficha do Paciente ===")
paciente.exibir()
