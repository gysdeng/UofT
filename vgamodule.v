module vgamodule
	(
		CLOCK_50,						//	On Board 50 MHz
		// Your inputs and outputs here
        	KEY,
        	SW,
			LEDR,
		// The ports below are for the VGA output.  Do not change.
		VGA_CLK,   						//	VGA Clock
		VGA_HS,							//	VGA H_SYNC
		VGA_VS,							//	VGA V_SYNC
		VGA_BLANK_N,						//	VGA BLANK
		VGA_SYNC_N,						//	VGA SYNC
		VGA_R,   						//	VGA Red[9:0]
		VGA_G,	 						//	VGA Green[9:0]
		VGA_B   						//	VGA Blue[9:0]
	);

	input		CLOCK_50;					//	50 MHz
	input   [9:0]   SW;
	input   [3:0]   KEY;
	output [5:0] LEDR;

	// Declare your inputs and outputs here
	// Do not change the following outputs
	output		VGA_CLK;   				//	VGA Clock
	output		VGA_HS;					//	VGA H_SYNC
	output		VGA_VS;					//	VGA V_SYNC
	output		VGA_BLANK_N;				//	VGA BLANK
	output		VGA_SYNC_N;				//	VGA SYNC
	output	[9:0]	VGA_R;   				//	VGA Red[9:0]
	output	[9:0]	VGA_G;	 				//	VGA Green[9:0]
	output	[9:0]	VGA_B;   				//	VGA Blue[9:0]
	
	wire resetn;
	
	// Create the colour, x, y and writeEn wires that are inputs to the controller.
	wire [2:0] colour;
	wire [7:0] x;
	wire [6:0] y;
	wire writeEn;

	// Create an Instance of a VGA controller - there can be only one!
	// Define the number of colours as well as the initial background
	// image file (.MIF) for the controller.
	vga_adapter VGA(
			.resetn(~resetn),
			.clock(CLOCK_50),
			.colour(drawColor),
			.x(x),
			.y(y),
			.plot(writeEn),
			/* Signals for the DAC to drive the monitor. */
			.VGA_R(VGA_R),
			.VGA_G(VGA_G),
			.VGA_B(VGA_B),
			.VGA_HS(VGA_HS),
			.VGA_VS(VGA_VS),
			.VGA_BLANK(VGA_BLANK_N),
			.VGA_SYNC(VGA_SYNC_N),
			.VGA_CLK(VGA_CLK));
		defparam VGA.RESOLUTION = "160x120";
		defparam VGA.MONOCHROME = "FALSE";
		defparam VGA.BITS_PER_COLOUR_CHANNEL = 1;
		defparam VGA.BACKGROUND_IMAGE = "black.mif";

	// Put your code here. Your code should produce signals x,y,colour and writeEn/plot
	// for the VGA controller, in addition to any other functionality your design may require.
    
	wire [2:0] drawColor;
	assign colour = SW[9:7];
	
	wire [6:0] data;
	assign data = SW[6:0];

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
