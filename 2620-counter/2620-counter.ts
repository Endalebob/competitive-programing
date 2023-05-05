function createCounter(n: number): () => number {
    return function() {
        n += 1
        return n-1
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */