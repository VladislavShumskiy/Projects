# Project 1. Анализ резюме на Headhunter


## Содержание
[1. Описание проекта](#Описание-проекта)  
[2. Краткое описание данных](#Краткое-описание-данных)  
[3. Steps in the work on the project](#steps-in-the-work-on-the-project)  
[4. Conclusions](#conclusions)


### Описание проекта
Задача - очистить данные о выложенных на платформе Headhunter резюме, проанализировать их и сделать выводы о состоянии рынка труда.

:arrow_up: [К содержанию](#Содержание)


### Краткое описание данных
Начальные данные представлены в виде csv-файла, содержащего следующие столбцы:
1) Пол, возраст
2) ЗП  
  Желаемая заработная плата
4) Ищет работу на должность:
5) Город, переезд, командировки
  Информация о месте проживания соискателя, и готовности его к переезду и командировкам
5) Занятость
  Информация о желаемом типе занятости (полная занятость, частичная занятость, проектная работа, стажировка, волонтерство)
6) График
  Информация о желаемом графике работы (полный день, сменный график, гибкий график, удаленная работа, вахтовый метод)
7) Опыт работы
8) Последнее/нынешнее место работы
9) Последняя/нынешняя должность
10 Образование и ВУЗ
11 Обновление резюме
  Дата последнего обновления резюме
12 Авто
  Информация о наличии у соискателя личного автомобиля

:arrow_up: [К содержанию](#Содержание)


### Steps in the work on the project
....

:arrow_up: [К содержанию](#Содержание)


### Result
**Algorythms average scores:**
- Random guessing ~ 100
- Improved random guessing ~ 7.5
- Binary search ~ 5.8

:arrow_up: [К содержанию](#Содержание)


### Conclusions
Random guessing takes on average as many tries as there are total possibilities for the correct answer, as expected.
While taking into account the relative position of the answer relative to the guess at each random guess drastically reduces the number of steps required it is still more efficient to use the binary search.

:arrow_up: [К содержанию](#Содержание)

Link to the .csv file:
https://drive.google.com/file/d/1xpi9MRYt0yb_dD8pz0uSTUmgfwe4oWxU/view?usp=sharing

