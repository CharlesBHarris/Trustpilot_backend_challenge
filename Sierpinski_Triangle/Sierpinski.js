var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "black";

//draw corners
ctx.fillRect(199, 0, 1, 1);
ctx.fillRect(399, Math.sqrt(3) * 399, 1, 1);
ctx.fillRect(0, Math.sqrt(3) * 399, 1, 1);

//take a guess for initial (X,Y)
var tempX = 400 * Math.random();
var tempY = Math.sqrt(3) * 400 * Math.random();


//We be looping...
for(var i = 0; i < 10000; i++){

    var cornertemp = Math.floor(3 * Math.random() + 1);
    if (cornertemp == 1){

        tempX = 0.5 * tempX;
        tempY = 0.5 * tempY + (100 * Math.sqrt(3));
        if (i > 1000){
            ctx.fillRect(tempX, tempY, 1, 1);
        }

        
    } else if (cornertemp == 2){

        tempX = 0.5 * tempX + 100;
        tempY = 0.5 * tempY;
        if (i > 1000){
            ctx.fillRect(tempX, tempY, 1, 1);
        }

    } else {
      
        tempX = 0.5 * tempX + 200;
        tempY = 0.5 * tempY + 100 * Math.sqrt(3);
        if (i > 1000){
            ctx.fillRect(tempX, tempY, 1, 1);
        }
    
    }  
  
}



