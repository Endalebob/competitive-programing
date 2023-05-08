function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const ans = new Array<number>(arr.length)
    for(let i=0; i<arr.length; i++){
        ans[i] = (fn(arr[i],i))
    }
    return ans
};