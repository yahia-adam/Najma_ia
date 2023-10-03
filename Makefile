CC	= gcc

SRC =	$(wildcard src/main.c)						\

BIN	= bin/run
BUILD = build

OBJ =$(SRC:.c=.o)
DEP =$(OBJ:.o=.d)  # one dependency file for each source

CFLAGS = -MMD     # option to generate a .d file during compilation
LDFLAGS = -lm

$(BIN):	$(OBJ)
	$(CC) -o $@	$^ $(LDFLAGS)
	@echo "Compiling "$@
	@echo "Build successful!"

-include $(DEP)   # include all dep files in the makefile

.PHONY: clean
clean:
	rm -f $(OBJ) $(BIN)

.PHONY: cleandep
cleandep:
	rm -f $(DEP)
