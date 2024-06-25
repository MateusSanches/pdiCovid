# Titulo

Detecção de COVID-19 em  Raio-X utilizando descritores de textura GLCM

## Equipe

Mateus Borreiro Sanches RA:1633651

## Repositorio

```bash
https://github.com/MateusSanches/pdiCovid
```


## Link Apresentacao Youtube

```bash
https://youtu.be/oyKkGC8Lslo
```

## Descrição do descritor implementado

-Matriz de Co-ocorrência de Nível de Cinza (GLCM)

A GLCM é um descritor de textura que captura a frequência com que diferentes combinações de níveis de cinza de pixels ocorrem em uma determinada relação espacial na imagem.

A GLCM é gerada computando a frequência de ocorrência de pares de pixels com valores específicos de nível de cinza, separados por uma distância e um ângulo definidos. A partir da GLCM, vários parâmetros estatísticos podem ser calculados, como contraste, correlação, energia e homogeneidade, que são usados como características para a classificação.

## Classificador e acurácia

Classificador: SVC  
Acurácia: 0.98

## Instruções de uso

Rode o comando abaixo no ambiente conda:

```bash
conda install -c conda-forge opencv numpy pandas scikit-image scikit-learn
```

Em seguida rode(O arquivo requirements.txt esta dentro do projeto):

```bash
pip install -r requirements.txt
```

Agora que o ambiente esta configurado, crie uma pasta "entrada" dentro do projeto e extraia as imagens do data-set:

```bash
https://www.kaggle.com/datasets/tarandeep97/covid19-normal-posteroanteriorpa-xrays
```

Note que dentro da pasta entrada deve conter duas outras pastas, uma chamada "covid" e a outra chamada "normal"

Por fim, execute os arquivos com o ambiente configurado na seguinte ordem:

    -extrai.py
    -classificador.py
    -avaliacao.py
