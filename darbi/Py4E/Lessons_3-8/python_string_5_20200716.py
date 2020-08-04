# This script compares an alphabetical order of user's word with word 'banana',
# and writes 'All right, bananas.' if user's word is 'banana'
# Uppercase letters come before lowercase letters.
word= input('Enter word\n')
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')
