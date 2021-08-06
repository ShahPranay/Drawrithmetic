var canvas,ctx;
function onbodyload(){
    canvas=document.getElementById("drawing-canvas");
    ctx=canvas.getContext("2d");

    ctx.fillStyle="#fff";
    ctx.fillRect(0,0,canvas.width,canvas.height);
    ctx.lineWidth=6;
    var hold=false,curX,curY;
    canvas.onmousedown = function(e){
        hold=true;
        curX=e.clientX-canvas.offsetLeft;
        curY=e.clientY-canvas.offsetTop;
        ctx.beginPath();
        ctx.moveTo(curX,curY);
    };
    canvas.onmousemove = function(e){
        if(hold){
            curX=e.clientX-canvas.offsetLeft;
            curY=e.clientY-canvas.offsetTop;
            draw();
        }
    };
    canvas.onmouseup = function(e){
        hold=false;
    };
    canvas.onmouseout = function(e){
        hold=false;
    };
    function draw(){
        ctx.lineTo(curX,curY);
        ctx.stroke();
    }
}
function clearcanvas(){
    ctx.clearRect(0,0,420,140);
    ctx.fillStyle="#fff";
    ctx.fillRect(0,0,canvas.width,canvas.height);
    document.getElementById("answer").innerHTML='=';
}
function calculate(){
    img=canvas.toDataURL();
    console.log(img);
    var xhr=new XMLHttpRequest();
    xhr.open("post","/predict",true);
    xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    xhr.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200)
            document.getElementById("answer").innerHTML="="+xhr.responseText;
    }
    img=encodeURIComponent(img.substr(22));
    xhr.send("img="+img);
}