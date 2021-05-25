BEGIN
    WriteLn('ЛЕН' > 'ЛЁН'); {True, 'Ё' в Unicode идёт перед 'А'                }
    WriteLn('лен' > 'лён'); {False, 'ё' в Unicode идёт после 'я'               }
    WriteLn('Дерево' <= 'дуб'); {True, так как прописные буквы меньше строчных }

END.
