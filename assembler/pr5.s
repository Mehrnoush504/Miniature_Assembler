loop 	slt 2,0,1
	beq 2,0,Exit
	add 1,1,0
	addi 0,0,-1
	j loop
Exit 	lw 1,4,-2
	nand 2,3,7
	lui 5,14
MyArray .space 3
	ori 7,9,MyArray