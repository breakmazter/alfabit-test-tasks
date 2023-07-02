from django.test import TestCase

from task_1.models import DeliveryState


class DeliveryStateTestCase(TestCase):
    def setUp(self) -> None:
        for name, value in DeliveryState.__dict__.items():
            if 'STATE_' in name:
                DeliveryState.objects.create(pk=value)

    def test_delivery_state_methods(self) -> None:
        self.assertEqual(
            first=DeliveryState.get_new(),
            second=DeliveryState.objects.get(pk=DeliveryState.STATE_NEW),
        )
        self.assertEqual(
            first=DeliveryState.get_issued(),
            second=DeliveryState.objects.get(pk=DeliveryState.STATE_ISSUED),
        )
        self.assertEqual(
            first=DeliveryState.get_delivered(),
            second=DeliveryState.objects.get(pk=DeliveryState.STATE_DELIVERED),
        )
        self.assertEqual(
            first=DeliveryState.get_handed(),
            second=DeliveryState.objects.get(pk=DeliveryState.STATE_HANDED),
        )
        self.assertEqual(
            first=DeliveryState.get_refused(),
            second=DeliveryState.objects.get(pk=DeliveryState.STATE_REFUSED),
        )
        self.assertEqual(
            first=DeliveryState.get_paid_refused(),
            second=DeliveryState.objects.get(pk=DeliveryState.STATE_PAID_REFUSED),
        )
        self.assertEqual(
            first=DeliveryState.get_complete(),
            second=DeliveryState.objects.get(pk=DeliveryState.STATE_COMPLETE),
        )
        self.assertEqual(
            first=DeliveryState.get_none(),
            second=DeliveryState.objects.get(pk=DeliveryState.STATE_NONE),
        )
