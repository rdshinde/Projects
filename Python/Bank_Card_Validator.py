# Bank card Validaror
# Luhn Algorithm is used to varify the bank card numbers and Government security numbers. This algorithm is also known as 'Modulus 10 Algorithm'.
# In this program Luhn Algorithm is used to check validity of card number.
# Card service provider can be known from first and second digit of card and length of card number.

import threading
from threading import Thread
print("\n\n                              **   BANK CARD NUMBER VALIDATOR.   **\n")
print("------------------------------------------------------------------------------------------------------------------------\n")
class validator:

    def sum_algo(self):
        global sum_oddNum,sum_evenNum,oddNum,evenNum,multiOddNum,cardNum

        cardNum = input('* Enter your card number: ')#.replace(" ","")
        cardNum = cardNum.replace(" ","")
        oddNum = cardNum[::2]
        evenNum = cardNum[1::2]
        multiOddNum = []

        for num in oddNum:
            multiOddNum.append(int(num) * 2)
        sum_evenNum = sum(list(map(int,str(evenNum))))
        sum_oddNum = 0
        for num in multiOddNum:
            if num//10==1 and num!=0:
                sum_oddNum = sum_oddNum+1
            digit = num % 10
            sum_oddNum = sum_oddNum+digit
            num = num//10
#Now validation of card number will be carried out with modulus of 10.
    def validation(self):
        first=int(cardNum[:1])
        second=int(cardNum[1:2])
        if (sum_oddNum+sum_evenNum)%10==0:
            if second==0 and first==6 and len(cardNum)==16:
                print('\n* Card is of RUPAY.')
            elif first==4 and (len(cardNum)==13 or len(cardNum)==16):
                print('\n* Card is of VISA.')
            elif first==5 and len(cardNum)==16:
                print('\n* Card is of MASTERCARD.')
            elif first==3 and (second==4 or second==7) and len(cardNum)==15:
                print('\n* Card is of AMERICAN EXPRESS.')
            elif first==6 and len(cardNum)==16:
                print('\n* Card is of DISCOVER.')
            elif first==3 and (second==0 or second==6 or second==8) and len(cardNum)==14:
                print('\n* Card is of DINNER CLUB.')
        else:
            print('\n\nInvalid Card Number.')
    def response(self):
        global resp,count

        resp = input("\n* Want to try another card number? (y/n)")
        if resp.lower() == 'y':
            validator.sum_algo(self)
            validator.validation(self)
        if resp.lower() == 'n':
            print("\nThank you! Have a nice day!")
            quit()
    def runall(self):
        if __name__ == '__main__':
            Thread(target = self.sum_algo()).start()
            Thread(target = self.validation()).start()
            Thread(target = self.response()).start()


run = validator()
run.runall()
