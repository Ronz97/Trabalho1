import matplotlib.pyplot as plt
import pandas as pd
import sys
import random 
import numpy as np
#Exercicio 1
"""Given two integer numbers return their product only if the product is greater than
1000, else return their sum
"""""

def funcao():
    numero1 = int(input('Digite um Numero => '))
    numero2 = int(input('Digite um Numero => '))

    soma = numero1 + numero2
    produto = numero1 * numero2
    
    if produto > 1000:
        return produto
    else:
       return soma


#Exercicio 2
"""Print the sum of the current number and the previous number"""
def funcao2():
    
    numero = int(input('Numero => '))
    soma = numero + (numero - 1)
    print('A Soma => {} \nNumero Atual => {} \nAntecessor => {} '.format(soma, numero,numero-1))



#Exercicio3
"""Check if the first and last number of a list is the same. Write a function to
return True if the first and last number of a given list is same. If numbers are
different then return False."""

def lista():
    lista = []
    i = 0
    dimensao = int(input('Dimensao : '))
    while i < dimensao:
        numeros = int(input('Digite os valores da lista : '))
        lista.append(numeros)
        i += 1

    if lista[0] == lista[-1]:
        return True
    else:
        return False    


#Exercicio 4
"""Accept numbers from a user. Write a program to accept two numbers from the user
and calculate multiplication."""

def multiplication():
    numero1 = int (input('Digite um Numero => '))
    numero2 = int (input('Digite um Numero => '))
    multiplicação = numero1 * numero2
    return multiplicação
    #print(f'{numero1} * {numero2} = {multiplicação} ')


#Exercicio 5
"""Display numbers from a list using loop. Write a program to display only those
numbers from a list that satisfy the following conditions (Divisivel por 5)"""

def lista2():
 lista = []
 i = 0
 print('------Digite Valores Divisivel por 5--------\n')
 dim = int(input('Digite a Dimensão da lista => '))
    


 while i<dim:
       num = int(input('Digite os Valores => '))
       if num % 5 == 0 :
         lista.append(num)
         i += 1
       #print(i)
       #continue
       else:
          print('\nNão é multiplo de 5\n')
 #print(lista)
 return lista   

    #i += 1


#Exercicio 6
"""Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-
index element from the list l1 and even index elements from the list l2."""
def exe06():
    l1 = []
    l2 = []
    i = 0
    j = 0
    dim = int(input('Digite a Dimensão da lista => '))

    print('\n-----Lista 1---------\n')

    while i < dim:
        num1 = int(input('Digite os Valores => '))
        l1.append(num1)
        i += 1
    print('\n-----Lista 2---------\n')
    while j < dim:
        num2 = int(input('Digite os Valores => '))
        l2.append(num2)
        j += 1

    print('\n-----Listas---------\n')
    print(f'Lista 1 => {l1}')
    print(f'Lista 2 => {l2}')
    print(f'\n-----Lista3---------\n')
#l3 = l1[0] + l2[0]
    l3 = []
    l3.extend(l1[::1])
    l3.extend(l2[-1::1])
    print(f'Lista 3 => {l3}')


#Execicio 7
"""Write a program to remove the item present at index 4 and add it to the 2nd
position and at the end of the list."""
def exe07():
    lista = []
    i = 0
    dim = int(input('Digite a dimensão maior que 4 da lista => '))
    if dim > 4 :
     while i < dim:
         num = input('Inserir os dados => ')
         lista.append(num)
         i += 1


    print('\n------Lista----\n')
    print(lista)
    index = lista[3]
    lista.pop(3)
    print('\n------\n')
    print(f'lista apos eliminacao => {lista} ')
    print(f'Dado Eliminado => {index} ')
    lista.insert(1,index)
    lista.insert(dim,index)
    print('\n----Final----\n')
    #print(lista)
    return lista

