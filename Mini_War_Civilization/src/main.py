import Mini_War_Civilization.src.Civilization as Civilization
import Mini_War_Civilization.src.unit as unit
import sys
import pandas

###################################################################################################
def crear_civilizacion(name: str, resources: int, workers: int, archers: int, cavalry: int, infantry: int) -> Civilization:
    # creamos instancias de civilización
    civ = Civilization.Civilization(name=name, resources=resources, units=[])

    # creamos unidades según la cantidad especificada en el fichero de batalla escogido
    for trabajador in range(0, workers):
        civ.train_unit("Worker")
    for arquero in range(0, archers):
        civ.train_unit("Archer")
    for caballero in range(0, cavalry):
        civ.train_unit("Cavalry")
    for soldado in range(0, infantry):
        civ.train_unit("Infantry")
    return civ

###################################################################################################
def tropas_vivas(trabajadores: list, arqueros: list, caballeros: list, soldados: list, civ: Civilization) -> list:
    """
Clasifica las tropas vivas de la civilización.

    Args:
        trabajadores (list): Lista para almacenar trabajadores vivos.
        arqueros (list): Lista para almacenar arqueros vivos.
        caballeros (list): Lista para almacenar caballeros vivos.
        soldados (list): Lista para almacenar soldados vivos.
        civ (Civilization): Civilización a clasificar.

    Returns:
        list: Listas actualizadas de unidades vivas.
    """
    for unidad in civ.units:
        if unidad.hp > 0:
            unit_info = f"{unidad.name} ({unidad.hp}/{unidad.total_hp})"
            if unidad.unit_type == "Worker":
                trabajadores.append(unit_info)
            elif unidad.unit_type == "Archer":
                arqueros.append(unit_info)
            elif unidad.unit_type == "Cavalry":
                caballeros.append(unit_info)
            elif unidad.unit_type == "Infantry":
                soldados.append(unit_info)

##############################################################################################

def reporte(A: Civilization, B: Civilization) -> str:
    """
Imprime un reporte de la civilización.

    Args:
        A (Civilization): Primera civilización.
        B (Civilization): Segunda civilización.

    Returns:
        str: Reporte de las civilizaciones.
    """
    for civ in [A, B]:
        civ.collect_resources()
        print(civ.name, " Resources: ", civ.resources)
        print()

        # Clasificar las tropas vivas de la civilización

        trabajadores = []
        arqueros = []
        caballeros = []
        soldados = []

        # Enseñar las tropas vivas de la civilización

        tropas_vivas(trabajadores, arqueros, caballeros, soldados, civ)
        print("Worker: ", trabajadores)
        print("Archer: ", arqueros)
        print("Cavalry: ", caballeros)
        print("Infantry: ", soldados)
        print()

    return civ1, civ2

##############################################################################################

def producir_unidad(A: Civilization, B: Civilization) -> tuple:
    """
Produce una unidad para cada civilización.

    Args:
        A (Civilization): Primera civilización.
        B (Civilization): Segunda civilización.

    Returns:
        tuple: Civilizaciones actualizadas.
    """
    for civ in [A, B]:
        if t%4 == 3 and civ.resources < 30:
            print(civ.name, "  cannot create any unit right now.")
        elif (t%4 == 0, 1 or 2) and civ.resources < 60:
            print(civ.name, "  cannot create any unit right now.")
        elif t%4 == 0:
            civ.train_unit("Archer")
            print(civ.name, "  creates ", civ.units[-1])
        elif t%4 == 1:
            civ.train_unit("Cavalry")
            print(civ.name, "  creates ", civ.units[-1])
        elif t%4 == 2:
            civ.train_unit("Infantry")
            print(civ.name, "  creates ", civ.units[-1])
        else:
            civ.train_unit("Worker")
            print(civ.name, "  creates ", civ.units[-1])
    return civ1, civ2

###################################################################################################

