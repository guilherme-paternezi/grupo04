from random import randint

class dados_view_model:
    def __init__(self,transaction, tempo , memoria, estado_atual):
        self.transaction = transaction
        self.tempo = tempo
        self.memoria = memoria
        self.etnia = self.gerar_etnia()
        self.classe_social = self.gerar_classe_social()
        self.idade = self.gerar_idade()
        self.sexo = self.gerar_sexo()
        self.grupo_risco = self.gerar_grupo_risco()
        self.febre = self.gerar_febre()
        self.coriza = self.gerar_coriza()
        self.tosse = self.gerar_tosse()
        self.dor_muscular = self.gerar_dor_muscular()
        self.variante = self.gerar_variante()
        self.estado_atual = estado_atual
    
    def mostrar_dados_da_View_model(self):
        print("\
Inserido o valor no banco de dados: transaction = {},\
tempo = {},\
memoria = {},\
etnia = {},\
idade = {},\
sexo = {},\
grupo de risco = {},\
febre = {},\
coriza = {},\
tosse = {},\
dor muscular = {},\
variante = {},\
classe social = {},\
estado = {} \
".format(
            self.transaction,
            self.tempo,
            self.memoria,
            self.etnia,
            self.idade,
            self.sexo,
            self.grupo_risco,
            self.febre,
            self.coriza,
            self.tosse,
            self.dor_muscular,
            self.variante,
            self.classe_social,
            self.estado_atual)) 
    
    def gerar_etnia(self):
        valor = randint(0, 100)
        if self.classe_social == "Baixa":
            valor = valor + 5
        elif self.classe_social == "Alta":
            valor = valor - 5
        etnia = ""
        if valor < 43:
            etnia = "Branca"
        elif valor < 90:
            etnia = "Pardos"
        elif valor < 99:
            etnia = "Preta"
        else:
            etnia = "Amarela ou Indigena"
        return etnia

    def gerar_idade(self):
        valor_idade = randint(0, 1000)
        idade = ""
        if valor_idade < 210:
            idade = "Menor de 0 a 14 anos"
        elif valor_idade < 450:
            idade = "15 a 29 anos"
        elif valor_idade < 864:
            idade = "30 a 59 anos"
        else:
            idade = "Maior de 60 anos"
        return idade

    def gerar_sexo(self):
        valor_sexo = randint(0, 100)
        sexo = ""
        if valor_sexo < 53:
            sexo = "F"
        else:
            sexo = "M"
        return sexo

    def gerar_grupo_risco(self):
        valor_grupo = randint(0, 100)
        grupo_risco = False
        if valor_grupo < 55:
            grupo_risco = True
        return grupo_risco
    
    def gerar_febre(self):
        valor_febre = randint(0, 100)
        febre = False
        if valor_febre < 82:
            febre = True
        return febre

    def gerar_coriza(self):
        valor_coriza = randint(0, 100)
        coriza = False
        if valor_coriza < 85:
            coriza = True
        return coriza
    
    def gerar_tosse(self):
        valor_tosse = randint(0, 100)
        tosse = False
        if valor_tosse < 80:
            tosse = True
        return tosse

    def gerar_dor_muscular(self):
        valor_dor = randint(0, 100)
        dor_muscular = False
        if valor_dor < 80:
            dor_muscular = True
        return dor_muscular

    def gerar_variante(self):
        valor_variante = randint(0, 100)
        variante = ""
        if valor_variante < 50:
            variante = "Omicron"
        elif valor_variante < 80:
            variante = "Delta"
        else:
            variante = "Alpha"
        return variante
    
    def gerar_classe_social(self):
        valor_social = randint(0, 100)
        classe_social = ""
        if valor_social < 6:
            classe_social = "Alta"
        elif valor_social < 53:
            classe_social = "Media"
        else:
            classe_social = "Baixa"
        return classe_social
