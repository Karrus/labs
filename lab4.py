alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' *2 # гаммирование
m = 1096
y = [0]*8
y[0] = 205
a = 9
b = 9
num_word_str =[]
num_word = []
word_encode = []
decode_word = []
word = 'hello'.upper()

for i in word:
    num_word_str.append(alph.index(i)+1)

for i in range(1, len(word)):
    y[i] = (a * y[i-1] + b) % m
print(y)

for i in range(len(num_word_str)):
    num_word.append((y[i] + num_word_str[i])%len(alph))


for i in num_word:
    word_encode.append(alph[i])


word2 = ''.join(word_encode)
print('Гаммирование шифровка: ',word2)



def a(txt, b, op):                     # Гронсфельд
    b *= len(txt) // len(b) + 1
    txt = txt.upper()
    return ''.join([alph[alph.index(j) + int(b[i]) * op] for i, j in enumerate(txt)])
def encrypt(message, key):
    return a(message, key, 4)
print('Шифровка гаммирования, через гронсфельда: ',encrypt(word2, '314141'))

def decrypt(ciphertext, key):
    return a(ciphertext, key, -4)
print('Расшифровка  по гронсфельду: ',decrypt(encrypt(word2, '314141'), '314141')) 

alph1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
num_word_str_decode = []    #гаммирование
num_word_decode = []
for i in word2:
    num_word_str_decode.append(alph1.index(i))


for i in range(len(num_word_str_decode)):
    num_word_decode.append((num_word_str_decode[i]+26 - y[i])%len(alph1))

for i in num_word_decode:
    decode_word.append(alph1[i-1])
print('расшифровка по гаммированию: ',''.join(decode_word))
