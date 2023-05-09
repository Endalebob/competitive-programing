function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    return arr.filter((num,i)=>fn(num,i))

};