import unittest
from unittest.mock import patch
from vehicle_management import Vehicle, Car, Truck, VehicleManager


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("V123", "Toyota", "Corolla", 2020, "Blue", 15.0)

    def test_display_info(self):
        with patch("builtins.print") as mocked_print:
            self.vehicle.display_info()
            mocked_print.assert_any_call("Vehicle ID: V123")

    def test_calculate_fuel_consumed(self):
        self.assertAlmostEqual(self.vehicle.calculate_fuel_consumed(150), 10.0)

    def test_add_service(self):
        self.vehicle.add_service("2024-01-01", "Oil change", 100)
        self.assertEqual(len(self.vehicle.service_history), 1)

    def test_display_service_history(self):
        self.vehicle.add_service("2024-01-01", "Tire change", 200)
        with patch("builtins.print") as mocked_print:
            self.vehicle.display_service_history()
            mocked_print.assert_any_call("Tire change")


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("C001", "Honda", "Civic", 2021, "Red", 20.0, 4, True)

    def test_display_info(self):
        with patch("builtins.print") as mocked_print:
            self.car.display_info()
            mocked_print.assert_any_call("Number of Doors: 4")


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck("T001", "Ford", "F-150", 2019, "Black", 10.0, 1000)

    def test_display_info(self):
        with patch("builtins.print") as mocked_print:
            self.truck.display_info()
            mocked_print.assert_any_call("Payload Capacity: 1000 kg")


class TestVehicleManager(unittest.TestCase):
    def setUp(self):
        self.manager = VehicleManager()
        self.car = Car("C123", "Tesla", "Model S", 2022, "White", 25.0, 4, True)
        self.truck = Truck("T123", "RAM", "1500", 2020, "Gray", 8.0, 2000)
        self.manager.add_vehicle(self.car)
        self.manager.add_vehicle(self.truck)

    def test_add_vehicle(self):
        self.assertEqual(len(self.manager.vehicles), 2)

    def test_remove_vehicle(self):
        self.manager.remove_vehicle("C123")
        self.assertIsNone(self.manager.get_vehicle_by_id("C123"))
