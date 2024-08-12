impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let mut largest = None;
        for i in 2..num.len() {
            let nums = &num.as_bytes()[i-2..=i];
            if(nums[0] == nums[1] && nums[1] == nums[2]){
                if let Some( curr ) = largest {
                    largest = Some(nums[0].max(curr)); 
                } else {
                    largest = Some(nums[0]);
                }
            }
        }
        if let Some(found_largest) = largest {
            return std::iter::repeat(found_largest as char).take(3).collect();
        } else {
            return "".to_string();
        }
    }
}