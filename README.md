# Rating Books

Análise exploratória de um acervo de **52.478 livros** raspados do Goodreads (25 colunas, ~74 MB).
O notebook responde a quatro perguntas sobre gêneros, avaliações, autores e preços — e registra o
caminho até cada resposta, incluindo os pontos em que o dado engana.

## As perguntas

1. Quais gêneros têm mais avaliações no total e melhores notas médias?
2. Quais livros são os mais bem avaliados dentro de cada gênero?
3. Quais autores se destacam (melhor nota média) dentro de cada gênero?
4. Quais os livros são mais caros?

## Como rodar

```bash
pip install -r requirements.txt
jupyter lab analise.ipynb
```

O notebook já vem executado, com as tabelas e gráficos salvos. Para gerar as imagens usadas neste
README, basta rodar todas as células — os PNGs são escritos em `images/`.

## Estrutura

```
analise.ipynb                      análise completa, passo a passo
books_1.Best_Books_Ever.csv        base bruta (Goodreads)
images/                            gráficos exportados, usados abaixo
requirements.txt
```

## Resumo dos resultados

### 1. Gêneros com mais avaliações e melhores notas

Fiction, Fantasy e Young Adult lideram em volume — mas os três descrevem boa parte do mesmo
acervo, já que cada livro entra, em média, em **7,8 gêneros**.

![Gêneros com mais avaliações](images/01-generos-avaliacoes.png)

| gênero | avaliações | nota média | livros |
| --- | ---: | ---: | ---: |
| Fiction | 798.727.913 | 3,969 | 30.081 |
| Fantasy | 397.519.302 | 4,015 | 14.328 |
| Young Adult | 335.459.161 | 3,988 | 11.362 |
| Audiobook | 333.774.204 | 3,992 | 7.204 |
| Romance | 324.139.718 | 3,989 | 14.527 |

Quando o critério vira a **nota média** (com um mínimo de 5 livros por gênero), o ranking troca
de cara: sobem nichos como Baha'i, Cartoon Strips e Webcomic — pequenos, coesos e bem avaliados
por públicos específicos.

![Gêneros com melhores notas](images/02-generos-nota-media.png)

| gênero | nota média | avaliações | livros |
| --- | ---: | ---: | ---: |
| Baha'i | 4,625 | 1.588 | 6 |
| Cartoon | 4,474 | 367.823 | 37 |
| Comic Strips | 4,459 | 716.979 | 59 |
| LDS Non Fiction | 4,427 | 161.535 | 29 |
| Scripture | 4,425 | 30.108 | 24 |

### 2. Melhores livros por gênero

Top 3 por nota dentro de cada gênero. O resultado revela o principal limite do critério: sem
filtro de volume, o topo dos "gêneros" mais comuns é ocupado por recortes minúsculos, como
século por século, onde três ou quatro títulos bastam para preencher o pódio.

### 3. Autores que se destacam por gênero

Mínimo de 2 livros por autor dentro do gênero. A figura mostra bem o padrão: pouquíssimos nomes
se repetem por vários recortes ao mesmo tempo.

![Autores por gênero](images/03-autores-por-genero.png)

Destaques: **Bill Watterson** (Calvin and Hobbes, 4,73 em Comics), **Brandon Sanderson** (4,73 em
Novels) e **Elias Zapple** / **Kenneth Thomas**, que aparecem em muitos gêneros — sinal de que
suas obras são marcadas com um leque amplo de tags.

### 4. Livros mais caros

A lista é dominada por **box sets e obras de referência**, não por romances caros: um dicionário
de 20 volumes, coleções de mangá e guias técnicos. O preço mediano do acervo, para comparação, é
de apenas **US$ 5,20**.

![Livros mais caros](images/04-livros-mais-caros.png)

| preço | formato | nota | título |
| ---: | --- | ---: | --- |
| US$ 898,64 | Paperback | 4,11 | I See by My Outfit |
| US$ 867,05 | Hardcover | 4,34 | Margin of Safety |
| US$ 811,04 | Hardcover | 4,41 | V/Crying of Lot 49 / Gravity's Rainbow |
| US$ 796,14 | Paperback | 4,42 | Men's Garments, 1830-1900 |
| US$ 653,73 | Hardcover | 4,72 | The Oxford English Dictionary (20 vol.) |

### Extra — preço, nota e popularidade

![Preço x nota x avaliações](images/05-preco-nota-avaliacoes.png)

Livros mais avaliados tendem a notas mais estáveis; a nota satura entre 3,8 e 4,4 na maior parte
do acervo, e o preço não mostra relação clara com nenhuma das duas.

## Onde estes números merecem desconfiança

- **A soma por gênero conta a mesma avaliação várias vezes.** Um livro com 8 gêneros soma suas
  avaliações 8 vezes, e o total agregado sai cerca de 10x acima do real. Serve para comparar
  gêneros entre si, não como contagem de leitores.
- **A média de nota é não ponderada.** Um livro com 2 avaliações pesa o mesmo que um com 300 mil.
- **O ranking de livros por gênero não filtra por volume.** São 2.444 livros com menos de 10
  avaliações, e 1.346 deles com nota ≥ 4,5.
- **Preço compara edições, não obras.** Box set, paperback e ebook do mesmo título entram na
  mesma lista.
- **Cobertura parcial:** 27,4% do acervo não tem preço, e 81% do catálogo está em inglês.

## Stack

Python 3 · pandas · plotly · Kaleido (exportação das imagens)
