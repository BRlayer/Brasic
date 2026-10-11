import brasic

VERSION = "v1.1"
MANUAL_URL = "https://github.com/BRlayer/Brasic/blob/main/MANUAL.md"

while True:
	print()
	text = input('brasic_console > ')
	print()
	if text.strip() == "": continue

	command = text.upper()

	if command == "SALIR":
		print("Cerrando Brasic...")
		break
	elif command == "AYUDA":
		print(f"Manual de Brasic {VERSION}:")
		print(MANUAL_URL)
		continue
	else:
		result, error = brasic.run('<stdin>', text)

		if error:
			print(error.as_string())
		elif result:
			if len(result.elements) == 1:
				value = result.elements[0]
				if repr(value) != "0":
					print(repr(value))
			else:
				print(repr(result))