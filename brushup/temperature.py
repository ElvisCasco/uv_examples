def c_to_f(celsius):
    fahrenheit=celsius*9/5+32
    print(str(celsius) + " degrees celsius is equal to " + str(fahrenheit) + " degrees fahrenheit")
    return fahrenheit

def c_to_f_list(celsius):
    fahrenheit=[]
    for i in range(len(celsius)):
        fahrenheit.append(i*9/5+32)
    return fahrenheit

cel=15
c_to_f(cel)
print(c_to_f(cel))
cel_list=[15,32,25]
print(c_to_f_list(cel_list))