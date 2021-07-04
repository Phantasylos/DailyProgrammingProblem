#[allow(dead_code)]
pub fn find_continue(slice: &mut [i32]) -> i32 {
    slice.sort();

    let mut expected_next: i32 = 1;
    for i in slice {
        if i == &expected_next {
            expected_next += 1;
        }
    }

    expected_next
}