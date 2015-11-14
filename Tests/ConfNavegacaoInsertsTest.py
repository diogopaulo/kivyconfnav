from Processes.ConfNavegacaoInserts import ConfNavegacaoInserts

class ConfNavegacaoInsertsTest:
    def __init__(self, test_path):
        self.path = test_path

    def test(self):
        configuracoes = self.mock_configuracoes()
        process = ConfNavegacaoInserts(configuracoes, self.path)
        process.process()

    def mock_configuracoes(self):
        pass