def buscar_objetivo(atacante: unit, posibles_objetivos: list) -> unit:
    """
Busca el objetivo más efectivo para el atacante.

    Args:
        atacante (unit): Unidad atacante.
        posibles_objetivos (list): Lista de posibles objetivos.

    Returns:
        unit: Objetivo más efectivo.
    """
    objetivo = None
    valor = -2
    for opcion in posibles_objetivos:
        if atacante.effectiveness(opcion) > valor:
            valor = atacante.effectiveness(opcion)
            objetivo = opcion
    return objetivo

###################################################################################################

def ataque(atacante: unit, ataca: Civilization, defensor: Civilization, datos: list) -> str:
    """
Realiza un ataque de una unidad a otra.

    Args:
        atacante (unit): Unidad atacante.
        ataca (Civilization): Civilización atacante.
        defensor (Civilization): Civilización defensora.
        datos (list): Lista para almacenar los datos del ataque.

    Returns:
        str: Resultado del ataque.
    """
    if atacante.hp == 0:
        return
    else:
        posibles_objetivos = [x for x in defensor.units if x.hp > 0 and x.unit_type != "Worker"]
        objetivo = buscar_objetivo(atacante, posibles_objetivos)
        if objetivo is None:
            posibles_objetivos = [x for x in defensor.units if x.hp > 0 and x.unit_type == "Worker"]
            objetivo = buscar_objetivo(atacante, posibles_objetivos)
            if objetivo is None:
                return
        daño = atacante.attack(objetivo)
        print(ataca.name, "-", atacante.name, " attacks ", defensor.name, "-", objetivo.name, " with damage", daño, " hp = ", objetivo.hp, "/", objetivo.total_hp)
        dato = [atacante.name, atacante.unit_type, ataca.name, objetivo.unit_type, daño]
        datos.append(dato)

###################################################################################################

def batalla(A: Civilization, B: Civilization, datos: list) -> str:
    """
Simula una batalla entre dos civilizaciones.

    Args:
        A (Civilization): Primera civilización.
        B (Civilization): Segunda civilización.
        datos (list): Lista para almacenar los datos de la batalla.

    Returns:
        str: Resultado de la batalla.
    """
    # Filtrar las unidades no debilitadas (hp > 0) y que no sean trabajadores Workers para cada civilización
    a = [x for x in A.units if x.hp > 0 and x.unit_type != "Worker"]
    b = [x for x in B.units if x.hp > 0 and x.unit_type != "Worker"]

    # Filtrar las unidades no debilitadas (hp > 0) que sean trabajadores (Worker)
    w1 = [x for x in A.units if x.hp > 0 and x.unit_type == "Worker"]
    w2 = [x for x in B.units if x.hp > 0 and x.unit_type == "Worker"]

    # Añadir los trabajadores a las listas de unidades no debilitadas

    a += w1
    b += w2

    # Realizar ataques intercalados entre las unidades de ambas civilizaciones

    for atacante1, atacante2 in zip(a,b):
        ataque(atacante1, A, B, datos)
        ataque(atacante2, B, A, datos)
        if A.all_debilitated() == True or B.all_debilitated() == True:
            return
    print()
    # Si una civilización tiene más unidades no debilitadas, realizar ataques adicionales

    if len(a) > len(b):
        print("One civilization has no more attackers left")
        print("The remaining units of the ", civ1.name, " now attack in sequence")
        for atacante in a[len(b):]:
            ataque(atacante, A, B, datos)
            if B.all_debilitated() == True:
                return

    elif len(a) < len(b):
        print("One civilization has no more attackers left")
        print("The remaining units of the ", civ2.name, " now attack in sequence")
        for atacante in b[len(a):]:
            ataque(atacante, B, A, datos)

            if A.all_debilitated() == True:
                return

###################################################################################################

