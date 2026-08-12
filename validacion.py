#Funcion para validar la cedula que tenga 10 sigitos y que sean numéricos

def validar_cedula(cedula):
    if len(cedula) == 10 and cedula.isdigit():
        return True
    else:
        return False

#Función Para validar solo nombres y apellidos que sean alfabéticos y que no contengan números ni caracteres especiales
def validar_nombre_apellido(nombre_apellido):
    if nombre_apellido.isalpha():
        return True
    else:
        return False