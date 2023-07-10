// 옹알이(2)

import java.util.HashMap;
import java.util.Vector;

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
    public static int solution2(String[] babbling){
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


//    https://velog.io/@aoleejohn/C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%98%B9%EC%95%8C%EC%9D%B4-2
public static int solution3(String[] babbling)
{
    int answer=0;

    for(String s : babbling)
    {
        int flag=0; boolean j=true;
        for(int i=0; i<s.length(); i++)
        {
            if(s.substring(i,3)=="aya" && flag!=1) { flag=1; i+=2; }
            else if(s.substring(i,2)=="ma" && flag!=2) { flag=2; i+=1; }
            else if(s.substring(i,3)=="woo" & flag!=3) { flag=3; i+=2; }
            else if(s.substring(i,2)=="ye" && flag!=4) { flag=4; i+=1; }
            else { j=false; break; }
        }
        if(j==true) answer++;
    }

    return answer;
}



    public static void main(String[] args) {
        String[] babbling= {"ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"};
//        pass- 2

//        System.out.println(new Main().solution(babbling)); // x
        // System.out.println(solution2(babbling)); // 0
        System.out.println(solution3(babbling)); // 0
    }
}
