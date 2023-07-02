from django.db import models
from django_fsm import FSMField
from django_fsm import transition


class LeadState(models.Model):
    STATE_NEW = 'new'
    STATE_IN_PROGRESS = 'in_progress'
    STATE_POSTPONED = 'postponed'
    STATE_DONE = 'done'

    STATE_CHOICES = (
        (STATE_NEW, 'Новый'),
        (STATE_IN_PROGRESS, 'В работе'),
        (STATE_POSTPONED, 'Приостановлен'),
        (STATE_DONE, 'Завершен'),
    )

    name = models.CharField(
        'Название',
        max_length=50,
        choices=STATE_CHOICES,
        unique=True,
    )

    def __str__(self):
        return self.name


class Lead(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Имя',
    )
    state = FSMField(
        default=LeadState.STATE_NEW,
        verbose_name='Состояние',
    )

    @transition(field=state, source=LeadState.STATE_NEW, target=LeadState.STATE_IN_PROGRESS)
    def start_work(self):
        print('''Метод бизнес логики для перехода из состояния `Новый` в `В работе`''')

    @transition(field=state, source=LeadState.STATE_IN_PROGRESS, target=LeadState.STATE_POSTPONED)
    def postpone_work(self):
        print('''Метод бизнес логики для перехода из состояния `В работе` в `Приостановлен`''')

    @transition(field=state, source=LeadState.STATE_IN_PROGRESS, target=LeadState.STATE_DONE)
    def complete_work(self):
        print('''Метод бизнес логики для перехода из состояния `В работе` в `Завершен`''')

    @transition(field=state, source=LeadState.STATE_POSTPONED, target=LeadState.STATE_IN_PROGRESS)
    def resume_work(self):
        print('''Метод бизнес логики для перехода из состояния `Приостановлен` в `В работе`''')

    @transition(field=state, source=LeadState.STATE_POSTPONED, target=LeadState.STATE_DONE)
    def finish_work(self):
        print('''Метод бизнес логики для перехода из состояния `Приостановлен` в `Завершен`''')

    def __str__(self):
        return self.name
