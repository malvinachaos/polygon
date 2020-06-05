# <имя кортежа> = (<значения, значения>)
# Их нельзя изменить
dude = ("sudo", "notsudo", 0)
try:
    dude[0] = 9
except:
    print("You can\'t do this\n")
print(dude)

ur = "mom", "gay"
no_u = ()
try:
    no_u[0] = 1488
except:
    print("It\`s illegal\n")

