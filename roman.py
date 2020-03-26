
class RomanCalculation(object):
    """
    Handles roman numeral conversion and representation
    """
    def __init__(self, number):
        self.number = int(number)
        self.roman_numeral_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                                  (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def to_roman_numeral(self):
        """
        Convert selected number to roman number
        :return:
        """
        result = ''
        number = int(self.number)

        if number < 0:
            return result

        for (value, roman) in self.roman_numeral_map:
            (factor, number) = divmod(number, value)

            result += str(roman * factor)
            if number == 0:
                break

        return result


if __name__ == '__main__':
    try:
        number_to_convert = input('Enter number to convert: ')
        roman_obj = RomanCalculation(number_to_convert)
        print('Number to convert: {}'.format(number_to_convert))
        print('Roman numeral value: {}'.format(roman_obj.to_roman_numeral()))
    except:
        raise Exception('Enter valid integer')
