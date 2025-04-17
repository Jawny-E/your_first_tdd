under_twenty = [
                "zero", "one", "two", "three", "four", 
                "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thriteen",
                "fourteen", "fifteen", "sixteen", "seventeen",
                "eighteen", "nineteen"
                ]

decades = [
            "", "", "twenty", "thrity", "fourty", "fifty",
            "sixty", "seventy", "eighty", "ninety"
            ]

thousands = [
            " thousand ", " million ", " billion ", " trillion "
            ]

class NumberConverter:
    def three_numbers_to_words(self, three_digit_number):
        words = ''
        if three_digit_number > 99:
            hundreds = three_digit_number // 100
            three_digit_number = three_digit_number % 100
            words += under_twenty[hundreds] + "-hundred" 
            if three_digit_number > 0:
                words += " and "
            else:
                return words
        if three_digit_number >= 20: 
            decade = three_digit_number // 10
            units = three_digit_number % 10
            if units != 0:
                words += decades[decade] + "-" + under_twenty[units]
            else:
                words += decades[decade]
        if three_digit_number < 20:
            words += under_twenty[three_digit_number]
        return words
        
    def to_words(self, number):
        # Special case
        if number == 0:
            return under_twenty[0]
        else:
            last_three = number % 1000
            number = number // 1000
            words = self.three_numbers_to_words(last_three)
            
            i = 0
            while number > 0:
                last_three = number % 1000
                number = number // 1000
                if last_three != 0:
                    words = self.three_numbers_to_words(last_three) + thousands[i] + "and " + words
                i += 1
            return words
