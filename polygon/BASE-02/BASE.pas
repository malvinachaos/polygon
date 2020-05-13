PROGRAM MARINA_GAME;

{-------------------------------------~~~ Структуры ~~~--------------------------------------------}
TYPE
Item = RECORD                                       {*---~~~ Список структур ~~~----*}
    Name:string;                                    {| * Item   * Persona   * Floor |}
    Count:byte;                                     {| * Chest  * Block             |}
    Texture:file;                                   {*------------------------------*}
END;

Persona = RECORD
    Name:string;
    Look:file;

    HP, MP, SP, LVL, XP:byte;

    UserInventory: array[1..13] of Item;

    Position: array[1..2] of byte;
END;

Mob = RECORD
    Name:string;
    Look:file;
    
    HP, MP:byte;

    DropItems: array[1..3] of Item;
    Position: array[1..2] of byte;
END;

Floor = RECORD
    Name:string;
    Map: array[1..64, 1..2] of boolean;
    FlooTexture: file;
END;

Chest = RECORD
    DropItems: array[1..5] of Item;
    Texture:file;
    Position: array[1..2] of byte;
END;

Block = RECORD
    Name:string;
    Texture:file;
    Position: array[1..2] of byte;
END;
{-----------------------------------------~~~~ END ~~~~--------------------------------------------}

{-------------------------------~~~~ Процедуры и функции ~~~~--------------------------------------}
(*  ~~~ Список ~~~  *
 *                  *)

{-----------------------------------------~~~~ END ~~~~--------------------------------------------}

{----------------------------------------~~~~ MAIN ~~~~--------------------------------------------}
BEGIN
    while true do
    begin
        writeln('ИГРА');
        break;
    end;
END.
{-----------------------------------------~~~~ END ~~~~--------------------------------------------}
