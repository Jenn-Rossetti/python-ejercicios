def informe_espia(tira_numeros):

    numeros = tira_numeros.split('-')
    cuartel = int(numeros[-1])
    informe = 0
    for num in numeros[:-1]:
        if int(num) % cuartel == 0:
            informe += int(num)
    print(f"En el cuartel número {cuartel} hay {informe} soldados")
    return (cuartel, informe)





