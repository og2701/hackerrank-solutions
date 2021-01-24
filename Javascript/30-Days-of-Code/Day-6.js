function processData(input) {
    input = input.split("\n");
    n = input[0];
    for(var i=0; i<n; i++){
        s = input[i+1];
        for(var j=0; j<s.length; j+=2){
            process.stdout.write(s[j]);
        }
        process.stdout.write(' ');
        for(var j=1; j<s.length; j+=2){
            process.stdout.write(s[j]);
        }
        console.log();
    }
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
