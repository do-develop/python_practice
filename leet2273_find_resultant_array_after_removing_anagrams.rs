impl Solution {
    pub fn remove_anagrams(mut words: Vec<String>) -> Vec<String> {
        let mut i = words.len() - 1;

        while i > 0 {
            let mut current = words[i].as_bytes().to_vec();
            let mut previous = words[i - 1].as_bytes().to_vec();
            current.sort_unstable();
            previous.sort_unstable();
            if(current == previous){
                words.remove(i);             
            }
            i -= 1 
        }
        return words
    }
}