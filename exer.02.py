horario = input('Digite um horário (0-23):')

if horario.isdigit():
     horario = int(horario)

     if horario < 0 or horario > 23:
             print('Horário deve estar sentre 0 e 23')
     else:
         if horario <= 11:
             print('Bom Dia')
         elif horario <= 17:
            print('Boa tarde')
         else:
             print('Boa noite')
else:
    print('Por favor, digite um horário entre 0 e 23.')
