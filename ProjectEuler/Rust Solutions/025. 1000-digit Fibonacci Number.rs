// Project Euler Problem 25 find index of first 1000 digit fib number
// 07/07/2025
use num::BigUint;
use num::FromPrimitive; // Use big int as 1000 digits exceeds native 128 bit

fn main() {
    let mut a = BigUint::from_u8(0).unwrap();
    let mut b = BigUint::from_u8(1).unwrap();
    let mut index: i32 = 1;

    while b.to_string().len() < 1000 {
        let temp = b.clone();
        b += a;
        a = temp;
        index += 1;
    }

    println!("Index: {}", index);
}
