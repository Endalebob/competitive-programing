/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var m = ""+x
    var ans = true
    for (let i = 0; i < (m.length)/2; i++){
        if (m[i] != m[m.length-i-1]){
        ans = false
        }
            
    }
    return ans
};