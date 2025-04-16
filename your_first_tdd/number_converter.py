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
            "thousand", "million", "billion", "trillion"
            ]

class NumberConverter:
    
    def to_words(self, number):
        if number < 20:
            return under_twenty[number]
        decade = number // 10
        units = number % 10
        if units != 0:
            return decades[decade] + "-" + under_twenty[units]
        else:
            return decades[decade]