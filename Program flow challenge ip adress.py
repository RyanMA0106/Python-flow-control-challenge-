print('Hello! this program is used to tell you how many numbers and segments their '
      'are in the ip address that you enter')
IP = input('Ok then, lets start. Please give me a ip address ')
number_of_segment = 1
length_of_segment = 0
character = ''

for character in IP:
    if character == '.':
        print('segment {} contains {} characters'.format(number_of_segment, length_of_segment))
        number_of_segment += 1
        length_of_segment = 0
    else:
        length_of_segment += 1
# unless the final character is a . then it wont print the last segment so this wil solve that
if character != '.':
    print('segment {} contains {} characters'.format(number_of_segment, length_of_segment))
