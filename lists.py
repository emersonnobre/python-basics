friends = ["Murilo", "Duda", "Rebecca"]
polymorfism = [1, False, "some text"]
numbers = [1, 34, 2, 1, 0, 34, 4, 100, 98]

#Funções para listas

friends.extend(polymorfism) # adiciona um array no final do array
friends.append("Carlinhos") # adiciona um valor na última posição do array
friends.insert(1, "Doja") # adiciona um valor do index especificado e desloca os demais itens para frente 
friends.remove("Carlinhos") # remove o elemento com o valor especificado, se não encontrar estoura erro
friends.pop() # remove o último valor do array
friends.extend( [1, 1] )
numbers.sort()

print(friends.count(1)) # conta o número de ocorrências do valor passado
print(friends)
print(numbers)