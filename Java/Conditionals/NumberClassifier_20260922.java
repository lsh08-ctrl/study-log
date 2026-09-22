import java.util.Scanner;

public class numberclassifier_20260922 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String value; 
        
        // 양수일 때
        if (n > 0) {
            // 양수이면서 짝수이면
            if (n % 2 == 0) {
                value = "양의 짝수";
            }
            // 양수이면서 홀수이면
            else {
                value = "양의 홀수";
            }
        }
        // 양수가 아니면
        else {
            value = "양수 아님";
        }
        
        // 결과 출력
        System.out.println(value);
        sc.close();
    
    }
}
