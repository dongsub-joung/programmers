// I cant solve it.


fn solution(strs: &str, n: usize) -> String{
    let mut answer= String::new();
    let char_list= strs.chars();
    
    for e in char_list{
        for _ in 0..n{
            answer= format!("{}", e);
        }
    }
    
    answer
}

fn main(){
    solution("hello", 3);
}

#[cfg(test)]
mod testing{
    use super::*;

    #[test]
    fn name() {
        let expect= String::from("hhheeellllllooo");
        assert_eq!(expect, solution("hello", 3usize))
    }
}
