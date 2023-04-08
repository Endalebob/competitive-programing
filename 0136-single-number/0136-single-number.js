/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let check = new Set()
    let dupl = new Set()
    for (let i of nums){
        if (check.has(i)){
            dupl.add(i)
        }
        check.add(i)
    }
    for (let i of check){
        if(!dupl.has(i)){
            return i
        }
    }
    
};