import cv2
import pandas as pd
from skimage.feature import graycomatrix, graycoprops, local_binary_pattern
from skimage.measure import label, regionprops
from sklearn.model_selection import train_test_split
import numpy as np

dados_completos = []
dado = pd.read_csv("Leaves/all.csv")
for _, linhas in dado.iterrows():
    # Imagem
    nome = linhas["id"]
    classe = linhas["y"]
    img = cv2.imread("Leaves/" + nome, 0)
    if img is None:
        continue
    # GLCM
    glcm = graycomatrix(
        img, distances=[1], angles=[0], levels=256, symmetric=True, normed=True
    )
    dissimilaridade = graycoprops(glcm, "dissimilarity")[0, 0]
    correlação = graycoprops(glcm, "correlation")[0, 0]
    homogeneidade = graycoprops(glcm, "homogeneity")[0, 0]
    asm = graycoprops(glcm, "ASM")[0, 0]
    energia = np.sqrt(asm)
    # LBP
    lbp_imagem = local_binary_pattern(img, P=8, R=1, method="uniform")
    histograma, _ = np.histogram(lbp_imagem, bins=10, range=(0, 10), density=True)
    # 7 momentos de Hu
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    _, binario = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    momentos = cv2.moments(binario)
    hu = cv2.HuMoments(momentos).flatten()
    hu_log = -np.sign(hu) * np.log10(np.abs(hu) + 1e-15)

    # Atributos de forma
    rotulado = label(binario)
    propriedades = regionprops(rotulado)
    if len(propriedades) == 0:
        excentricidade = 0
        razão_aspecto = 1
        alongamento = 0
        solidez = 1
        fator_isoperimetrico = 0
        convexidade = 1
    else:
        folha = max(propriedades, key=lambda x: x.area)
        # Exentricidade
        excentricidade = folha.eccentricity
        # Razão de aspecto
        min_row, min_col, max_row, max_col = folha.bbox
        altura = max_row - min_row
        largura = max_col - min_col
        razão_aspecto = altura / largura if largura > 0 else 1
        # Alongamento
        r_circunscrito = folha.equivalent_diameter / 2
        mapa_distancia = cv2.distanceTransform(binario, cv2.DIST_L2, 5)
        _, r_inscrito, _, _ = cv2.minMaxLoc(mapa_distancia)
        alongamento = 1 - (r_inscrito / r_circunscrito) if r_circunscrito > 0 else 0
        # Solidez
        solidez = folha.solidity
        # Fator Isoperimetrico
        area = folha.area
        perimetro = folha.perimeter
        fator_isoperimetrico = (
            (4 * np.pi * area) / (perimetro**2) if perimetro > 0 else 0
        )
        # Convexidade
        contornos, _ = cv2.findContours(
            binario, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        if len(contornos) > 0:
            maior_contorno = max(contornos, key=cv2.contourArea)
            casco = cv2.convexHull(maior_contorno)
            p_casco = cv2.arcLength(casco, True)
            p_contorno = cv2.arcLength(maior_contorno, True)
            convexidade = p_casco / p_contorno if p_contorno > 0 else 1
        else:
            convexidade = 1
    # Registrar
    registro = {
        "id": nome,
        "y": classe,
        "glcm_dissimilaridade": dissimilaridade,
        "glcm_correlação": correlação,
        "glcm_homogeneidade": homogeneidade,
        "glcm_ASM": asm,
        "glcm_energia": energia,
        "forma_excentricidade": excentricidade,
        "forma_razão_aspecto": razão_aspecto,
        "forma_alongamento": alongamento,
        "forma_solidez": solidez,
        "forma_fator_isoperimetrico": fator_isoperimetrico,
        "forma_convexidade": convexidade,
    }
    for i in range(10):
        registro[f"lbp{i}"] = histograma[i]
    for i in range(7):
        registro[f"momentos de hu {i+1}"] = hu_log[i]
    dados_completos.append(registro)
df_features = pd.DataFrame(dados_completos)
df_features.to_csv("Atributos.csv", index=False)