#Exercicio 8
"""Checks if one set is a subset or superset of another set. If found, delete all elements
from that set."""
def exe08():
    set1 = set()
    set2 = set()
    print('\n------Set 1-------\n')
    print('OBS => Digite -1 para terminar o Set')
    while True:
        num = int(input('Digite os dados => '))
        if num != -1:
            set1.add(num)
        else:
            break


    print('\n------Set 2-------\n')
    print('OBS => Digite -1 para terminar o Set')
    while True:
        num = int(input('Digite os dados => '))
        if num != -1:
            set2.add(num)
        else:
            break
    print('\n------ Sets ------\n')
    print(f'Set 1 => {set1} ')
    print(f'Set 2 => {set2} ')
    print('-----------------------')

    if set1.issubset(set2) or set1.issuperset(set2):
        print(f'This Set => {set1} is Subset or SuperSet of this Set => {set2}')
        set1.clear()
    #print(f'Set1 => {set1} ')
    else:
        print(f'Set1 "{set1}" não é subset nem superset de "{set2}"  ')        
    print('\n----Final Sets------\n')
    print('Set 1 => ',set1)
    print('Set 2 =>',set2)


#Exercicio 9
"""Create a 5X2 integer array from a range between 100 to 200 such that the difference
between each element is 10."""
def exercicio9():
    matrix = np.arange(100,200,10)
    matrix = matrix.reshape(5,2)
    print('Matriz 5x2 Gerada')
    print(matrix)


#Exercicio 10
"""Create two 2-D arrays and Plot them using matplotlib"""
def exe10():
    x = [1,2,3,4,5,6,7,8,9,10,11]
    y = [1,2,3,4,5,6,7,8,9,10,11]

    plt.scatter(x,y)
    plt.show()
   

#Exercicio 11
"""From the given dataset print the first and last five rows ( YOU SHOULD HAVE THE DATA)."""
def exe11():
    x = pd.read_csv('Automobile_data.csv')
    # primeira linha 
    print('==================================')
    print('1 Rows')
    print(x.head())
    # ultimas 5 linhas
    print('==================================')
    print('last 5 Rows')
    print(x.tail(5))
#exercicio 13
"""Find the most expensive car company name."""
def exe13():
    dataBase = pd.read_csv('Automobile_data.csv')
    header = ['company','price']
    df = pd.DataFrame.from_records(dataBase,columns=header)
    name = ''
    max = 0
    for _, row in df.iterrows():
        if row[1] > max:
            name, max = row[0], row[1]
    return name, max
#Exercicio 14
"""Print All Toyota Cars details."""
def exe14():
    dataBase = pd.read_csv('Automobile_data.csv')
    toyota = dataBase[dataBase['company']=='toyota']
    return toyota
#Exercio 15
"""Count total cars per company"""
def exe15():
    dataBase = pd.read_csv('Automobile_data.csv')
    count = {}
    for _, row in dataBase.iterrows():
        if row[1] in count:
            count[row[1]] += 1
        else:
            count[row[1]] = 1
    return count

#Exercicio 16
"""Find each company’s Higesht price car."""
def exe16():
    df = pd.read_csv("Automobile_data.csv")
    car_Manufacturers = df.groupby('company')
    print(car_Manufacturers['company', 'price'].max())
#Exercicio 17
""" Find the average mileage of each car making company."""
def exe17():
    df = pd.read_csv("Automobile_data.csv")
    car_Manufacturers = df.groupby('company')
    print(car_Manufacturers['company', 'average-mileage'].mean())
#Exercico 18
""" Sort all cars by Price column."""
def exe18():
    dataBase = pd.read_csv('Automobile_data.csv')
    return dataBase.sort_values(by=['price'])
#Exercicio 19
"""Create two data frames using the following two Dicts, Merge two data frames, and 
    append the second data frame as a new column to the first data frame.
    INSTRUCTIONS UNCLEAR(which Dicts??)
    """
def exe19():
    car_Price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
    carPriceDf = pd.DataFrame.from_dict(car_Price)

    car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 80, 182, 160]}
    carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

    print(pd.merge(carPriceDf, carsHorsepowerDf, on="Company"))
#Exercicio 20
"""Read Total profit of all months and show it using a line plot 
   """
def exe20():
    df = pd.read_csv("company_sales_data.csv")
    profitList = df['total_profit'].tolist()
    monthList = df['month_number'].tolist()

    plt.plot(monthList, profitList, label='Month-wise Profit data of last year')
    plt.xlabel('Month number')
    plt.ylabel('Profit in dollar')
    plt.xticks(monthList)
    plt.title('Company profit p/month')
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()

