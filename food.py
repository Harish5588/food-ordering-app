def uber_eats():
  print('welcome user what u want to eat')
  print("welcome to the page")
  print("please enter ur order")
  print("(o)-->order,(p)-->payment,(r)-->report,(e)-->exit")
  a=input("please select one of the option from above mentioned")
  if a=='o':
    def_order()
  elif a=='p':
    def_payment()
  elif a=='r':
    def_report()
  elif a=='e':
    def_exit()
  else:
    print('invalid input,please visit again')
def def_order():
  print("welcome to the orderpage,what would u like to have?")
  print('(f)-->food(),(m)-->menu, (e)-->exit')
  b=input("please select any option from the above list")
  if b=='f':
    def_food_items()
  elif b=='m':
      def_menu()
  elif b=='e':
      def_exit()
  else:
    def_order()
order_list={}
def def_payment():
  print("here is ur total bill")
  print('how would you like to payment cash\n card\n online mode')
  print('you have ordered this things',order_list)
  if len(order_list)>0:
    for key,value in order_list():
      print("and your total payment is:",order_list[key])
      print("and your total bill is :",sum(order_list.values()))
  else:
    print('you have not make any order please make an order!')
def def_report():
  print("rate ur satisafaction with us")
  c=int(input('any digit from 1 to 5'))
  if c==1:
    print("not satified")
  elif c==2:
    print("satisfied normal")
  elif c==3:
    print('satisfied intermediately')
  elif c==4:
    print('good')
  else:
    print("satisfied fully")
def def_exit():
  print('thank you for visiting . visit again to our page')
def def_food_items():
  print("here are the food items")
  d={'biryani':100,'chicken curry':240,'cool_drinks':20}
  print(d['biryani'])


  g=input('enter any key from d to select an item',)
  
def def_menu():
  print('the above is the menu list')
uber_eats()