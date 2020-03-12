import re


class PhoneNumber(object):
    def __init__(self, phone_number):
        numbers_only = "".join([x for x in phone_number if x.isdigit()])
        if numbers_only.startswith('1'):
            numbers_only = numbers_only[1:]
        if not re.match('^[2-9][0-9]{2}[2-9][0-9]{6}$', numbers_only):
            raise ValueError('Formato invalido')
        self.number = numbers_only
        self.area_code = self.number[:3]

    def pretty(self):
        return "({}) {}-{}".format(self.number[:3], self.number[3:6], self.number[6:])
