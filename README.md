# Построение кривой бенчмарка

Цены свопов взять по ссылке https://www.chathamfinancial.com/technology/european-market-rates#view

Для честной цены однолетнего свопа используется формула: ![\frac{Price}{4}(DF_{3m}+DF_{6m}+DF_{9m}+DF_{12m}){\color{Cyan}](https://latex.codecogs.com/svg.image?\frac{Price}{4}(DF_{3m}&plus;DF_{6m}&plus;DF_{9m}&plus;DF_{12m}){\color{Cyan})


Строится интерполяция сплайнами
