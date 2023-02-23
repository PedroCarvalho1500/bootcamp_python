#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
from os.path import exists



if __name__ == '__main__':
    dear_part = ""
    
    with open("Input/Letters/starting_letter.txt",mode='r',encoding='UTF-8') as start_letter:
        #print(f'{start_letter.read()}')
        
        #for line in start_letter:
        #    print(f'{line}')
        dear_part = start_letter.readlines()
        #letter_complete = start_letter.read()
        #dear_part = start_letter.readlines()
        start_letter.close()
        #print(f'{dear_part}')
        
        #print(f'{dear_part[0].strip()}')
        
        with open("Input/Names/invited_names.txt", mode='r', encoding='UTF-8') as names_list:
            names = names_list.readlines()
            #print(f'{names}')

            for name in names:
                #print(f'{name.strip()}')
                
                dear_with_name = dear_part[0].strip().replace('[name]',name.strip())

                existe = exists('Output/ReadyToSend/'+name.strip()+'.txt')
                
                if(not existe):
                    with open('Output/ReadyToSend/'+name.strip()+'.txt',mode='a+', encoding='UTF-8') as new_file:
                        new_file.write(f"{dear_with_name}")
                        new_file.write(f'\nYou are invited to my birthday this Saturday.')
                        new_file.write(f'\nHope you can make it!')
                        new_file.write(f'\nAngela')
                
                
            names_list.close()
        
        #print(f'{letter_complete}')
        