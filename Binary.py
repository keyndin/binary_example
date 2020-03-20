from BinaryValueException import BinaryValueException


class Binary:
    __value = "0"  # Binary number, 0 per default
    __msb = False  # Flag whether our number is written as LSB / MSB

    def __init__(self, value):
        """
        Constructor. Takes integer as argument and converts it to Least Significant Bit binary number

        :param value: integer value, will be converted to binary representation
        """
        if value == 0:
            return
        self.__value = ""
        while value > 0:
            self.__value += str(value % 2)
            value = value // 2

    def set_msb(self):
        """
        Fluent setter. Converts number to Most Significant Bit
        """
        if not self.__msb:
            self.__value = self.__value[::-1]
            self.__msb = True
        return self

    def set_lsb(self):
        """
        Fluent setter. Converts number to Least Significant Bit
        """
        if self.__msb:
            self.__value = self.__value[::-1]
            self.__msb = False
        return self

    def get_value(self):
        """
        Returns binary number

        :returns: string representation of binary number
        """
        return self.__value

    def is_lsb(self) -> bool:
        """
        Returns our bit position.

        :returns: `True` if our number is represented as Most Significant Bit, `False` otherwise
        """
        return not self.__msb

    def __get_bits(self, bits):
        """
        Fills number with 0. Takes LSB / MSB into consideration, cuts off numbers that are longer then set bits

        :param bits: bit representation
        :raises BinaryNumberException: will be thrown, if number cannot be represented as set bit position
        :returns: string representation of binary number
        """
        number_len = self.__value.__len__()
        if self.__value.__len__() > bits:
            raise BinaryValueException("Cannot represent number")
        if not self.__msb:
            return self.__value + (bits - number_len) * "0"
        else:
            return (bits - number_len) * "0" + self.__value

    def get_8_bit(self):
        """
        Public wrapper function for __get_bits. Converts binary number to an 8-bit number.

        :raises BinaryNumberException: will be thrown, if number cannot be represented as 8 bit
        :returns: returns 8 bit representation of binary number
        """
        return self.__get_bits(8)

    def get_16_bit(self):
        """
        Public wrapper function for __get_bits. Converts binary number to an 16-bit number.

        :raises BinaryNumberException: will be thrown, if number cannot be represented as 16 bit
        :returns 16 bit representation of binary number
        """
        return self.__get_bits(16)