if __name__ == "__main__":

    # Leer el archivo de configuración desde la línea de comandos o usar el predeterminado
    config_file = sys.argv[1] if len(sys.argv) > 1 else "battle0.txt"

    # Intentar abrir el archivo especificado
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo '{config_file}' no existe.", file=sys.stderr)
        sys.exit(1)

    # Resto del código de la simulación...
    print(f"Leyendo configuración desde: {config_file}")

    civ1_data = lines[0].split(":")
    civ1_name = civ1_data[0]
    resources1 = int(civ1_data[1])

    civ2_data = lines[1].split(":")
    civ2_name = civ2_data[0]
    resources2 = int(civ2_data[1])

    turns_line = lines[2]
    parts = turns_line.replace(":", ",").split(",")
    turns = int(parts[1].strip())

    # Leer la cantidad inicial de cada tipo de unidad
    workers_line = lines[3]
    workers = int(workers_line.split(":")[1].strip())

    archers_line = lines[4]
    archers = int(archers_line.split(":")[1].strip())

    cavalry_line = lines[5]
    cavalry = int(cavalry_line.split(":")[1].strip())

    infantry_line = lines[6]
    infantry = int(infantry_line.split(":")[1].strip())

    # Crear instancias de civilización
    print (f"[TODO: Create civilization: {civ1_name} with {resources1} initial resources]")
    print (f"[TODO: Create civilization: {civ2_name} with {resources2} initial resources]")

    # Crear unidades según la cantidad especificada en el fichero de batalla escogido
    print (f"[TODO: Create {workers} workers for {civ1_name}]")
    print (f"[TODO: Create {workers} workers for {civ2_name}]")
    print (f"[TODO: Create {archers} archers for {civ1_name}]")
    print (f"[TODO: Create {archers} archers for {civ2_name}]")
    print (f"[TODO: Create {cavalry} cavalry for {civ1_name}]")
    print (f"[TODO: Create {cavalry} cavalry for {civ2_name}]")
    print (f"[TODO: Create {infantry} infantry for {civ1_name}]")
    print (f"[TODO: Create {infantry} infantry for {civ2_name}]")


civ1 = crear_civilizacion(civ1_name, resources1, workers, archers, cavalry, infantry)
civ2 = crear_civilizacion(civ2_name, resources2, workers, archers, cavalry, infantry)


t = 1
datos = []
# bucle principal de nuestro juego
while t < (turns+1):
    print("Turno: ", t)
    print("Fase 1: Reporte")
    print("--------------------")
    reporte(civ1, civ2)
    print()

    print("Fase 2: Producción")
    print("--------------------")
    producir_unidad(civ1, civ2)
    print()

    print("Fase 3: Batalla")
    print("--------------------")
    batalla(civ1, civ2, datos)
    print()
    if civ1.all_debilitated() == True:
        print(civ2.name, " wins")
        t = turns
    elif civ2.all_debilitated() == True:
        print(civ1.name, " wins")
        t = turns

    t+= 1

if civ1.all_debilitated() != True and civ2.all_debilitated() != True:
    print("Draw")

# creamos un dataframe con los datos de la batalla

data = pandas.DataFrame(datos, columns=["Nombre","Tipo_unidad","Civilización","Tipo_objetivo","Daño"])
print()
print()
# agrupamos por civilización y nombre de la unidad y calculamos la media y la desviación estándar del daño infligido por cada unidad
print ("##################################################################################")
print (" Daño infligido por cada unidad")
print ("##################################################################################\n")
group_col = ["Civilización", "Nombre"]
target_col = "Daño"
data_soldados = data.groupby(group_col).agg({target_col :["mean","std"]})
print(data_soldados)
print()

# agrupamos por civilización y tipo de unidad y calculamos la media y la desviación estándar del daño infligido por cada tipo de unidad
print ("##################################################################################")
print (" Daño infligido por tipo de unidad")
print ("##################################################################################\n")
group_col = ["Civilización", "Tipo_unidad"]
data_tipo_unidades = data.groupby(group_col).agg({target_col :["mean","std"]})
print(data_tipo_unidades)
print()

# agrupamos por civilización, tipo de unidad y tipo de objetivo y calculamos la media y la desviación estándar del daño infligido por cada tipo de unidad a cada tipo de objetivo
print ("###################################################################################")
print (" Daño infligido por tipo de unidad a cada tipo de unidad")
print ("###################################################################################\n")
group_col = ["Civilización", "Tipo_unidad","Tipo_objetivo"]
data_tipo_unidades_vs_tipo_unidades = data.groupby(group_col).agg({target_col :["mean","std"]})
print(data_tipo_unidades_vs_tipo_unidades)