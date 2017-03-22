module control(
	input resetn,
	input clk,
	output reg [2:0] drawColor,
	input [2:0] colour,
	output reg wren,
	output reg [2:0] curr,
	input finish,
	output reg init,
	output reg move
	);

    // reg [2:0] curr, next;
    reg [2:0] next;
    reg refresh;

    reg [18:0] onesixty;
    reg [5:0] frames;

    // 1/60 clock + framerate clock
    always @(posedge clk)
    begin
	if(resetn == 1) begin
	    onesixty <= 19'd83_3333;
	    frames <= 6'd60;
		
		 curr<=INIT;
	    end
	else begin
	    onesixty <= onesixty - 1'b1;
		 curr <= next;
	    end
	if(onesixty == 19'b0) begin
	    onesixty <= 19'd83_3333;
		 frames <= frames - 1'b1;
		 end
	if(frames == 6'b0) begin
	    frames <= 6'd60;
	    refresh <= 1'b1;
	    end
		 
	   
	if(curr == MOVE || curr == WAIT)
	    refresh <= 1'b0;
   
	 
	end // end always clock

    localparam	INIT	= 3'd0,
		DRAW	= 3'd1,
		ERASE	= 3'd2,
		MOVE	= 3'd3,
		WAIT    = 3'd4;

    always @(*)
    begin: state_table
	case(curr)
	    INIT: next = refresh? ERASE: INIT;
	    ERASE: next = finish? MOVE : ERASE;
	    MOVE: next = DRAW;
	    DRAW: next = finish? WAIT: DRAW; 
	    WAIT: next = refresh? ERASE: WAIT; 
	    default: next = INIT;
	endcase
    end

    always @(*)
    begin: signals
	wren = 1'b0;
	init = 1'b0;
	move = 1'b0;
	drawColor = 3'b000;
	case(curr)
	    INIT: begin wren = 1'b1; init = 1'b1; drawColor = colour; end
	    ERASE: begin wren = 1'b1; drawColor = 3'b000; end
	    MOVE: move = 1'b1;
	    DRAW: begin wren = 1'b1; drawColor = colour; end
		 
	endcase
    end


endmodule

