# Намиране на оптимално разположение на търговски обект

### Оисание на задачата
Целта на задачата е да се намери оптимално разположение и поставяне на реклами по определени пътща на търговски обект, че да генерира максимална печалба за дадена област. Областта е разделена на богати и бедни региони. 

### Решение на проблема
За решаването на този проблем използваме agent-based model (симулация с агенти) за да определим печалбата на търговския обект спрямо неговата локация. Ще използваме опростен модел с надеждата, че достатъчно добре апроксимира реалния свят. Агентите от модела са разделени на 2 типа - богати и бедни, като богатите естествено носят повече печалба, а бедните - по-малко. Движението на агентите се определя с Марковска верига, състоянията на която съответсват на регионите на града или страната в която искаме да оптимизираме. Агентите се движат от регион в регион праволинейно като при преминаването ако видят реклама на търговския обект има вероятност да го посетят. Богатите хора в нашия модел е по-вероятно да се движат между богати региони, а бедните се движат между всички региони с почти еднаква вероятност. За генерирането на Марковската матрица използваме алгоритъма Метрополис-Хастингс. Приемаме, че търговския обект трябва да плаща наем който се изчислява на база колко близко се намира до богатите квартали, а между кои пътища да има реклама се определя от окръжност - ако правата свързваща двата региона попада в окръжността, то има реклама по този път. Така получаваме функцията за печалба  на търговския обект:
profit(cx,cy,cr) = income(cx,cy,cr) - (ad(cr) + rent(cx,cy)). Очевидно се опитваме да максимизираме печалбата, затова решаваме дуалната задача max(profit(cx,cy,cr)) = -min(-profit(cx,cy,cr)). Поведението на функцията е неизвестно, но знаем че е възможно за малки промени по cx, cy и cr да няма промяна в стойността й. За оптимизиране изпозлваме simulated annealing без особени модификации.


### Анализ на поведението на алгоритъма
При еднаква вероятност за преход от богат в беден квартал и на двата типа агенти, и равни печалби които носят на магазина, с малка цена на реклама и малка цена за наем, алгоритъмът намира (минимална) описана окръжност около всички региони. При по голяма цена на рекламата очакваме алгоритъмът да намери някакво оптимално решение което включва повечето пътища между богати региони и е максимално отдалечено от тях. Наистина очакванията ни са оправдани както се вижда на следните картинки:

### Карта преди оптимизация
![карта след оптимизация](https://github.com/randomzy/MonteCarloMethods/blob/master/initial.png)


### Карта след оптимизация
![карта след оптимизация](https://github.com/randomzy/MonteCarloMethods/blob/master/optimized.png)


## Приложение на алгоритъма на друга карта

### Карта преди оптимизация
![карта след оптимизация](https://github.com/randomzy/MonteCarloMethods/blob/master/initial2.png)


### Карта след оптимизация
![карта след оптимизация](https://github.com/randomzy/MonteCarloMethods/blob/master/optimized2.png)


Може би е интиутивно разположението да е в центъра на богатите квартали с такъв радиус, че да обхваща повечето пътища между тя. Ще считаме за наивно решение cx = mean(richAreaX) cy = mean(richAreaY) cr = така че да е минимален, но да обхваща повечето пътища  межуд богати региони.

|Карта|Наивно решение| Оптимизирано решение |
|-|-|-|
|1|2.4745049121191354|3.2954439763466086|
|2|--2.70382551821496|4.636587256438732|

Може да заключим, че оптимизираното решение дава по-добри резултати от наивния подход.
