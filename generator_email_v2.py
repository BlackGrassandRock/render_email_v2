import random
import datetime

def control_panel():
      """панель контроля генерации имейла"""
      NUM_OF_EML = int(input("How many emails do you need to generate? Write a number:\n"))
      settings = int(input("What type of email you will use? Default settings (0) or personal settings(1)?"))
      if settings == 0:
            compos_of_mail = ["character_gnr", 6, "number_gnr", 2, "character_gnr", 3]
      if settings == 1:
            compos_of_mail = []
            set_pers = 0
            while set_pers != 4:
                  set_pers = int(input("What type of sum do you need? Letters(2) or numbers(3)?"))
                  if set_pers == 2:
                        am_sum = int(input("How many letters should be?"))
                        compos_of_mail.append("character_gnr")
                        compos_of_mail.append(am_sum)
                  if set_pers == 3:
                        amount_num = int(input("How many numbers should be?"))
                        compos_of_mail.append("number_gnr")
                        compos_of_mail.append(amount_num)
      amount_email(NUM_OF_EML, compos_of_mail)

def amount_email(NUM_OF_EML, compos_of_mail):
      """установка количества однотипных генеририруемых данных"""
      file_str = ""
      for i in range(NUM_OF_EML):
            mail_sum = clay_symb(compos_of_mail)
            password = passw_gen()
            disp_of_result(i, mail_sum, password)
            file_str += str(mail_sum) + "  " + str(password)+ "\n"
      cr_file(file_str)
            

def clay_symb(compos_of_mail):
      """Объединение символов в почте, в один адрес"""
      mail_sum = ""
      x = len(compos_of_mail)
      for n in range(x-1):
            if compos_of_mail[n] == "character_gnr":
                        mail_sum += character_gnr(compos_of_mail[n+1])
            if compos_of_mail[n] == "number_gnr":
                  mail_sum += number_gnr(compos_of_mail[n+1])
      mail_sum += "@gmail.com"
      return mail_sum
      
def disp_of_result(i, mail_sum, password):
      """отображение сгенерироваванных данных"""
      print(i+1, ") ", mail_sum, "  ", passw_gen())
      

def passw_gen():
      """генерация пароля"""
      password = ""
      for i in range(11):
            x = random.randint(0, 1)
            if x == 0:
                  password += chr(random.randint(ord('A'), ord('z')))
            if x == 1:
                  password += str(random.randint(0, 9))
      return str(password)

def number_gnr(amount_num):
      """генерация случайных чисел"""
      mail = ""
      for i in range(amount_num):
            rand_n = str(random.randint(0, 9))
            mail += rand_n
      return mail

def cr_file(file_str):
      """создание файла с почтами"""
      dt = datetime.datetime.now()
      file = dt.strftime("emails/%d_%m_%y_%H_%M_%S.txt")
      txt = open(file, "w")
      txt.writelines(file_str)
      txt.close

      

def character_gnr(am_sum):
    """генерация случайных букв"""
    rand_f = chr(random.randint(ord('a'), ord('z')))
    mail = rand_f
    

    #Markov chain
    alphabet = {
        "a" : ("n", "t", "l", "r", "s"),
        "b" : ("e", "u", "a", "i"),
        "c" : ("o", "e", "h", "i", "t"),
        "d" : ("e", "a", "i", "u"),
        "e" : ("r", "n", "s", "d", "a"),
        "f" : ("e", "a", "t", "g"),
        "g" : ("e", "h", "o", "l"),
        "h" : ("e", "a", "i", "o"),
        "i" : ("n", "t", "o", "c"),
        "j" : ("a", "e", "i", "o", "u"),
        "k" : ("i", "e", "w", "y"),
        "l" : ("e", "i", "l", "o"),
        "m" : ("e", "a", "i", "o"),
        "n" : ("d", "t", "e", "c"),
        "o" : ("n", "r", "f", "u", "m"),
        "p" : ("a", "i", "o", "w"),
        "q" : "u",
        "r" : ("e", "i", "o", "a"),
        "s" : ("t", "i", "e", "a"),
        "t" : ("h", "i", "e", "o"),
        "u" : ("r", "s", "t", "n"),
        "v" : ("e", "a", "i", "o"),
        "w" : ("a", "i", "h", "o"),
        "x" : ("a", "c", "l", "p"),
        "y" : ("a", "f", "o", "z"),
        "z" : ("a", "l", "h", "e")}
    for i in range(am_sum):
          
        #Learns the length of the chain
        ln_list = len(alphabet[mail[-1]])
        
        #Choosing an element from the chain
        rand_folow = random.randint(0, ln_list - 1)
        
        #Add the next letter
        mail += alphabet[mail[-1]][rand_folow]
    return mail

control_panel()