#Exercicio 21
"""Get total profit of all months and show line plot with the following Style properties."""
def exe21():
    df = pd.read_csv("company_sales_data.csv")
    profitList = df['total_profit'].tolist()
    monthList = df['month_number'].tolist()

    plt.plot(monthList, profitList, label='Profit data of last year',
             color='r', marker='o', markerfacecolor='k',
             linestyle='--', linewidth=3)

    plt.xlabel('Months')
    plt.ylabel('Profit in dollar')
    plt.legend(loc='lower right')
    plt.title('Company Sales data of last year')
    plt.xticks(monthList)
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()
#Exercicio 22
"""Read all product sales data and show it using a multiline plot."""
def exe22():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("company_sales_data.csv")
    monthList = df['month_number'].tolist()
    faceCremSalesData = df['facecream'].tolist()
    faceWashSalesData = df['facewash'].tolist()
    toothPasteSalesData = df['toothpaste'].tolist()
    bathingsoapSalesData = df['bathingsoap'].tolist()
    shampooSalesData = df['shampoo'].tolist()
    moisturizerSalesData = df['moisturizer'].tolist()

    plt.plot(monthList, faceCremSalesData, label='Face cream Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, faceWashSalesData, label='Face Wash Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, toothPasteSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, bathingsoapSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, shampooSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, moisturizerSalesData, label='ToothPaste Sales Data', marker='o', linewidth=3)
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.xticks(monthList)
    plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
    plt.title('Sales data')
    plt.show()
#Exercicio 23
"""Read toothpaste sales data of each month and show it using a scatter plot."""
def exe23():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("company_sales_data.csv")
    monthList = df['month_number'].tolist()
    toothPasteSalesData = df['toothpaste'].tolist()

    plt.scatter(monthList, toothPasteSalesData, label='Tooth paste Sales data')
    plt.xlabel('Month Number')
    plt.ylabel('Number of units Sold')
    plt.legend(loc='upper left')
    plt.title(' Tooth paste Sales data')
    plt.xticks(monthList)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.show()
#Exercicio 24
"""Read face cream and facewash product sales data and show it using the bar chart."""
def exe24():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("company_sales_data.csv")
    monthList = df['month_number'].tolist()
    faceCremSalesData = df['facecream'].tolist()
    faceWashSalesData = df['facewash'].tolist()

    plt.bar([a - 0.25 for a in monthList], faceCremSalesData, width=0.25, label='Face cream sales data', align='edge')
    plt.bar([a + 0.25 for a in monthList], faceWashSalesData, width=-0.25, label='Face wash sales data', align='edge')
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.title(' Sales data')

    plt.xticks(monthList)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('Facewash and facecream sales data')
    plt.show()
#Exercicio 25
"""Calculate total sale data for last year for each product and show it using a Pie chart."""
def exe25():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("company_sales_data.csv")
    monthList = df['month_number'].tolist()

    labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
    salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(),
                 df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]

    plt.axis("equal")
    plt.pie(salesData, labels=labels, autopct='%1.1f%%')
    plt.legend(loc='lower right')
    plt.title('Sales data')
    plt.show()

#Exercicio 26
"""Read all product sales data and show it using the stack plot"""
def exe26():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("company_sales_data.csv")
    monthList = df['month_number'].tolist()

    faceCremSalesData = df['facecream'].tolist()
    faceWashSalesData = df['facewash'].tolist()
    toothPasteSalesData = df['toothpaste'].tolist()
    bathingsoapSalesData = df['bathingsoap'].tolist()
    shampooSalesData = df['shampoo'].tolist()
    moisturizerSalesData = df['moisturizer'].tolist()

    plt.plot([], [], color='r', label='face Cream', linewidth=5)
    plt.plot([], [], color='y', label='Face Wash', linewidth=5)
    plt.plot([], [], color='k', label='Bathing soap', linewidth=5)
    plt.plot([], [], color='m', label='Tooth paste', linewidth=5)
    plt.plot([], [], color='c', label='Shampoo', linewidth=5)
    plt.plot([], [], color='g', label='Moisturizer', linewidth=5)

    plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData,
                  bathingsoapSalesData, shampooSalesData, moisturizerSalesData,
                  colors=['r', 'c', 'k', 'm', 'c', 'g'])

    plt.xlabel('Month Number')
    plt.ylabel('Sales unints in Number')
    plt.title('Alll product sales data using stack plot')
    plt.legend(loc='upper left')
    plt.show()

