import check50
import check50.c


@check50.check()
def existe():
    """O arquivo ola.c existe?"""
    check50.exists("ola.c")


@check50.check(existe)
def compila():
    """Verifica se o arquivo ola.c compila:"""
    check50.c.CFLAGS={'ggdb':True, 'lm':True, 'std':'c17', 'Wall':True, 'Wpedantic':True}
    check50.c.compile("ola.c", exe_name="ola", cc="gcc", max_log_lines=50, lcs50=True)


@check50.check(compila)
def resposta():
    """Verifica se imprime corretamente a frase 'Olá, mundo!' no terminal,
    com status retorno 0 (zero)."""
    check50.run("./ola").stdout("Olá, mundo!").exit(0)

