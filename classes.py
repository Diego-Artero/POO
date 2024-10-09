from abc import ABC
from datetime import datetime
from validate_email_address import validate_email


class Validador:
    @staticmethod
    def validar_emails(emails: list[str]) -> list[str]:
        emails_validados = []
        for email in emails:
            try:
                if validate_email(email, verify=True) is True:
                    emails_validados.append(email)
                else:
                    raise ValueError
            except ValueError:
                pass
        return emails_validados
    @staticmethod
    def validar_data(date:datetime) -> datetime:
        if date > datetime.now():
            return date
        else:
            raise ValueError("A data fornecida não pode ser anterior à data atual.")


class Compromisso(ABC):
    def __init__(self,data:datetime, titulo:str):
        self.data = Validador.validar_data(data)
        self.titulo = titulo

class Evento(Compromisso):
    def __init__(self, data:datetime, titulo:str, emails:list[str], local:str = ''):
        super().__init__(data, titulo)
        self.emails = Validador.validar_emails(emails)
        self.local = local

class Tarefa(Compromisso):

    def __init__(self, data:datetime, titulo:str):
        super().__init__(data, titulo)
        self._estado = False
    def marcar_concluir(self):
        self._estado = True
    def marcar_incompleto(self):
        self._estado = False