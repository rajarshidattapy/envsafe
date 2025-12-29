from envsafe import env

print(env.str("API_KEY"))
print(env.bool("DEBUG"))
print(env.int("PORT"))
print(env.list("LIST"))
print(env.json("JSON"))
print(env.int("TIMEOUT"))