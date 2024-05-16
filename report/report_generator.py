from abc import abstractmethod
class ReportGenerator:
    @abstractmethod
    def generate_report(self, data):
        pass