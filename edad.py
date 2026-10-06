def puede_votar(edad):
    if edad>= 18:
        return "puede votar"
    else:
        return "no puede votar"
print(puede_votar(20))
print(puede_votar(16))

