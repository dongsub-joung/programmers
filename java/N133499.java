// 옹알이(2)

import java.util.HashMap;

public class N133499 {

//    Its not work
    public int solution(String[] babbling) {
        int answer = 0;
        String[] buff= {"aya", "ye", "woo", "ma"};
        for (var babble: buff){
            for (int i=0; i< babbling.length; i++){
                if (babble == babbling[i]){
                    answer+=1;
                }
            }
        }
        return answer;
    }

//    https://velog.io/@subbni/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EC%98%B9%EC%95%8C%EC%9D%B42-Java
    public int solution2(String[] babbling){
        int answer= 0;
        HashMap<Character, String> words= new HashMap<>(){{
           put('a', "aya");
           put('y', "ye");
           put('w', "woo");
           put('m', "ma");
        }};

        for (var str: babbling){
            char prev= '\u0000';
            int i=0;
            for (;i< str.length();){
                if(prev == str.charAt(i))
                    break;

                String word= words.getOrDefault(str.charAt(i), "");
                if (word.equals(""))
                    break;

                String curStr= str.substring(i, Math.min(str.length(), i + word.length()));
                if (curStr.equals(word)){
                    prev= str.charAt(i);
                    i+= word.length();
                }else
                    break;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        String[] babbling= {"ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"};
//        2
//        System.out.println(new Main().solution(babbling));
        System.out.println(new Main().solution2(babbling));


    }
}
