from django.test import TestCase

from utils.visualization import print_data_structure


class VisualizationTestCase(TestCase):
    @staticmethod
    def test_visualization() -> None:
        tariff_info = {
            "root": {
                "children": [
                    {
                        "Внутрисетевой роуминг": {
                            "children": [
                                {
                                    "Internet": {
                                        "children": [
                                            "Значение A"
                                        ]
                                    }
                                },
                                {
                                    "MMS": {
                                        "children": [
                                            "Входящие: 0.00",
                                            "Исходящие: 6.45",
                                            {
                                                "Междугородние": {
                                                    "children": [
                                                        "Входящие: 0.00",
                                                        {
                                                            "Исходящие": {
                                                                "children": [
                                                                    "Значение B"
                                                                ]
                                                            }
                                                        }
                                                    ]
                                                }
                                            },
                                            {
                                                "Местные": {
                                                    "children": [
                                                        "Входящие: 0.00"
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "Домашняя сеть": {
                            "children": [
                                {
                                    "Internet": {
                                        "children": [
                                            "Значение C"
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }

        print_data_structure(tariff_info)
