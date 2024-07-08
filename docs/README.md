# makespice
COW용 spice netlist 생성 utility

## usage

~~~
% python3 stackspice.py output_file input_file start_N end_N
~~~

## input file

.subckt subckt pinnames ...
...
.ends

## output

*
x0 pinnames_{start_N} ... subckt
x1 pinnames_1 ... subckt
xN-1 pinnames_{end_N} ... subckt
*
rpinname_0_1 pinname_0 pinname_1 ... ${rvalue}
rpinname_1_2 pinname_1 pinname_2 ... ${rvalue}
...
rpinname_N-2_N-1 pinname_N-2 pinname_N-1 ... ${rvalue}

