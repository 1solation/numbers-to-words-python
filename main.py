# store your number as variable my_number
my_number = 42

# create list of int to string mappings
my_list_ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                10: 'ten'}
my_list_teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                 19: 'nineteen'}
my_list_tens = {20: 'twenty', 30: 'thirty', 40: 'fourty',
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
                90: 'ninety'}

# logid for number 1-19 simple (could have been done in one list)
if 0 <= my_number <= 10:
    print(my_list_ones[my_number])
elif 11 <= my_number <= 19:
    print(my_list_teens[my_number])
# logic for numbers > 20 need modulo to get the tens and remainder, then pass
# these to the respective lists
elif 20 <= my_number <= 99:
    tens, remainder = divmod(my_number, 10)
    print(my_list_tens[tens * 10] + ' ' + my_list_ones[remainder]
          ) if remainder != 0 else print(my_list_tens[tens * 10])
