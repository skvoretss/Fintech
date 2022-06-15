# Построение кривой бенчмарка

Цены свопов взять по ссылке https://www.chathamfinancial.com/technology/european-market-rates#view

Для честной цены однолетнего свопа используется формула: ![\frac{\textmb{Price}}{4}(DF_{3m}+DF_{6m}+DF_{9m}+DF_{12m}](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)

Строится сплайновая интерполяция
