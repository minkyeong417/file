filename = input('Enter a file name: ')
handle = open(filename,'r')
sumb = 0
count = 0
for str in handle:
    if str.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        index = str.find('0')
        sumb = sumb + float(str[index:])
print('Average spam confidence:',sumb/count)
