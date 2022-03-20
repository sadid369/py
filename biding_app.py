logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)



bider_list =[]
def input_fun ():
    name = input("what is your name? :")
    bid = int( input("what is your bid amount? :"))

def add_name_and_bid_amount(name, amount):
    name = input("what is your name? :")
    bid = int( input("what is your bid amount? :"))
    bider_dictionary ={}
    bider_dictionary["name"] = name
    bider_dictionary["bid"] = amount
    bider_list.append(bider_dictionary)

    
add_name_and_bid_amount(name=name, amount=bid)
    
continue_biding_task = input("Continue 'yes' or 'no")
if continue_biding_task == "yes":
    add_name_and_bid_amount()
elif continue_biding_task == "no":
    continue_biding = False     

print(bider_list)