import brasic

while True:
    text = input("Brasic -> ")
    result, error = brasic.run("<stdin>", text)

    if error:
        print(error.as_string())
    else:
        print(result)