print('\n==================================')
print('1  - Exercicio 1 ')
print('2  - Exercicio 2 ')
print('3  - Exercicio 3 ')
print('4  - Exercicio 4 ')
print('5  - Exercicio 5 ')
print('6  - Exercicio 6 ')
print('7  - Exercicio 7 ')
print('8  - Exercicio 8 ')
print('9  - Exercicio 9 ')
print('10 - Exercicio 10 ')
print('11 - Exercicio 11 ')
print('12 - Exercicio 12 ')
print('13 - Exercicio 13 ')
print('14 - Exercicio 14 ')
print('15 - Exercicio 15 ')
print('16 - Exercicio 16 ')
print('17 - Exercicio 17 ')
print('18 - Exercicio 18 ')
print('19 - Exercicio 19 ')
print('20 - Exercicio 20 ')
print('21 - Exercicio 21 ')
print('22 - Exercicio 22 ')
print('23 - Exercicio 23 ')
print('24 - Exercicio 24 ')
print('25 - Exercicio 25 ')
print('26 - Exercicio 26 ')

print('0  - EXIT ')
print('==================================')
while True:
    x = int(input('Qual vai ser => '))

    if x==1:
        print('\n--------Exercicio 1--------')
        print(funcao())
        print('\n')
        continue
    elif x==2:
        print('\n--------Exercicio 2--------')
        funcao2()
        print('\n')
        #continue
    elif x==3:
        print('\n--------Exercicio 3--------')
        print(lista())
        print('\n')
        #continue
    elif x==4:
        print('\n--------Exercicio 4--------')
        print(multiplication())
        print('\n')
        #continue
    elif x==5:
        print('\n--------Exercicio 5--------')
        print(lista2())
        print('\n')
        #continue
    elif x==6:
        print('\n--------Exercicio 6--------')
        exe06()
        print('\n')
        #continue
    elif x==7:
        print('\n--------Exercicio 7--------')
        print(exe07())
        print('\n')
        #continue
    elif x==8:
        print('\n--------Exercicio 8--------')
        exe08()
        print('\n')
        #continue
    elif x==9:
        print('\n--------Exercicio 9--------')
        exercicio9()
        print('\n')
        #continue
    elif x==10:
        print('\n--------Exercicio 10--------')
        exe10() 
        print('\n')
        #continue
    elif x==11:
        print('\n--------Exercicio 11--------')
        exe11()
        print('\n')
    elif x==12:
        print('\n--------Exercicio 12--------')
        #continue
    elif x==13:
        print('\n--------Exercicio 13--------')
        print(f'----> {exe13()} ')
        print('\n')
    elif x==14:
        print('\n--------Exercicio 14--------')
        print(exe14())
        print('\n')
    elif x==15:
        print('\n--------Exercicio 15--------')
        print(exe15())
        print('\n')
    elif x==16:
        print('\n--------Exercicio 16--------')
        exe16()
        print('\n')
    elif x==17:
        print('\n--------Exercicio 17--------')
        exe17()
        print('\n')
    elif x==18:
        print('\n--------Exercicio 18--------')
        print(exe18())
        print('\n')
    elif x==19:
        print('\n--------Exercicio 19--------')
        exe19()
        print('\n')
    elif x==20:
        print('\n--------Exercicio 20--------')
        print(exe20())
        print('\n')
    elif x==21:
        print('\n--------Exercicio 21--------')
        exe21()
        print('\n')
    elif x==22:
        print('\n--------Exercicio 22--------')
        exe22()
        print('\n')
    elif x==23:
        print('\n--------Exercicio 23--------')
        exe23()
        print('\n')
    elif x==24:
        print('\n--------Exercicio 24--------')
        exe24()
        print('\n')
    elif x==25:
        print('\n--------Exercicio 25--------')
        exe25()
        print('\n')
    elif x==26:
        print('\n--------Exercicio 26--------')
        exe26()
        print('\n')

    else:
        break
        
    
    
    
        
        
