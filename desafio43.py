n1 = float(input('Digite sua altura: '))
n2 = float(input('Digite o seu peso atual: '))
imc = n2 / (n1 * n1)

if imc < 18.5:
    print('Você está abaixo do seu peso ideal!')

elif (imc >= 18.5 and imc <= 25):
    print('Parabéns! Você está no seu peso ideal!!!')

if (imc >= 25 and imc <= 30):
    print('Muita ATENÇÃO! Você está com sobrepeso.')

elif (imc >= 30 and imc <= 40):
    print('ATENÇÃO REDOBRADA! Você está com o quadro de OBESIDADE!!!')

if imc > 40:
    print('MUITA ATENÇÃO!!! Você está com o quadro de OBESIDADE MÓRBIDA!!!!')



