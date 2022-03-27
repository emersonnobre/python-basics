is_male = False
is_tall = False

if is_male and is_tall:
    print("Youre a tall male")
elif is_male and not(is_tall):
    print("Youre a short male")
elif not(is_male) and is_tall:
    print("You arent a male but are tall")
else:
    print("You arent a male and arent tall")