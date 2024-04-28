'''
    Game:
        - welcome message
        - options ----> exit
        - user choice ---> run game
        - ask play again
        - n ---> exit game


            options :
                - multiplication taple
                - sentense ---> no duplicate , redundent =?
'''

class Game:
    def __init__(self):
        print('''welcome
Games:

    1 - Multiplication Taple Game
    2 - Remove Duplicates Game
    3 - Exit 
    ''')

        user_choice = int(input('Enter Game Number : '))
        if user_choice == 1:
            start = int(input('Enter Start Number : '))
            end = int(input('Enter End Number : '))
            self.multiplication_taple(start,end)

        elif user_choice == 2:
            sentence = input('Enter sentence : ')
            self.sentence_duplicate_remover(sentence)

        elif user_choice == 3:
            print("Goodbye...!")
            return
        else:
            print('The Number Error')
            print('*****************')
            print()
            self.__init__()

        play_again = input('Enter Again to play again , Exit to exit ')
        if play_again == 'Again':
           self.__init__() 
        elif play_again == 'Exit':
            print("Goodbye...!")
            return
        else:
            print('The Number Error')
            print('*****************')
            self.play_again
            
        
        
            
        
    def multiplication_taple(self,start,end):
        for number in range(start,end+1):
            for x in range (1,11):
                print(f'{number} X {x} = {number*x}')
                print('------------------')
            print('*******************')

            



    def sentence_duplicate_remover(self,sentence):
        no_duplicate = []

        for word in sentence.split(' '):
            if word not in no_duplicate:
                no_duplicate.append(word)

        new_sentence = ' '.join(no_duplicate)
        redundent = len(sentence.split(' ')) - len(no_duplicate)
        print(new_sentence)
        print(redundent)

g1 = Game()











# sentence_duplicate_remover('my name is is is is mostafa elsakka mostafa elsakka')


