# Rating Books

Análise de um acervo de **52.478 livros** raspados do Goodreads (25 colunas, ~74 MB). O notebook
responde a quatro perguntas sobre gêneros, notas, autores e preços — e mostra o caminho até cada
resposta.

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
README, rode todas as células — os PNGs são escritos em `images/`.

## Estrutura

```
analise.ipynb                      análise completa, passo a passo
books_1.Best_Books_Ever.csv        base bruta (Goodreads)
images/                            gráficos exportados, usados abaixo
requirements.txt
```

## Resultados

### 1. Gêneros com mais avaliações e melhores notas

Fiction, Fantasy e Young Adult lideram em volume. Como cada livro entra, em média, em **7,8
gêneros**, esses gêneros acabam se sobrepondo.

![Gêneros com mais avaliações](images/01-generos-avaliacoes.png)

| gênero | avaliações | nota média | livros |
| --- | ---: | ---: | ---: |
| Fiction | 798.727.913 | 3,969 | 30.081 |
| Fantasy | 397.519.302 | 4,015 | 14.328 |
| Young Adult | 335.459.161 | 3,988 | 11.362 |
| Audiobook | 333.774.204 | 3,992 | 7.204 |
| Romance | 324.139.718 | 3,989 | 14.527 |

Quando o critério passa a ser a **nota média** (exigindo pelo menos 5 livros por gênero), a lista
muda: aparecem nichos pequenos e bem avaliados, como Baha I, Cartoon e Comic Strips.

![Gêneros com melhores notas](images/02-generos-nota-media.png)

| gênero | nota média | avaliações | livros |
| --- | ---: | ---: | ---: |
| Baha I | 4,625 | 1.588 | 6 |
| Cartoon | 4,474 | 367.823 | 37 |
| Comic Strips | 4,459 | 716.979 | 59 |
| Lds Non Fiction | 4,427 | 161.535 | 29 |
| Scripture | 4,425 | 30.108 | 24 |

### 2. Melhores livros por gênero

Os três livros de melhor nota nos seis gêneros mais populares. O critério é só a nota; nos
empates, desempato pela quantidade de avaliações. Na figura, cada linha é um gênero, cada coluna
é a posição, e a cor é a nota. Dentro de cada célula estão o título, a nota e o número de
avaliações.

![Livros mais bem avaliados por gênero](images/06-livros-por-genero.png)

| gênero | posição | título | nota | avaliações |
| --- | ---: | --- | ---: | ---: |
| Fiction | 1º | Battle for Erthia | 5,00 | 7 |
| Fiction | 2º | Here Before Kilroy | 5,00 | 2 |
| Fiction | 3º | The Present | 4,92 | 463 |
| Romance | 1º | Battle for Erthia | 5,00 | 7 |
| Romance | 2º | Kiss Me, I'm Irish | 5,00 | 4 |
| Romance | 3º | Shadowed Love | 5,00 | 2 |
| Fantasy | 1º | 16 Myths | 5,00 | 9 |
| Fantasy | 2º | Battle for Erthia | 5,00 | 7 |
| Fantasy | 3º | Bertie's Book of Spooky Wonders | 5,00 | 4 |
| Young Adult | 1º | Battle for Erthia | 5,00 | 7 |
| Young Adult | 2º | The Present | 4,92 | 463 |
| Young Adult | 3º | Maya of the Inbetween | 4,86 | 90 |
| Contemporary | 1º | Truth and Measure | 4,78 | 260 |
| Contemporary | 2º | All the Lies | 4,72 | 5.398 |
| Contemporary | 3º | The 'Burg Series: The Complete Box Set | 4,72 | 1.213 |
| Nonfiction | 1º | A Debt Free You | 4,92 | 12 |
| Nonfiction | 2º | Among the Pigeons | 4,88 | 8 |
| Nonfiction | 3º | Намедни. Наша эра. 1946-1960. | 4,86 | 22 |

Um mesmo livro, **Battle for Erthia**, aparece em primeiro lugar em três gêneros diferentes — sinal
de que as tags de gênero se espalham demais. E boa parte desses livros tem menos de 10 avaliações.

### 3. Autores que se destacam por gênero

Para cada gênero, o autor com a melhor nota média, exigindo pelo menos 2 livros dele no gênero.
Isso evita que alguém com um único livro bem avaliado apareça na frente de quem tem vários.

![Autores por gênero](images/03-autores-por-genero.png)

Os nomes mais conhecidos da lista são **Bill Watterson** (Calvin e Hobbes) e **Brandon Sanderson**.
Já **Elias Zapple** e **Kenneth Thomas** aparecem em muitos gêneros, porque seus livros recebem
várias tags.

### 4. Livros mais caros

A lista é dominada por **box sets e obras de referência** — um dicionário de 20 volumes, coleções
de mangá e guias técnicos. Para comparar, o preço mediano do acervo é de apenas **US$ 5,20**.

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

A nota se concentra entre 3,8 e 4,4 na maior parte do acervo, e o preço não muda muito esse
padrão.

## Onde estes números merecem desconfiança

- **A soma por gênero conta a mesma avaliação várias vezes.** Um livro com 8 gêneros soma suas
  avaliações 8 vezes, e o total fica cerca de 10x maior que o real. Use os valores para comparar
  gêneros entre si, não como contagem de leitores.
- **A média de nota não é ponderada.** Um livro com 2 avaliações pesa o mesmo que um com 300 mil.
- **O ranking de livros por gênero não filtra por volume.** São 2.444 livros com menos de 10
  avaliações, e 1.346 deles com nota ≥ 4,5.
- **O preço compara edições, não obras.** Box set, paperback e ebook do mesmo título entram na
  mesma lista.
- **A cobertura é parcial:** 27,4% do acervo não tem preço, e 81% está em inglês.

## Stack

Python 3 · pandas · plotly · Kaleido (exportação das imagens)
