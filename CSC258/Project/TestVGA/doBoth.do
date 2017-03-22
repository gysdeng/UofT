vlib work

vlog -timescale 1ns/1ns vgamodule.v
vsim testvga

log {/*}
add wave {/*}

# reset all
# KEY0 reset
# KEY3 load
# KEY1 go
# SW[9:7] colour
# SW[6:0] data

force {KEY[3:0]} 1111
force {SW[9:0]} 10'b0
force CLOCK_50 0 0ns, 1 1ns -r 2ns
run 3ns

# reset
force {KEY[0]} 0
run 2ns
force {KEY[0]} 1
run 2ns

# colour
force {SW[9:7]} 3'b001
run 2ns

# x setup + time
force {SW[6:0]} 7'b000_1111
run 2ns

# load to x
force {KEY[3]} 0
run 2ns
force {KEY[3]} 1
run 2ns

# x hold time
run 2ns

# y setup + time
force {SW[6:0]} 7'b111_0000
run 2ns

# load to y and colour
force {KEY[1]} 0
run 2ns
force {KEY[1]} 1
run 2ns

# y hold time + compute
run 50ns