def pounds_to_kilo(lb):
    return lb * 0.45359237

def pes_e_polegadas_para_m(pe, pol= 0.0):
    return (pe*0.3048) + (pol*0.0254)

def imc_calculo(peso, altura):
    return peso/(altura**2)



print(imc_calculo(peso= pounds_to_kilo(176), altura= pes_e_polegadas_para_m(5, 7)))