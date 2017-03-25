vlib work

vlog -timescale 1ps/1ps vgamodule.v
vsim testvga

log {/*}
add wave {/*}

# reset all
# KEY0 reset
# KEY3 load
# KEY1 go
# SW[9:7] colour
# SW[6:0] data

force {KEY[0]} 1

force CLOCK_50 0 0ps, 1 1ps -r 2ps
run 2ps

force {SW[9:7]} 3'b000
force {KEY[0]} 0
run 50ns