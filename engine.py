import face_recognition as fr

# Função para reconhecer rosto em uma imagem
def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto, model="cnn")  # Usando o modelo CNN para detecção de rostos
    if len(rostos) > 0:
        return True, rostos
    return False, []

# Função para obter rostos conhecidos
def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    # Chama a função para reconhecer os rostos nas imagens
    roger1 = reconhece_face("./img/robertfoto.jpg")
    annanda1 = reconhece_face("./img/annanda.jpeg")
    ana1 = reconhece_face("./img/ana.jpeg")
    ulisses1 = reconhece_face("./img/ulisses.jpeg")
    luana1 = reconhece_face("./img/luana.jpeg")
    # Verifica se o rosto do Robert foi reconhecido
    if roger1[0]:
        rostos_conhecidos.append(roger1[1][0])
        nomes_dos_rostos.append("Robert")
    if ana1[0]:
        rostos_conhecidos.append(ana1[1][0])
        nomes_dos_rostos.append("Ana")
    # Verifica se o rosto da Annanda foi reconhecido
    if annanda1[0]:
        rostos_conhecidos.append(annanda1[1][0])
        nomes_dos_rostos.append("Annanda")
    if ulisses1[0]:
        rostos_conhecidos.append(ulisses1[1][0])
        nomes_dos_rostos.append("Ulisses")   
    if luana1[0]:
        rostos_conhecidos.append(luana1[1][0])
        nomes_dos_rostos.append("Luana")
    return rostos_conhecidos, nomes_dos_rostos
