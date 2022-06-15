# Построение кривой бенчмарка

Цены свопов взять по ссылке https://www.chathamfinancial.com/technology/european-market-rates#view

Для честной цены однолетнего свопа используется формула: 
\[
\frac{\textmb{Price}}{4}(DF_{3m}+DF_{6m}+DF_{9m}+DF_{12m}
\]

Строится сплайновая интерполяция
