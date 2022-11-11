a = input()
while a == 'on':
    print('hello im Ilya!')
    b = input('What are you want? Please, enter the command')
    while b!="calculator" and b!="funny words" and b!="mystery quest":
        b = input('What are you want? Please, enter the command')
    if b == 'calculator':
        print('Ok you can start')
        c = input('what action do you want to do?')
        while c!="+" and c!="-" and c!="*" and c!='/' and c!='**' and c!= '//' and c!='%':
            c = input('what action do you want to do?') 
        if c == '+':
            d = float(input('enter the number'))
            e = float(input('enter the scnd number'))
            print(d+e)
            z = input('Are you want contine?')
            while z!="yes" and z!="no":
                z = input('Are you want contine?')
            if z == 'yes':
                c = input('what action do you want to do?')
            elif z == 'no':
                print('ok')
                b = input('please, enter the command')
            else:
                print('unknow command')
                z = input('Are you want contine?')
                while z!="yes" and z!="no":
                    z = input('Are you want contine?')
        elif c == '-':
            d = float(input('enter the number'))
            e = float(input('enter the scnd number'))
            print(d-e)
            z = input('Are you want contine?')
            while z!="yes" and z!="no":
                z = input('Are you want contine?')
            if z == 'yes':
                c = input('what action do you want to do?')
            elif z == 'no':
                print('ok')
                b = input('please, enter the command')
            else:
                print('unknow command')
                z = input('Are you want contine?')
                while z!="yes" and z!="no":
                    z = input('Are you want contine?')
        elif c == '*':
            d = float(input('enter the number'))
            e = float(input('enter the scnd number'))
            print(d*e)
            z = input('Are you want contine?')
            while z!="yes" and z!="no":
                z = input('Are you want contine?')
            if z == 'yes':
                c = input('what action do you want to do?')
            elif z == 'no':
                print('ok')
                b = input('please, enter the command')
            else:
                print('unknow command')
                z = input('Are you want contine?')
                while z!="yes" and z!="no":
                    z = input('Are you want contine?')
        elif c == '/':
            d = float(input('enter the number'))
            e = float(input('enter the scnd number'))
            print(d/e)
            z = input('Are you want contine?')
            while z!="yes" and z!="no":
                z = input('Are you want contine?')
            if z == 'yes':
                c = input('what action do you want to do?')
            elif z == 'no':
                print('ok')
                b = input('please, enter the command')
            else:
                print('unknow command')
                z = input('Are you want contine?')
                while z!="yes" and z!="no":
                    z = input('Are you want contine?')
        elif c == '**':
            d = float(input('enter the number'))
            e = float(input('enter the scnd number'))
            print(d**e)
            z = input('Are you want contine?')
            while z!="yes" and z!="no":
                z = input('Are you want contine?')
            if z == 'yes':
                c = input('what action do you want to do?')
            elif z == 'no':
                print('ok')
                b = input('please, enter the command')
            else:
                print('unknow command')
                z = input('Are you want contine?')
                while z!="yes" and z!="no":
                    z = input('Are you want contine?')
        elif c == '//':
            d = float(input('enter the number'))
            e = float(input('enter the scnd number'))
            print(d//e)
            z = input('Are you want contine?')
            if z == 'yes':
                c = input('what action do you want to do?')
            elif z == 'no':
                print('ok')
                b = input('please, enter the command')
            else:
                print('unknow command')
                z = input('Are you want contine?')
        elif c == '%':
            d = float(input('enter the number'))
            e = float(input('enter the scnd number'))
            print(d%e)
            z = input('Are you want contine?')
            if z == 'yes':
                c = input('what action do you want to do?')
            elif z == 'no':
                print('ok')
                b = input('please, enter the command')
            else:
                print('unknow command')
                z = input('Are you want contine?')
        else:
            print('unknow command')
            c = input('please,repeat')
        
    elif b == 'funny words':
         print('Ok you can start')
         f = input('please, enter the word')
         g = input('please, enter the scnd word')
         print(f+g)
         print('funny isnt it"?')
         z = input('Are you want contine?')
         if z == 'yes':
            c = input('what action do you want to do?')
         elif z == 'no':
            print('ok')
            b = input('please, enter the command')
         else:
                print('unknow command')
                z = input('Are you want contine?')
    elif b == 'mystery quest':
          print('Ok you can start')
          print('You are in a dark room with a monster he wants to eat you. You quickly run into the room you have three options:')
          print('hide under the bed   hide in the closet   hide on the balcon')
          h = input('decide')
          if h == 'hide under the bed':
              print('You are hide under the bed, monster are there, but under the bed very dust, you sneezed and monster found you!')
              print('Game over')
              z = input('Are you want contine?')
              if z == 'yes':
                  print('You are in a dark room with a monster he wants to eat you. You quickly run into the room you have three options:')
                  print('hide under the bed   hide in the closet   hide on the balcon')
                  h = input('decide')
              elif z == 'no':
                print('ok')
                b = input('please, enter the command')
              else:
                  print('unknow command')
                  z = input('Are you want contine?')
          if h == 'hide on the balcon':
              print('You hide on the balcon, but it is transparent and monster found you! So stupid!')
              print('Game over')
              z = input('Are you want contine?')
              if z == 'yes':
                  print('You are in a dark room with a monster he wants to eat you. You quickly run into the room you have three options:')
                  print('hide under the bed   hide in the closet   hide on the balcon')
                  h = input('decide')
              elif z == 'no':
                print('ok')
                b = input('please, enter the command')
              else:
                print('unknow command')
                z = input('Are you want contine?')
          if h == 'hide in the closet':
              print('You hid in the closet, the monster went to the balcony. You quickly ran out, but the monster ran after you. So youve met face to face what will you do:')
              print('run away   move forward confidently   put up a cross')
              i = input('decide')
              if i == 'run away':
                  print('You tried to run away, but the monster caught up with you!')
                  print('Game over')
                  z = input('Are you want contine?')
                  if z == 'yes':
                      print('You hid in the closet, the monster went to the balcony. You quickly ran out, but the monster ran after you. So youve met face to face what will you do:')
                      print('run away   move forward confidently   put up a cross')
                      i = input('decide')
                  elif z == 'no':
                      print('ok')
                      b = input('please, enter the command')
                  else:
                      print('unknow command')
                      z = input('Are you want contine?')
              if i == 'put up a cross':
                  print('You put up a cross, but the monster still ate you (the supernatural must be watched to the end!!!!)!')
                  print('Game over')
                  z = input('Are you want contine?')
                  if z == 'yes':
                      print('You hid in the closet, the monster went to the balcony. You quickly ran out, but the monster ran after you. So youve met face to face what will you do:')
                      print('run away   move forward confidently   put up a cross')
                      i = input('decide')
                  elif z == 'no':
                    print('ok')
                    b = input('please, enter the command')
              if i == 'move forward confidently':
                  print('You decided to come forward, the monster suddenly evaporated, now you are saved!!!')
                  print('Congratulations you won!!!!')
                  z = input('Are you want repeat?')
                  if z == 'yes':
                      print('You are in a dark room with a monster he wants to eat you. You quickly run into the room you have three options:')
                      print('hide under the bed   hide in the closet   hide on the balcon')
                      h = input('decide')
                  elif z == 'no':
                        print('ok')
                        b = input('please, enter the command')
                  else:
                      print('unknow command')
                      z = input('Are you want contine?')
     #elif b == 'one-armed bandit':

        
    