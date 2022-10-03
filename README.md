# APItágoras

<div align="center">
  <p>
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/mariaseverino/apitagoras?color=39C2D8&logoColor=39C2D8&style=for-the-badge">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mariaseverino/apitagoras?color=39C2D8&logoColor=39C2D8&style=for-the-badge">
  </p>
</div>

## ✨ Sobre

Api desenvolvida com python utilizando o fremework Flask e Hospedada no Heroku.

## 🤔 Como Usar
**Api com os parametros:** ```https://maria-apitagoras.herokuapp.com/calcula?a={ladoA}&b={ladoB}&c={ladoC}```

-   A api recebe por parametro os valores dos lados do triangulo

-   A api calcula o valor do lado sem valor do trinagulo e retorna se ele é um triangulo retangulo, o resultado do calculo e o lado que ele representa.

-   Caso tiver alguma tenha alguma errada com a entrada, a api retorna que não e um trinagulo retangulo e qual foi o erro encontrado.


## 🚀 Exemplos de retorno

-   Caso de tudo certo

```json
{
    "resultado": 3.0,
    "retangulo": true,
    "valorQFalta": "c"
}
```

-   Caso tenha inserido valores em todas as entradas ou não tenha inserido uma quantidade suficente de dados

```json
{
    "motivo": "Insira dois valores para calcular o lado que falta!",
    "retangulo": false
}
```

-   Caso algum dos valores seja negativo.

```json
{
    "motivo": "Os valores devem ser maiores que 0!",
    "retangulo": false
}
```

-   Caso o valor de c seja maior que a.

```json
{
    "motivo": "O valor de a deve ser maior que o valor de c.",
    "retangulo": false
}
```

-   Caso o valor de b seja maior que a.

```json
{
    "motivo": "O valor de a deve ser maior que o valor de b.",
    "retangulo": false
}
```
