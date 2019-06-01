	beq 1,2,Plus #
	add 3,5,6    #
	add 3,3,4    #
	j Lab
Plus	add 3,4,5
	sub 3,3,6
	jalr 8,10
Space	.space 5
Zero	.fill -4
Lab	halt

