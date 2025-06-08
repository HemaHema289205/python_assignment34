with open('output.txt', 'w') as file:
    file.write(input('Enter text to write to the file: '))
    print('Data successfully written to output.txt.')
    
print()

with open('output.txt', 'a') as file:
    file.write('\n')
    file.write(input('Enter additional text to append: '))
    print('Data successfully appended.')
    
print()

with open('output.txt', 'r') as file:
    print('Final content of output.txt:')
    for line in file.readlines():
        print(line, end = '')
