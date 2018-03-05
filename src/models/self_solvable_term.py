import abc

from src.models.term import Term


class SelfSolvableTerm(Term, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def self_solve(self):
        raise NotImplementedError('self_solve is not implemented')
