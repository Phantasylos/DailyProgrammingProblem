#[allow(dead_code)]
pub fn add_to_target(target: i32, slice: &[i32]) -> bool {
    let slice_length = slice.len();
    for (i, item) in slice.iter().enumerate() {
        let remainder = target - item;
        if slice[i + 1..slice_length].contains(&remainder) {
            return true;
        }
    }
    false
}