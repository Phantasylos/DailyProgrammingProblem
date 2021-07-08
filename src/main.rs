mod modules;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first() {
        assert_eq!(modules::first::add_to_target(17, &[10, 15, 3, 7]), true);
    }

    #[test]
    fn test_second() {
        assert_eq!(modules::second::multiply_slice(&mut [1, 2, 3, 4, 5]), [120, 60, 40, 30, 24]);
    }

}


fn main() {
    assert_eq!(modules::first::add_to_target(17, &[10, 15, 3, 7]), true);
    assert_eq!(modules::second::multiply_slice(&mut [1, 2, 3, 4, 5]), [120, 60, 40, 30, 24]);
    assert_eq!(modules::fourth::find_continue(&mut [3, 4, -1, 1]), 2);
    assert_eq!(modules::fourth::find_continue(&mut [1, 2, 0]), 3);
    println!("Hello, world!");
}
