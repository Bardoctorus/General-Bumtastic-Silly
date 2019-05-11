let x = 5


function setup() {
  createCanvas(1000, 1000);
  stroke(50);
  tim = new Jimmy(100,100,100,100);
}

function draw() {
  background(200);
  tim.show();
  ellipse(10+x, 10+x, 10, 10);
  x++;
  

}