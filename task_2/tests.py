from django.test import TestCase
from django_fsm import can_proceed

from task_2.models import Lead
from task_2.models import LeadState


class LeadStateTestCase(TestCase):
    def test_lead_state_transitions(self) -> None:
        lead = Lead.objects.create(name='Lead 1')
        self.assertEqual(first=lead.state, second=LeadState.STATE_NEW)  # Проверка начального состояния

        # Проверка возможности перехода из состояния `Новый` в `В работе`
        self.assertEqual(first=can_proceed(lead.start_work), second=True)
        # Проверка возможности перехода из состояния `Новый` в `Приостановлен`
        self.assertEqual(first=can_proceed(lead.postpone_work), second=False)
        # Проверка возможности перехода из состояния `Новый` в `Завершен`
        self.assertEqual(first=can_proceed(lead.complete_work), second=False)

        lead.start_work()
        self.assertEqual(first=lead.state, second=LeadState.STATE_IN_PROGRESS)  # Проверка правильного состояния

        # Проверка возможности перехода из состояния `В работе` в `Приостановлен`
        self.assertEqual(first=can_proceed(lead.postpone_work), second=True)
        # Проверка возможности перехода из состояния `В работе` в `Завершен`
        self.assertEqual(first=can_proceed(lead.complete_work), second=True)
        # Проверка возможности перехода из состояния `В работе` в `В работе`
        self.assertEqual(first=can_proceed(lead.start_work), second=False)

        lead.postpone_work()
        self.assertEqual(first=lead.state, second=LeadState.STATE_POSTPONED)  # Проверка правильного состояния

        # Проверка возможности перехода из состояния `Приостановлен` в `Завершен`
        self.assertEqual(first=can_proceed(lead.finish_work), second=True)
        # Проверка возможности перехода из состояния `Приостановлен` в `В работе`
        self.assertEqual(first=can_proceed(lead.resume_work), second=True)
        # Проверка возможности перехода из состояния `Приостановлен` в `Приостановлен`
        self.assertEqual(first=can_proceed(lead.postpone_work), second=False)
