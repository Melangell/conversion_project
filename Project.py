# def binary_conversion(num):
#     binary = ""
#     if num == 0:
#         return 0
#     while num:
#         if num & 1: 
#             binary += "1"
#         else:
#           binary += "0"
#         num >>= 1
#     return binary[::-1]

def binary_conversion(num):
    binary = ""
    while num:
        binary += str(num & 1)
        num >>= 1
    return binary[::-1]

def hexadecimal_conversion(num):
    hexa_dict = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 
                 6:"6", 7:"7", 8:"8", 9:"9",10:"A", 
                 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    hexa = ""
    while num:
        remainder = num % 16
        hexa += hexa_dict[remainder]
        num >>= 4
    return hexa[::-1]

try:
    conversions = ["binary", "hexadecimal", "both"]
    conversion = input("What conversion do you want to perform?(Binary, Hexadecimal or Both) ")
    while conversion not in conversions:
        print("Try again. Check your spellings, pls.")
        conversion = input("What conversion do you want to perform?(Binary, Hexadecimal or Both) ")
    num = int(input("Enter the number to be converted: "))
    assert num > 0
    if conversion.lower() == "binary":
        print(f"The binary of {num} is ", binary_conversion(num))
    elif conversion.lower() == "hexadecimal":
        print(f"The hexadecimal of {num} is ", hexadecimal_conversion(num))
    elif conversion.lower() == "both":
        print(f"The binary and hexadecimal of {num} are", binary_conversion(num),"and", hexadecimal_conversion(num))

except ValueError:
    print("Not a number, buddy😢🙏. Try again.")
except AssertionError:
    print("Zero or Negative numbers are not allowed, buddy🙏. Try again.")
except KeyboardInterrupt:
    print("Keyboard interrupt error.")
except:
    print("Not the right conversion.😢")
print("You're welcome.")