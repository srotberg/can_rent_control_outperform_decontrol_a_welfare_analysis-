This file shows you how to run the simulations in "The Welfare Consequences of Rent Control", by Shahar Rotberg and Lin Zhang.

Before running each simulation you will have to run the following commands:

Write the command in the line below and press enter:
gfortran welfare_consequences_of_rent_control_Rotberg_Zhang_v1.f90 -I/usr/local/include -lm -mcmodel=medium -fopenmp -g -o welfare_consequences_of_rent_control

Write the command in the line below and press enter:
./welfare_consequences_of_rent_control

At the very top of the Fortran code there is a module titled "Global_Vars". At the top of this module you will see several variables, which we describe below how to set for each simulation.

1. Baseline

	a. Benchmark

		remove_controlled_market=0
        	remove_free_market=0
        	random_assignment=0

        	is_counterfactual=0
             	share_of_free_market_rent=(1-0.69528965484644489)

	b. Full decontrol

		remove_controlled_market=1
        	remove_free_market=0
        	random_assignment=0

        	is_counterfactual=1
             	share_of_free_market_rent=(1-0.69528965484644489)
       
	c. Full tenancy control

		remove_controlled_market=0
        	remove_free_market=1
        	random_assignment=0

        	is_counterfactual=1
             	share_of_free_market_rent=(1-0.69528965484644489)

	d. Welfare-maximizing degree of tenancy control

		remove_controlled_market=0
        	remove_free_market=0
        	random_assignment=0

        	is_counterfactual=1
             	share_of_free_market_rent=0.35

2. Unit control

	remove_controlled_market=0
        remove_free_market=0
       	random_assignment=1

       	is_counterfactual=1
        share_of_free_market_rent=(1-0.69528965484644489)