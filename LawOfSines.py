import math

# Angle Angle Side
def AAS (A, a, B):
    sinA = math.degrees(math.sin(math.radians(A)))
    sinB = math.degrees(math.sin(math.radians(B)))

    half = a / sinA

    final = half * sinB

    return round(final, 2)

def SSA (A, a, b):
    sinA = math.degrees(math.sin(math.radians(A)))

    half = a / sinA

    final = half * b

    return round(final, 2)
