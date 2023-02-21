from Ciphertext import Ciphertext

if __name__ == "__main__":
    ciphertext = Ciphertext('abc def')
    print(ciphertext.__str__())
    print(ciphertext.__len__())
    print(ciphertext.__len__(exclude=' '))
