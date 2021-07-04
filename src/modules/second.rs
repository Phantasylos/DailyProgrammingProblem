#[allow(dead_code)]
pub fn multiply_slice(slice: &mut [i32]) -> &[i32] {
    let mut new_vec: Vec<i32> = Vec::new();

    let mut temp: i32 = 1;
    for i in 0..slice.len() {
        new_vec.push(temp);
        temp *= slice[i];
        println!("{}", new_vec[i]);
    }

    temp = 1;
    for i in (0..slice.len()).rev() {
        new_vec[i] *= temp;
        temp *= slice[i];
        slice[i] = new_vec[i];
        println!("{}", temp);
    }
    
    slice
}
