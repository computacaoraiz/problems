import check50
import check50.c


@check50.check()
def exists():
    """O arquivo ola.c existe?"""
    check50.exists("ola.c")


@check50.check(exists)
def compiles():
    """Verifica se o arquivo ola.c compila:"""
    check50.c.compile("ola.c", exe_name="ola", cc="gcc", max_log_lines=50, lcs50=True)


@check50.check(compiles)
def uvv():
    """Responde corretamente ao nome UVV?"""
    check50.run("./ola").stdin("UVV").stdout("UVV").exit()


@check50.check(compiles)
def kevin():
    """Responde corretamente ao nome Kevin?"""
    check50.run("./ola").stdin("Kevin").stdout("Kevin").exit()


@check50.check(compiles)
def abrantes():
    """Responde corretamente ao nome Abrantes?"""
    check50.run("./ola").stdin("Abrantes").stdout("Abrantes").exit()
