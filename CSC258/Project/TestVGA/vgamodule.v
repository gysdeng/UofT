module testvga
	(
		CLOCK_50,						//	On Board 50 MHz
		// Your inputs and outputs here
        	KEY,
        	SW,
		LEDR
	);

	input		CLOCK_50;					//	50 MHz
	input   [9:0]   SW;
	input   [3:0]   KEY;
	output	[5:0]	LEDR;
	
	wire resetn;
	
	// Create the colour, x, y and writeEn wires that are inputs to the controller.
	wire [2:0] colour;
	wire [7:0] x;
	wire [6:0] y;
	wire writeEn;

	wire [2:0] drawColor;
	assign colour = SW[9:7];
	
	wire init, move, finish;
	assign resetn = ~KEY[0];
	
	wire [2:0] curr;

    // Instansiate datapath
	// datapath d0(...);
    datapath d0(
	.resetn(resetn),
	.wren(writeEn),
	.clk(CLOCK_50),
	.init(init),
	.move(move),
	.x(x),
	.y(y),
	.finish(finish)
	);

    // Instansiate FSM control
    // control c0(...);
    control c0(
	.resetn(resetn),
        .clk(CLOCK_50),
	.drawColor(drawColor),
	.colour(colour),
	.wren(writeEn),
	.curr(curr),
	.finish(finish),
	.init(init),
	.move(move)
	);
	
	assign LEDR[2:0] = curr;
    
endmodule
