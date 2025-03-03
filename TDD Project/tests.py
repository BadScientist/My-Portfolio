import unittest
import datetime
import random
from task import conv_num
from task import my_datetime
from task import conv_endian


class TestCase(unittest.TestCase):

    # Tests whether empty strings return None
    def test_conv_num_01(self):
        num_str = ""
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings with multiple decimal points return None
    def test_conv_num_02(self):
        num_str = "1.2.3"
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether hexadecimal strings with decimal points return None
    def test_conv_num_03(self):
        num_str = "0xA1.2"
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings with non-hexadecimal alpha return None
    def test_conv_num_04(self):
        num_str = "0xA1G2"
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether hexadecimal strings without the proper prefix return None
    def test_conv_num_05(self):
        num_str = "FF"
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether a "prefix-only" string returns None
    def test_conv_num_06(self):
        num_str = "-0x"
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether integers return None
    def test_conv_num_07(self):
        num_str = 123
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether floats return None
    def test_conv_num_08(self):
        num_str = 123.0
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether hexadecimal numbers return None
    def test_conv_num_09(self):
        num_str = 0xFF
        expected = None
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether "0" returns integer 0
    def test_conv_num_10(self):
        num_str = "0"
        expected = 0
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits return the correct integer
    def test_conv_num_11(self):
        num_str = "123"
        expected = 123
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits preceded by '-' return
    # the correct negative integer
    def test_conv_num_12(self):
        num_str = "-123"
        expected = -123
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether "0x0" returns integer 0
    def test_conv_num_13(self):
        num_str = "0x0"
        expected = 0
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits and hexadecimal alpha
    # preceded by "0x" return the proper integer
    def test_conv_num_14(self):
        num_str = "0x2A"
        expected = 42
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits and hexadecimal alpha
    # preceded by "-0x" return the proper negative integer
    def test_conv_num_15(self):
        num_str = "-0x2A"
        expected = -42
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether "0.0" returns the float 0.0
    def test_conv_num_16(self):
        num_str = "0.0"
        expected = 0.0
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits and one decimal point
    # return the correct float
    def test_conv_num_17(self):
        num_str = "6.66"
        expected = 6.66
        self.assertAlmostEqual(
            conv_num(num_str),
            expected,
            msg="Expected {} got {}".format(expected, conv_num(num_str)))

    # Tests whether strings containing only digits and one decimal point
    # preceded by '-' return the correct negative float
    def test_conv_num_18(self):
        num_str = "-6.66"
        expected = -6.66
        self.assertAlmostEqual(
            conv_num(num_str),
            expected,
            msg="Expected {} got {}".format(expected, conv_num(num_str)))

    # Tests whether strings containing only digits and one decimal point
    # with no digits before the decimal return the correct float
    def test_conv_num_19(self):
        num_str = ".666"
        expected = 0.666
        result = conv_num(num_str)
        self.assertEqual(type(result),
                         float,
                         msg="Expected float got {}".format(type(result)))
        self.assertAlmostEqual(
            conv_num(num_str),
            expected,
            msg="Expected {} got {}".format(expected, conv_num(num_str)))

    # Tests whether strings containing only digits and one decimal point
    # with no digits after the decimal return the correct float
    def test_conv_num_20(self):
        num_str = "666."
        expected = 666.0
        result = conv_num(num_str)
        self.assertEqual(type(result),
                         float,
                         msg="Expected float got {}".format(type(result)))
        self.assertAlmostEqual(
            conv_num(num_str),
            expected,
            msg="Expected {} got {}".format(expected, conv_num(num_str)))

    # Tests whether strings containing only digits with leading zeros return
    # the correct integer
    def test_conv_num_21(self):
        num_str = "0123"
        expected = 123
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits with leading zeros
    # preceded by '-' return the correct negative integer
    def test_conv_num_22(self):
        num_str = "-0123"
        expected = -123
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits and hexadecimal alpha
    # with leading zeros preceded by "0x" return the correct integer
    def test_conv_num_23(self):
        num_str = "0x02A"
        expected = 42
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits and hexadecimal alpha
    # with leading zeros preceded by "-0x" return the correct negative integer
    def test_conv_num_24(self):
        num_str = "-0x02A"
        expected = -42
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether strings containing only digits and a single decimal
    # point with leading zeros return the correct float
    def test_conv_num_25(self):
        num_str = "006.6600"
        expected = 6.66
        self.assertAlmostEqual(
            conv_num(num_str),
            expected,
            msg="Expected {} got {}".format(expected, conv_num(num_str)))

    # Tests whether strings containing only digits and a single decimal
    # point with leading zeros preceded by '-' return the correct negative
    # float
    def test_conv_num_26(self):
        num_str = "-006.6600"
        expected = -6.66
        self.assertAlmostEqual(
            conv_num(num_str),
            expected,
            msg="Expected {} got {}".format(expected, conv_num(num_str)))

    # Tests whether strings containing only digits and hexadecimal alpha
    # preceded by "-0x" return the proper negative integer regardless of
    # case of alpha characters
    def test_conv_num_27(self):
        num_str = "-0X2a"
        expected = -42
        self.assertEqual(conv_num(num_str),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         conv_num(num_str)))

    # Tests whether it takes a zero integer
    def test_date_time_01(self):
        num_sec = 0
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests after one leap year has passed
    def test_date_time_02(self):
        num_sec = 123456789
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests up to max date 12-31-9999
    def test_date_time_03(self):
        num_sec = 253402232400
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests end of a year 12-31
    def test_date_time_04(self):
        num_sec = 1072846800
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests beginning of a year 01-01
    def test_date_time_05(self):
        num_sec = 1420135200
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests a leap year month of february 2-29
    def test_date_time_06(self):
        num_sec = 2466612000
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests a leap year month of february 2-28
    def test_date_time_07(self):
        num_sec = 3981290400
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests beginning of a leap year 1-1
    def test_date_time_08(self):
        num_sec = 820519200
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests end of a leap year 12-31
    def test_date_time_09(self):
        num_sec = 4007815200
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests end of a month leap year 6-30
    def test_date_time_10(self):
        num_sec = 3991914000
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests beginning of non-leap year 1-1
    def test_date_time_11(self):
        num_sec = 852141600
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests end of non-leap year 12-31
    def test_date_time_12(self):
        num_sec = 250246605600
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests end of month non-leap year 9-30
    def test_date_time_13(self):
        num_sec = 175574883600
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Random date between years 1970 - 3000
    def test_date_time_14(self):
        num_sec = random.randint(0, 32535147600)
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Random date between years 3001 - 4000
    def test_date_time_15(self):
        num_sec = random.randint(32535234000, 64092142800)
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Random date between years 4001 - 5000
    def test_date_time_16(self):
        num_sec = random.randint(64092229200, 95649051600)
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Random date between 5001 - 6000
    def test_date_time_17(self):
        num_sec = random.randint(95649138000, 127206046800)
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Random date between 6001 - 7000
    def test_date_time_18(self):
        num_sec = random.randint(127206133200, 158762955600)
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Random date between 7001 - 8000
    def test_date_time_19(self):
        num_sec = random.randint(158763042000, 190319950800)
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Random date between 8001 - 9000
    def test_date_time_20(self):
        num_sec = random.randint(190320037200, 221876859600)
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Random date between 9001 - 9999
    def test_date_time_21(self):
        num_sec = random.randint(221876946000, 253402232400)
        expected = datetime.datetime.utcfromtimestamp(num_sec).strftime(
            "%m-%d-%Y")
        self.assertEqual(my_datetime(num_sec),
                         expected,
                         msg="Expected {} got {}".format(expected,
                                                         my_datetime(num_sec)))

    # Tests expected value of passing 954786 and endian 'big'
    def test_conv_endian_1(self):
        num = 954786
        endian = 'big'
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num, endian),
                         expected,
                         msg="Expected {}, got {}".format(expected,
                                                          conv_endian(num,
                                                                      endian)))

    # Tests expected value of passing 954786 and no endian passed
    def test_conv_endian_2(self):
        num = 954786
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num),
                         expected,
                         msg="Expected {}, got {}".format(expected,
                                                          conv_endian(num)))

    # Tests expected value of passing -954786 and no endian passed
    def test_conv_endian_3(self):
        num = -954786
        expected = '-0E 91 A2'
        self.assertEqual(conv_endian(num),
                         expected,
                         msg="Expected {}, got {}".format(expected,
                                                          conv_endian(num)))

    # Tests expected value of passing 954786 and endian 'little'
    def test_conv_endian_4(self):
        num = 954786
        endian = 'little'
        expected = 'A2 91 0E'
        self.assertEqual(conv_endian(num, endian),
                         expected,
                         msg="Expected {}, got {}".format(expected,
                                                          conv_endian(num,
                                                                      endian)))

    # Tests expected value of passing -954786 and endian 'little'
    def test_conv_endian_5(self):
        num = -954786
        endian = 'little'
        expected = '-A2 91 0E'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing -954786 and endian 'little' through
    # argument statement
    def test_conv_endian_6(self):
        expected = '-A2 91 0E'
        self.assertEqual(conv_endian(
            num=-954786, endian='little'),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num=-954786, endian='little')))

    # Tests expected value of passing invalid endian value
    def test_conv_endian_7(self):
        num = -954786
        endian = 'small'
        expected = None
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing invalid endian value
    def test_conv_endian_7b(self):
        num = 954786
        endian = 'large'
        expected = None
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing 0
    def test_conv_endian_8(self):
        num = 0
        expected = '00'
        self.assertEqual(conv_endian(
            num),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(num)))

    # Tests expected value of passing -99999999 and endian 'big'
    def test_conv_endian_9(self):
        num = -99999999
        endian = 'big'
        expected = '-05 F5 E0 FF'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing -99999999 and endian 'little'
    def test_conv_endian_10(self):
        num = -99999999
        endian = 'little'
        expected = '-FF E0 F5 05'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing 99999999 and endian 'big'
    def test_conv_endian_11(self):
        num = 99999999
        endian = 'big'
        expected = '05 F5 E0 FF'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing 99999999 and endian 'little'
    def test_conv_endian_12(self):
        num = 99999999
        endian = 'little'
        expected = 'FF E0 F5 05'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing -1 and endian 'little'
    def test_conv_endian_13(self):
        num = -1
        endian = 'little'
        expected = '-01'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing 1 and endian 'little'
    def test_conv_endian_14(self):
        num = 1
        endian = 'little'
        expected = '01'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing -1 (default big endian)
    def test_conv_endian_15(self):
        num = -1
        expected = '-01'
        self.assertEqual(conv_endian(
            num),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(num)))

    # Tests expected value of passing 1 (default big endian)
    def test_conv_endian_16(self):
        num = 1
        expected = '01'
        self.assertEqual(conv_endian(
            num),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(num)))

    # Tests expected value of passing -9199207 and endian 'little'
    def test_conv_endian_17(self):
        num = -9199207
        endian = 'little'
        expected = '-67 5E 8C'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))

    # Tests expected value of passing 735 and endian 'big'
    def test_conv_endian_18(self):
        num = 735
        endian = 'big'
        expected = '02 DF'
        self.assertEqual(conv_endian(
            num, endian),
            expected,
            msg="Expected {}, got {}".format(expected, conv_endian(
                num, endian)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
