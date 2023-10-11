class Main_method():
    def __init__(self, arg) -> None:
        self.decimal_num = str(arg)
        self.result = ''
        self.dictionary = {
            0:'&#128512;',
            1:'&#128515;',
            2:'&#128516;',
            3:'&#128513;',
            4:'&#128518;',
            5:'&#128517;',
            6:'&#129315;',
            7:'&#128514;',
            8:'&#128578;',
            9:'&#128579;'

        }

    def transmitation(self):
        for currect_num in self.decimal_num:
            print(currect_num)
            self.result += self.dictionary[int(currect_num)]

    
    def write_to_file(self):
        with open('file.html', 'w') as file:
            file.write(self.result)
            file.close()
    
    def operations(self):
        self.transmitation()
        self.write_to_file()


if __name__ == '__main__':
    while True:
        decimal_num = int(input('Введите число в десятичной системе счисления: '))
        main_class = Main_method(decimal_num)
        main_class.operations()
        break





