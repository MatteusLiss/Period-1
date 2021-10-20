järn = 200
silver = 500
guld = 1000
kr = int(input('Hur mycket pengar har du? ->'))
if kr >= guld:
    print('Du har råd med ett guldsmycke')
elif kr >= silver:
    print('Du har råd med ett silversmycke')
elif kr >= järn:
    print('Du har råd med ett järnsmycke')
else:
    print('Du har inte råd med något smycke')