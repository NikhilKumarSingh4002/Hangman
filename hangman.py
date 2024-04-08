call_count=0
def Guess(list,length):
  guess=input("Guess a letter: ").lower()
  for i in range(length):
    if chosen_word[i]==guess:
      list[i]=guess
  print(f"{' '.join(list)}")

def GameOver(list):
  if '_' in list:
    return False
  return True

def checkBlank(list):
  count=0
  for char in list:
    if char=='_':
      count+=1
  return count

def trigger():
  global call_count
  call_count+=1
  if call_count==1:
    return '''
        +---+
        |   |
        O   |
            |
            |
            |
      =========
    '''
  if call_count==2:
    return '''
      +---+
        |   |
        O   |
        |   |
            |
            |
      =========
    '''
  if call_count==3:
    return '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========
    '''
  if call_count==4:
    return '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========
    '''
  if call_count==5:
    return '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      =========
    '''
  if call_count==6:
    return '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========
    '''

from random_word import RandomWords
r=RandomWords()
chosen_word = r.get_random_word()
print(chosen_word)
length=len(chosen_word)
list=[]
lives=0
for i in range(length):
  list.append('_')
print('''
    +---+
    |   |
        |
        |
        |
        |
  =========
''')
while not GameOver(list) and lives!=6:
  blank1=checkBlank(list)
  Guess(list,length)
  blank2=checkBlank(list)
  if blank1==blank2:
    lives+=1
    print(trigger())
if lives==6:
  print("You lost")