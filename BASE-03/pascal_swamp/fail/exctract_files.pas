PROGRAM TESTING_FILES;

VAR f: text;
    name: string = 'files/log.log';

BEGIN
    assign(f, name);
    if not fileexists(name) then
        rewrite(f)
    else
        append(f);

    f.write('Hello world!!!!', NewLine, NewLine); {Лучше использовать данную}
                                                  {данную константу вместо  }
                                                  {#13#10 или #10. Путаница }

    close(f);
END.
