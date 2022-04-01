var sum = 0;
for (i = 1; i < 4000000; i += i){
    if (i % 2 == 0){
        sum += i;
    }
}
console.log(sum)