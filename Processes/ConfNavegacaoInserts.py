def obtem_valor_bd(valor):
    if valor == None:
        return 'null'
    elif isinstance(valor, bool):
        return 1 if valor else 0
    elif isinstance(valor, int):
        return valor
    else:
        return "'" + valor.replace("'", "''") + "'"


class ConfNavegacaoInserts:
    def __init__(self, configuracoes, path):
        self.path_script = path
        self.paginas = ''
        self.configuracoes_nav = ''
        self.configuracoes = configuracoes

    def process(self):
        for configuracao in self.configuracoes:
            self.trata_configuracao(configuracao)
        self.escreve_script()

    def trata_configuracao(self, configuracao):
        if configuracao.pagina.generate:
            self.gera_pagina(configuracao.pagina)
        self.gera_configuracao(configuracao)

    def gera_configuracao(self, configuracao):
        self.configuracoes_nav += 'insert into () values'
        self.configuracoes_nav += '('
        self.configuracoes_nav += obtem_valor_bd(configuracao.menus_id) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.pagina) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.pagina_seguinte) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.pagina_pai) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.redesenha_navegacao) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.nivel) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.mvc_action_name_cabecalho) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.apresenta_bread_crumb) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.tipologias_id) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.programas_id) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.sub_navegacao) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.obrigatoriedade_id) + ','
        self.configuracoes_nav += obtem_valor_bd(configuracao.tipos_navegacao) + ','
        self.configuracoes_nav += 'getdate(),1,getdate(),1)\n'

    def gera_pagina(self, pagina):
        self.paginas += 'insert into () values '
        self.paginas += '('
        self.paginas += obtem_valor_bd(pagina.id) + ','
        self.paginas += obtem_valor_bd(pagina.nome_pagina) + ','
        self.paginas += obtem_valor_bd(pagina.mvc_action_name) + ','
        self.paginas += 'getdate(),1,getdate(),1)\n'

    def escreve_script(self):
        if self.paginas == '' and self.configuracoes == '':
            pass
        with open(self.path, 'w') as f:
            f.write('-- Paginas \n')
            f.write(self.paginas)
            f.write('\n\n-- Configuracoes Navegacao \n')
            f.write(self.configuracoes)
        f.close()
