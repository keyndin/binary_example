import unittest

from Binary import Binary
from BinaryValueException import BinaryValueException


class TestBinaryNumbers(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual('0', Binary(0).get_value())
        self.assertEqual('01', Binary(2).get_value())
        self.assertEqual('001', Binary(4).get_value())
        self.assertEqual('111', Binary(7).get_value())
        self.assertEqual('1001', Binary(9).get_value())
        self.assertEqual('00000000001', Binary(1024).get_value())

    def test_bit_position(self):
        binary = Binary(4)
        self.assertFalse(binary.set_msb().is_lsb())
        self.assertEqual('100', binary.get_value())
        self.assertTrue(binary.set_lsb().is_lsb())
        self.assertEqual('001', binary.get_value())

    def test_msb(self):
        self.assertEqual('0', Binary(0).set_msb().get_value())
        self.assertEqual('10', Binary(2).set_msb().get_value())
        self.assertEqual('100', Binary(4).set_msb().get_value())
        self.assertEqual('10000000000', Binary(1024).set_msb().get_value())

    def test_8_bit(self):
        self.assertEqual('00000000', Binary(0).get_8_bit())
        self.assertEqual('01000000', Binary(2).get_8_bit())
        self.assertEqual('00100000', Binary(4).get_8_bit())
        self.assertRaises(BinaryValueException, Binary(1024).set_msb().get_8_bit)

    def test_16_bit(self):
        self.assertEqual('0000000000000000', Binary(0).get_16_bit())
        self.assertEqual('0100000000000000', Binary(2).get_16_bit())
        self.assertEqual('0010000000000000', Binary(4).get_16_bit())
        self.assertEqual('0000010000000000', Binary(1024).set_msb().get_16_bit())
        self.assertRaises(BinaryValueException, Binary(1200000).set_msb().get_16_bit)


if __name__ == '__main__':
    unittest.main()
