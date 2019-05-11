q = 0;
e = 0;

function setup(){
    createCanvas(1000, 1000);
}

function draw(){
    background(100);
    noStroke();
    fill(0);
    ellipse(50+q, 50+q, 50+q, 50+q);
    fill(190 )
    textSize(16+q)
    text('B',50+q, 50+q)

    e++;
    if ( e >= 10){
        q++;
        e = 0;
    }
}