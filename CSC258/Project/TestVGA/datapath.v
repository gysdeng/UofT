module datapath(
	input resetn,
	input wren,
	input clk,

	input init,
	input move,

	output [7:0] x,
	output [6:0] y,
	output reg finish
	);

    reg [5:0] count;
    reg [7:0] loadx;
    reg [6:0] loady;

    always @(posedge clk)
    begin
	// if write is enabled, and not finished yet, begin
	// if it's moving
	if(wren == 1'b1 && finish == 1'b0) begin

	    if(resetn == 1'b1) begin
	    	count <= 0;
	    	finish <= 1'b0;
		end

	    if(init == 1'b1) begin
		loadx <= 8'd10;
		loady <= 7'd0;
		end
		
	    else begin // draw
		// put clock here
		count <= count + 1'b1;	
		end
	    end //end wren==1
	if(count == 6'b111111) begin
	    count <= 6'b000000;
	    finish <= 1'b1;
	    end

	// move
	if(move == 1'b1)
	    loady <= loady + 1'b1;
		
//	if(loadx == 8'b0)
//		loadx <= 8'b10;
	if(loadx == 7'b111_1111)
		loadx <= 7'b0;

    end // end always


	assign x = loadx + count[5:2];
	assign y = loady + count[1:0];
endmodule

