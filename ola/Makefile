# ******************************************************************************
# Makefile para o lab "ola", em C, cujo objetivo é imprimir um simples
# "Olá, mundo!" no terminal, e sair com status 0 (zero).
#
# Por: Abrantes Araújo Silva Filho



# ******************************************************************************
# Parâmetros, variáveis e comandos:

LAB = $(notdir $(PWD))
LIMPARCMD=rm -f *~ *.tar



# ******************************************************************************
# Target padrão: compila todos os targets principais, exceto os de limpeza

all: handout handout-tarfile autograder-tarfile



# ******************************************************************************
# Targets principais

# Target handout: cria o diretório LAB-handout, com tudo o que será enviado para
# os estudantes em um arquivo compactado no formato tar. Devem ser incluídos
# aqui tudo o que estudante precisa: "starter files", LEIAME, orientações do lab
# em TXT e/ou PDF, arquivos adicionais, etc. Para organização geral, tais
# arquivos devem ficar no diretório alunos/ (isso separa os arquivos que serão
# entregues aos estudantes dos arquivos que serão apenas do professor).
handout:
	(rm -fr $(LAB)-handout; mkdir $(LAB)-handout)
	cp -p alunos/LEIAME.txt $(LAB)-handout/LEIAME.txt
	cp -p alunos/LEIAME.txt.pdf $(LAB)-handout/LEIAME.pdf
	-cp -p alunos/ola.pdf $(LAB)-handout/ola.pdf
	cp -p alunos/ola.c $(LAB)-handout/ola.c

# Target handout-tarfile: compacta o diretório de handout em um arquivo tar,
# que será disponibilizado aos estudantes.
handout-tarfile: handout
	tar cvf $(LAB)-handout.tar $(LAB)-handout

# Target autograder: gera o arquivo autograder.tar, com o Makefile do
# autograder e outros arquivos necessários. Esses arquivos devem estar dentro
# do diretório "autograder" que, por sua vez, deve conter outros dois
# subdiretórios: "check50" e "grade50" (que conterão os testes a serem
# realizados pelo check50 e a pontuação a ser considerada pelo grade50.
# A Makefile do autograder deve ficar na raiz do diretório "autograder".
autograder-tarfile: $(shell find autograder)
	tar cvf autograder.tar autograder



# ******************************************************************************
# Targets de limpeza (CUIDADO com o apagartudo!)

# Target limpar: limpa toda a árvore do laboratório, de modo seguro. Você pode
# rodar este target (make limpar; make) a qualquer momento, mesmo que o lab já
# esteja liberado para os alunos, sem qualquer problema. Este target apenas
# apaga arquivos de backup do Emacs, arquivos compactados no formato tar e
# outros arquivos e diretório temporários que podem ser gerados novamente
# com o comando make.
limpar:
	$(LIMPARCMD)
	(cd alunos; $(LIMPARCMD))
	(cd autograder; $(LIMPARCMD))
	(cd autograder/check50; $(LIMPARCMD))
	(cd autograder/grade50; $(LIMPARCMD))
	rm -fr $(LAB)-handout

# Target apagartudo: APAGA TODOS OS REGISTROS DOS ESTUDANTES do arquivo
# de log e do diretório handin/. CUIDADO, NUNCA RODE ESTE TARGET DEPOIS QUE
# O LAB ESTÁ LIBERADO PARA OS ESTUDANTES! Este target tem o propósito de
# apagar todo o lab (inclusive todos os arquivos de códigos enviados pelos
# estudantes) para que você possa criar uma NOVA VERSÃO do lab a partir do
# zero. Também pode ser útil quando você está debugando o lab ANTES dele
# ser liberado para os estudantes.
apagartudo:
	make limpar
	rm -f log.txt
	rm -fr handin/*

