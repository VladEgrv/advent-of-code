target = '7'
list_of_numbers = {
      '1' : ['1', 'one'],
      '2' : ['2', 'two'],
      '3' : ['3', 'three'], 
      '4' : ['4', 'four'], 
      '5' : ['5', 'five'], 
      '6' : ['6', 'six'], 
      '7' : ['7', 'seven'], 
      '8' : ['8', 'eight'], 
      '9' : ['9', 'nine']}
for key, value in list_of_numbers.items():
        if target in value:
            print(key)