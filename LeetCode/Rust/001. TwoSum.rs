use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut table = HashMap::new();
        for (i, item) in nums.iter().enumerate() {
            let i = i as i32;
            if table.contains_key(item) {
                return vec![*table.get(item).unwrap(),i];
            }
            table.insert(target-item, i);
        }
        return vec![0];
    }
}
