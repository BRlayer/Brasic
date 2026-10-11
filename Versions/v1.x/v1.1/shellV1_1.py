import brasicV1_1

VERSION = "v1.1"
MANUAL_URL = "PEGA_AQUI_EL_ENLACE_DEL_MANUAL"

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
		result, error = brasicV1_1.run('<stdin>', text)

		if error:
			print(error.as_string())
		elif result:
			if len(result.elements) == 1:
				value = result.elements[0]
				if repr(value) != "0":
					print(repr(value))
			else:
				print(repr(result))