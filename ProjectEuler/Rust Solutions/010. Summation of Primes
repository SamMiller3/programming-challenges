// Project Euler Problem 10
// Find sum of primes under 2 million
// 13/07/25


fn main(){
    let mut primes = vec![true; 2_000_000]; // store to heap as large amount
    // use sieve of Eratosthene
    (primes[0], primes[1]) = (false, false);
    for i in 2..1414 { // sqrt of 2 million
        if primes[i] == true {
            for j in ((i*i)..2_000_000).step_by(i) {
                primes[j] = false;
            }
        }
    }  
    let mut sum = 0;
    for i in 0..2_000_000{
        if primes[i]{
            sum+=i;
        }
    }
    println!("{}", sum);
}
