# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

# Метод рисует игровое поле.
def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

# Метод принимает пользовательский ввод и проверяет его корректность.
def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

# Метод проверяет, выиграл ли игрок.
def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

# Мета-метод, объединяющий предыдущие методы для игрового процесса.
def main(board):
    counter = 0 # Установлен счётчик, определяющий кто ходит в конкретный момент цикла игры.
    win = False
    while not win: # Основной цикл игры.
        draw_board(board)
        if counter % 2 == 0: # Первым ходит "крестик" и, соответственно, его ходы соответствуют чётному счётчику.
           take_input("X")
        else:
           take_input("O") # "Нолик" ходит, когда счётчик нечётный.
        counter += 1 # Увеличение счётчика после каждого хода.
        if counter > 4: # После 5-го хода 1-ый игрок сделал 3 отметки - теоретически возможна победа, идёт проверка.
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9: # Если после 9-го хода не определён победитель, то это ничья.
            print("Ничья!")
            break
    draw_board(board)

main(board)

input("Нажмите Enter для выхода")