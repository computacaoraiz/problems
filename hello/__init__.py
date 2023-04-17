import check50
import check50.c


@check50.check()
def exists():
    """O arquivo hello.c existe?"""
    check50.exists("hello.c")


@check50.check(exists)
def compiles():
    """Verifica se o arquivo hello.c compila:"""
    check50.c.compile("hello.c", exe_name="hello", cc="gcc", max_log_lines=50, lcs50=True)


@check50.check(compiles)
def emma():
    """Responde corretamente ao nome Emma?"""
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()


@check50.check(compiles)
def rodrigo():
    """Responde corretamente ao nome Rodrigo?"""
    check50.run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit()


@check50.check(compiles)
def abrantes():
    """Responde corretamente ao nome Abrantes?"""
    check50.run("./hello").stdin("Abrantes").stdout("Abrantes").exit()
