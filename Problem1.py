  # klara sameh wadie   20230294
  # katren nader nagy   20230289
#___________________________________

#storing each menu in a variable to be easy to call anytime
menu1=("**numbering system converter**\nA)Insert a new number\nB)Exit program")
menu2=("\n** Please select the base you want to convert a number from **\nA) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal")
menu3=("\n** Please select the base you want to convert a number to **\nA) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal")


#defining functions for each single convertion to easy calling it in need#

#converting decimal into binary
def dec_to_bin(decimal):
      if decimal==0:
          binary=0
      else:
          binary=''
          while decimal > 0:
           remainder = decimal % 2
           binary = str(remainder) + binary
           decimal = decimal // 2
          return binary

#converting decimal into octal
def dec_to_oct(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal = decimal // 8
    return octal

#converting decimal into hexadecimal
def dec_to_hex(decimal):
    hex_digit="0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digit[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

#converting binary into decimal
def bin_to_dec(binary):
    decimal = 0
    for i in range(len(binary)):
      digit = int(binary[-(i+1)])
      decimal+= digit * (2**i)
    return decimal
 
 #converting binary into octal
def bin_to_oct(binary):
    octal=''
    binary='0'*(3-len(binary)%3)+binary
    for i in range(0,len(binary),3):
        octal_digit=int(binary[i:i+3],2)
        octal+=str(octal_digit)
    return octal    

#converting binary into hexadecimal
#it will be in two steps
#1)pad the number with zeros to make the lenght multible of 4
def pad_with_zeros(binary):
    length = len(binary)
    remainder = length % 4
    if remainder != 0:
        padded_length = length + (4 - remainder)
        return '0' * (padded_length - length) + binary
    return binary
#2)converting
def bin_to_hex(binary):
    binary = pad_with_zeros(binary) 

    hex_digits = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    hex = ""
    for i in range(0, len(binary), 4):
        chunk_of_bytes = binary[i:i + 4]
        hex += hex_digits[chunk_of_bytes]
    return hex
    
    

#converting octal into decimal
def oct_to_dec(octal):
    decimal = 0
    position = len(octal) - 1
    for digit in octal:
        decimal += int(digit) * (8 ** position)
        position -= 1
    return decimal

#converting octal into binary
def oct_to_bin(octal):
    decimal=oct_to_dec(octal)
    binary= dec_to_bin(decimal)
    return binary 
    
#converting octal into hexadicemal    
def oct_to_hex(octal):
    binary=oct_to_bin(octal)
    hex=bin_to_hex(binary)
    return hex 

#converting hexadecimal into decimal
def hex_to_dec(hexadecimal):
    dec_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                'C': 12, 'D': 13, 'E': 14, 'F': 15}

    decimal = 0
    hex_len = len(hexadecimal)

    for i in range(hex_len):
        digit=hexadecimal[i]
        decimal+=dec_digit[digit]*16**(hex_len-i-1)
    return decimal

#converting hexadecimal into binary
def hex_to_bin(hexadecimal):
    binary_digit = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    binary = ''
    for digit in hexadecimal:
        binary += binary_digit[digit]
    return binary

#converting hexadecimal into octal
def hex_to_oct(hexadecimal):
    octal_digit = {'000': '0', '001': '1', '010': '2', '011': '3',
                '100': '4', '101': '5', '110': '6', '111': '7'}

    binary = hex_to_bin(hexadecimal)
    while len(binary) % 3 != 0:
        binary = '0' + binary

    octal = ''
    for i in range(0, len(binary), 3):
        octal += octal_digit[binary[i:i+3]]
    return octal


#the main program (showing menues and doing convertions by calling the defined functions above).
def main_program():
 while True:
    print(menu1)
    choice_1=input("Enter your choice(A/B):").upper()
    if choice_1 == "A":
        number = input("Insert the number: ").upper()

        while True:
         print(menu2)
         choice_2 = input("Enter your choice (A/B/C/D): ").upper()
         while True:
          if choice_2 in ['A', 'B', 'C', 'D']:
           while True:
              print(menu3)
              choice_3 = input("Enter your choice (A/B/C/D): ").upper()
              while True:
               if choice_3 in ['A', 'B', 'C', 'D']:
                if choice_2 == 'A' and choice_3 == 'B':
                    result = dec_to_bin(int(number))
                elif choice_2 == 'A' and choice_3 == 'C':
                    result = dec_to_oct(int(number))
                elif choice_2 == 'A' and choice_3 == 'D':
                    result = dec_to_hex(int(number))
                elif choice_2 == 'B' and choice_3 == 'A':
                    result = bin_to_dec(str(number))
                elif choice_2 == 'B' and choice_3 == 'C':
                    result = bin_to_oct(str(number))
                elif choice_2 == 'B' and choice_3 == 'D':
                    result = bin_to_hex(str(number))
                elif choice_2 == 'C' and choice_3 == 'A':
                    result = oct_to_dec(str(number))   
                elif choice_2 == 'C' and choice_3 == 'B':
                    result = oct_to_bin(str(number))  
                elif choice_2 == 'C' and choice_3 == 'D':
                    result = oct_to_hex(str(number))
                elif choice_2 == 'D' and choice_3 == 'A':
                    result = hex_to_dec(str(number))    
                elif choice_2 == 'D' and choice_3 == 'B':
                    result = hex_to_bin(str(number))  
                elif choice_2 == 'D' and choice_3 == 'C':
                    result = hex_to_oct(str(number))     
                else:
                    result = number
                print(f"\nThe result is: {result}\n") 
                main_program()
                
                
            
                
               else:
                print("\nErorr:please select a valid choice.\n")
                print(menu3)
                choice_3 = input("\nEnter your choice (A/B/C/D):").upper()
                
          else:
           print("\nErorr:Please select a valid choice.\n")
           print(menu2)
           choice_2 = input("Enter your choice (A/B/C/D):\n").upper()
          
            
    elif choice_1 == "B":
        print("\nExiting the program...Goodbye!\n")
        break
    
    else:
        print("\nErorr:Please select a valid choice.\n")
        
main_program()