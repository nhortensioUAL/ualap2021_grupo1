def cria_tabela_precos():
  metropolitano = {"tipo_passe":"Metropolitano","validade_espacial": "AML",
                   "validade_temporal": 1 ,"normal": 40,"social_b": 30, "social_a": 20,
                   "sub_23":16}
  municipal_lisboa = {"tipo_passe":"Municipal Lisboa","validade_espacial": "Lisboa",
                   "validade_temporal": 1 ,"normal": 30,"social_b": 22.5, "social_a": 15,
                   "sub_23":12}  
  municipal_amadora = {"tipo_passe":"Municipal Amadora","validade_espacial": "Amadora",
                   "validade_temporal": 1 ,"normal": 30,"social_b": 22.5, "social_a": 15,
                   "sub_23":12}
  municipal_odivelas = {"tipo_passe":"Municipal Odivelas","validade_espacial": "Amadora",
                   "validade_temporal": 1 ,"normal": 30,"social_b": 22.5, "social_a": 15,
                   "sub_23":12}
  menos_12 = {"tipo_passe":"-12","validade_espacial": "AML",
                   "validade_temporal": 12 ,"normal": 0,"social_b": 0, "social_a": 0,
                   "sub_23":0}  
  mais_16 = {"tipo_passe":"+16","validade_espacial": "AML",
                   "validade_temporal": 1 ,"normal": 20,"social b": 20, "social a": 20,
                   "sub23":20}
  tabela_precos = [metropolitano,municipal_lisboa,municipal_amadora,municipal_odivelas,
                   menos_12,mais_16]
  return tabela_precos
    
def obter_validade_espacial(tabela_precos,tipo_passe):
    for passe in tabela_precos:
        if(passe["tipo_passe"] == tipo_passe):
            return passe["validade_espacial"]

def obter_validade_temporal(tabela_precos,tipo_passe):
    for passe in tabela_precos:
        if(passe["tipo_passe"] == tipo_passe):
            return passe["validade_temporal"]
        
def obter_preco(tabela_precos,tipo_passe,escalao):
    escalao = escalao.lower()
    for passe in tabela_precos:
        if(passe["tipo_passe"] == tipo_passe):
            return passe[escalao]