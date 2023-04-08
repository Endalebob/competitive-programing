/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x<0){
        return false;
    }
    let num = 0;
    let num1 = x;
    while (x>0){
        last_digit = x % 10
        num = num * 10 + last_digit
        x = Math.floor(x/10)
    }
    return num == num1
};