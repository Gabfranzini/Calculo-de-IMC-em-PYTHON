nome= input('Qual seu nome?')
peso= int(input('Qual seu peso?'))
altura= float(input('Qual sua altura?'))
imc= peso / (altura*altura)

print('Olá', nome, 'seu imc é:', imc)