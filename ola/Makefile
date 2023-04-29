#
# Makefile para o lab ola
#

# Obtém o nome do lab (através do nome do diretório)
LAB = $(notdir $(PWD))

# Target padrão, que faz o build completo do lab
all: handout handout-tarfile

# Target handout, que faz o build do diretório handout que os estudantes baixam
handout:
	(rm -fr $(LAB)-handout; mkdir $(LAB)-handout)
	cp -p src/LEIAME.txt-handout $(LAB)-handout/LEIAME.txt
	cp -p src/ola.pdf-handout $(LAB)-handout/ola.pdf
	cp -p src/ola.c-handout $(LAB)-handout/ola.c

# Target handout-tarfile, que faz o build do *-handout.tar e autograde.tar
handout-tarfile: handout
	tar cvf $(LAB)-handout.tar $(LAB)-handout
	cp -p $(LAB)-handout.tar autograder.tar

# Target limpa, que limpa toda a árvore do laboratório. Você pode rodar o
# "make limpa; make" a qualquer momento, mesmo que o lab já esteja liberado
# para os alunos, sem qualquer problema.
limpa:
	rm -f *~ *.tar
	(cd src; make limpa)
	(cd test-autograder; make limpa)
	rm -fr $(LAB)-handout
	rm -f autograde.tar

# Target apagartudo, que APAGA TODOS OS REGISTROS DOS ESTUDANTES no arquivo
# de log e do diretório handin/. CUIDADO, nunca rode este target depois que
# o lab está liberado para os estudantes. Este target tem o propósito de
# limpar tudo para que você possa criar uma NOVA VERSÃO do lab a partir do
# zero, ou quando você está debugando o lab ANTES dele ser liberado para
# os estudantes.apagartudo:
	make limpa
	rm -f log.txt
	rm -fr handin/*
