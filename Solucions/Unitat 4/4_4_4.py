def anagrama (paraula1, paraula2):
    if sorted(paraula1) == sorted(paraula2):
        return True
    return False

print(anagrama("tame", "meta"))
print(anagrama("tame", "mate"))
print(anagrama("tame", "team"))
print(anagrama("tabby", "batty"))
print(anagrama("python", "java")) 