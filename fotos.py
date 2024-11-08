from engine import reconhece_face, get_rostos
import face_recognition as fr

# Carregar o rosto desconhecido
desconhecido = reconhece_face("./img/desconhecido.jpeg")
if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nomes_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    for i in range(len(rostos_conhecidos)):
        resultado = resultados[i]
        if(resultado):
            print("Rosto do", nomes_dos_rostos[i], "foi reconhecido")
else:
    print("Não foi encontrado nenhum rosto")
