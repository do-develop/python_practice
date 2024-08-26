impl Solution {
    pub fn percentage_letter(s: String, letter: char) -> i32 {
        let word = s.as_bytes();
        let count = word.len();
        let character: u8 = letter.try_into().unwrap();
        let letter_count = word.iter().filter(|x| **x==character).count();
        return (letter_count * 100 / count).try_into().unwrap();
    }
}