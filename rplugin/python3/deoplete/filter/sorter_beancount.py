from .base import Base
import logging


class Filter(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter_beancount'
        self.description = 'beancount sorter'

    def filter(self, context):
        complete_str = context['complete_str'].lower()
        input_len = len(complete_str)
        return sorted(context['candidates'],
                      key=lambda x: (
                          self.rank_account(x['word']),
                          abs(x['word'].lower().find(complete_str, 0, input_len))
                          )
                      )

    def rank_account(self, account):
        if account.startswith('Expenses'):
            return 1
        elif account.startswith('Equity'):
            return 3
        return 2
